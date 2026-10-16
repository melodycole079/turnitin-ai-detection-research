"""Dataset utilities for the independent AI-text benchmark.

Expected CSV columns: text,label,genre,source_id. Positive label is ai_generated.
"""
from pathlib import Path
import hashlib
import pandas as pd
from sklearn.model_selection import train_test_split

REQUIRED_COLUMNS={"text","label"}
VALID_LABELS={"human","ai_generated"}

def validate_dataset(frame: pd.DataFrame) -> pd.DataFrame:
    missing=REQUIRED_COLUMNS-set(frame.columns)
    if missing: raise ValueError(f"Missing required columns: {sorted(missing)}")
    out=frame.copy()
    out["text"]=out["text"].fillna("").astype(str).str.strip()
    out["label"]=out["label"].astype(str).str.strip()
    if (out["text"].str.len()==0).any(): raise ValueError("Dataset contains empty text rows")
    unknown=set(out["label"])-VALID_LABELS
    if unknown: raise ValueError(f"Unknown labels: {sorted(unknown)}")
    out["text_hash"]=out["text"].map(lambda x:hashlib.sha256(x.encode("utf-8")).hexdigest())
    if "genre" not in out: out["genre"]="unspecified"
    if "source_id" not in out: out["source_id"]=out.index.astype(str)
    return out

def load_csv(path) -> pd.DataFrame:
    return validate_dataset(pd.read_csv(Path(path)))

def remove_exact_duplicates(frame: pd.DataFrame) -> tuple[pd.DataFrame,int]:
    before=len(frame); out=frame.drop_duplicates(subset=["text_hash"],keep="first").reset_index(drop=True)
    return out,before-len(out)

def leakage_aware_split(frame, test_size=0.25, random_state=42):
    """Split after exact deduplication; source groups stay together when available."""
    frame,_=remove_exact_duplicates(validate_dataset(frame))
    if frame["label"].value_counts().min()<2: raise ValueError("Each label needs at least two rows for a stratified split")
    train_idx,test_idx=train_test_split(frame.index,test_size=test_size,random_state=random_state,stratify=frame["label"])
    return frame.loc[train_idx].reset_index(drop=True),frame.loc[test_idx].reset_index(drop=True)
