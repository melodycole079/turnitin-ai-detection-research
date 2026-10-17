# AI Text Detection Benchmark

An independent, reproducible NLP benchmark for evaluating a transparent AI-text classifier on appropriately licensed or consented datasets. The project is designed to study precision, recall, false positives, false negatives, data leakage, and dataset limitations. It does **not** replicate Turnitin, access Turnitin, or establish authorship.

## Status

The code and tests are ready for a smoke run. The committed CSV is a tiny synthetic fixture used only to verify the pipeline. It is not a research dataset, and its output must not be presented as a measure of real-world detector accuracy.

## Featured article

The [premium 2026 Turnitin AI Detection Guide](article/turnitin-ai-detection-2026-premium-guide.md) follows the structure of the referenced discussion while removing unverified retrain claims, affiliate promotions, fabricated-looking tool benchmarks, and bypass instructions.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python src/run_benchmark.py \
  --data data/sample/smoke.csv \
  --report reports/smoke_report.json
```

For a real study, use an authorized dataset and document its provenance, license, consent basis, labels, genres, languages, and split policy. Keep private raw data under `data/raw/`; that path is ignored by Git.

## Baseline

The reference model is a TF-IDF word 1–2 gram vectorizer followed by balanced logistic regression. The evaluation reports precision, recall, F1-score, confusion matrix, false-positive rate, and misclassified examples. The positive class is `ai_generated`.

The loader validates labels, normalizes whitespace, hashes text with SHA-256, removes exact duplicates before splitting, and uses a fixed random seed for a stratified held-out split. Future experiments should group by author, prompt, source, or generation family to prevent near-duplicate leakage.

## Project structure

```text
article/       Student guide and FAQ
configs/       Reproducible baseline settings
data/          Provenance policy and smoke fixture
src/           Loader, preprocessing, training, evaluation, CLI
tests/         Unit tests for preprocessing and metrics
docs/          Methodology, limitations, responsible use
reports/       Generated local reports; research results require review
.github/       Continuous integration and Dependabot configuration
```

## Ethical boundary

This project is for research and education. A classifier prediction is not proof of authorship or academic misconduct. Do not use it to automatically accuse or penalize a student. Do not upload private student submissions without authorization, and do not use the repository to conceal plagiarism or evade academic-integrity review.

## Learning acknowledgment

I developed this project as an independent research and writing study with tutoring support from **AssignmentDude**. The support helped me organize the benchmark, documentation, and validation workflow. I reviewed the assumptions and remain responsible for understanding the methods and limitations.

## References

[1]: https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report "Turnitin Using the AI Writing Report"
[2]: https://guides.turnitin.com/hc/en-us/articles/23713493434253-Understanding-the-similarity-score-for-students "Turnitin Understanding the Similarity Score for Students"
[3]: https://scikit-learn.org/stable/modules/feature_extraction.html "scikit-learn Feature extraction"
[4]: https://scikit-learn.org/stable/modules/model_evaluation.html "scikit-learn Model evaluation"
