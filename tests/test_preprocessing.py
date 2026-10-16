import pandas as pd
import pytest
from preprocessing import normalize_text
from data_loader import validate_dataset, remove_exact_duplicates

def test_normalize_text_collapses_whitespace():
    assert normalize_text('  a\n\tb  ')=='a b'

def test_validate_rejects_unknown_label():
    with pytest.raises(ValueError): validate_dataset(pd.DataFrame({'text':['x'],'label':['maybe']}))

def test_duplicate_removal_is_explicit():
    frame=validate_dataset(pd.DataFrame({'text':['same','same','other'],'label':['human','human','ai_generated']}))
    result,count=remove_exact_duplicates(frame)
    assert len(result)==2 and count==1
