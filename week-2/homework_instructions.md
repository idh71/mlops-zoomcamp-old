Question 1:

- **Question:** `mlflow --version`
- **Response:** `mlflow, version 2.3.0`

Question 2:

To run the `preprocess_data` script:
```
python preprocess_data.py --raw_data_path ./data --dest_path ./output
```

To check the size of the `dv` that is created:
```
cd ./output
ls -lh
```
The closest answer is 154kb.

Question 3:

To start the MLflow UI:
```
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Make the necessary alterations to the `train.py` script:
1. `mlflow.sklearn.autolog()`
2. Wrap the appropriate portion with `with mlflow.start_run()`

```
python train.py
```

Check out the parameters under the new experiment run, and I see that the value of `max_depth` is 10.

Question 4:

To launch the MLflow tracking server locally:
```
mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts
```

Changed the `hpo.py` script to log params and log the RMSE. In checking the UI and ranking by RMSE, the best performance was 2.45.

Question 5:

To answer this question, you need to write code into the `register_model.py` file that uses the MLflow client to select a certain number of runs based on given criteria. See the script to see how it was done.

I made the necessary changes to the `register_model.py` script to select the best 5 models, then run them on the test set and register the best. The RMSE of the best model was 2.285, so the closest answer is 2.185.

Question 6:

The information that the Model Registry UI appears to have is the version number.
