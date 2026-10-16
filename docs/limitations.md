# Limitations

The baseline classifier learns statistical associations in the selected dataset. It does not identify authorship, intent, or academic misconduct. Dataset labels can be noisy, and human writing varies by language, discipline, proficiency, editing history, and assignment type. Performance can also change when generation models, prompts, or paraphrasing tools change.

A held-out split reduces one form of leakage but does not guarantee external validity. A stronger study would use author- or prompt-grouped splits, time-based evaluation, cross-genre tests, multilingual data, calibration analysis, and confidence intervals across repeated runs.

The repository does not upload submissions to Turnitin, access Turnitin accounts, or reproduce Turnitin's proprietary detector. It is an independent NLP benchmark for understanding classifier behavior.
