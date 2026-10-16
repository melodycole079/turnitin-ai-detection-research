from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def build_classifier(random_state=42):
    return Pipeline([
        ("tfidf",TfidfVectorizer(lowercase=True,ngram_range=(1,2),max_features=50000,strip_accents="unicode")),
        ("classifier",LogisticRegression(max_iter=1000,class_weight="balanced",random_state=random_state)),
    ])

def fit_classifier(train_frame, random_state=42):
    model=build_classifier(random_state)
    model.fit(train_frame["text"],train_frame["label"])
    return model
