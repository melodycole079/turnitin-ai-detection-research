import json
from pathlib import Path
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_classifier(model, test_frame):
    y_true=test_frame["label"].tolist(); y_pred=model.predict(test_frame["text"])
    report=classification_report(y_true,y_pred,labels=["human","ai_generated"],output_dict=True,zero_division=0)
    cm=confusion_matrix(y_true,y_pred,labels=["human","ai_generated"]).tolist()
    tn,fp,fn,tp=cm[0][0],cm[0][1],cm[1][0],cm[1][1]
    return {"positive_class":"ai_generated","n_test":len(test_frame),"classification_report":report,"confusion_matrix_labels":["human","ai_generated"],"confusion_matrix":cm,"false_positive_rate":fp/(fp+tn) if fp+tn else None,"error_rows":[{"text":text,"true_label":true,"predicted_label":pred} for text,true,pred in zip(test_frame["text"],y_true,y_pred) if true!=pred]}

def save_report(report,path):
    Path(path).parent.mkdir(parents=True,exist_ok=True); Path(path).write_text(json.dumps(report,indent=2))
