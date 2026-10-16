# Methodology

The benchmark treats `ai_generated` as the positive class and `human` as the negative class. The baseline is a TF-IDF word n-gram representation followed by balanced logistic regression. This is a transparent reference classifier, not a replica of Turnitin's proprietary system.

The loader validates labels and non-empty text, computes SHA-256 text hashes, removes exact duplicate text, and performs a stratified held-out split with a fixed random seed. Future studies should also group related documents by author, prompt, source, or generation family before splitting. Otherwise, near-duplicates can leak information from training into evaluation.

The report includes precision, recall, F1-score, a confusion matrix, false-positive rate, and misclassified examples. Results should be stratified by genre, language, text length, and generation source when the dataset supports those analyses. A single benchmark cannot establish general performance across institutions, languages, models, or writing contexts.

## Reproduction

```bash
python -m pip install -r requirements.txt
python src/run_benchmark.py --data data/sample/smoke.csv --report reports/smoke_report.json
```

The smoke fixture is intentionally too small for a meaningful research claim. Replace it with a documented, appropriately licensed dataset before reporting results.
