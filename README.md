# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/AkashKulkarni4444/KidneyDiseaseClassification
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/AkashKulkarni4444/KidneyDiseaseClassification.mlflow
MLFLOW_TRACKING_USERNAME=AkashKulkarni4444
MLFLOW_TRACKING_PASSWORD=a5822a71ae059c7a235dcb34190305eb72d1b62e
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/AkashKulkarni4444/KidneyDiseaseClassification.mlflow

export MLFLOW_TRACKING_USERNAME=AkashKulkarni4444

export MLFLOW_TRACKING_PASSWORD=a5822a71ae059c7a235dcb34190305eb72d1b62e

```
<!-- dvc repro  -->
<!-- dvc dag show dependance-->