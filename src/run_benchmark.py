import argparse, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from data_loader import load_csv, leakage_aware_split
from preprocessing import prepare_texts
from train import fit_classifier
from evaluate import evaluate_classifier, save_report

def main():
    p=argparse.ArgumentParser(description='Run the independent AI-text benchmark')
    p.add_argument('--data',required=True); p.add_argument('--report',default='results/benchmark_report.json'); p.add_argument('--random-state',type=int,default=42)
    args=p.parse_args(); frame=load_csv(args.data); frame['text']=prepare_texts(frame['text']); train,test=leakage_aware_split(frame,random_state=args.random_state)
    model=fit_classifier(train,args.random_state); report=evaluate_classifier(model,test); report.update({'dataset':str(args.data),'n_train':len(train),'duplicate_policy':'exact SHA-256 text duplicates removed before split','random_state':args.random_state,'status':'demonstration only; not a validated estimate of real-world detector performance'})
    save_report(report,args.report); print(f"wrote {args.report} ({len(train)} train / {len(test)} test rows)")
if __name__=='__main__': main()
