from evaluate import evaluate_classifier
import pandas as pd
class Model:
    def predict(self, texts): return ['human','ai_generated','ai_generated','human']

def test_metrics_and_false_positive_rate():
    frame=pd.DataFrame({'text':['a','b','c','d'],'label':['human','human','ai_generated','ai_generated']})
    report=evaluate_classifier(Model(),frame)
    assert report['confusion_matrix']==[[1,1],[1,1]]
    assert report['false_positive_rate']==0.5
