1. The mlflow version is 2.3.0

2. dv.pkl is closest to 154 kb (it appears to be closer to 151kb)

3.  `asas` 
the value of the max_depth parameter logged was 10

4.  -mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts

altered part of the hpo.py script:
```with mlflow.start_run():
            mlflow.log_params(params)
            rf = RandomForestRegressor(**params)
            rf.fit(X_train, y_train)
            y_pred = rf.predict(X_val)
            rmse = mean_squared_error(y_val, y_pred, squared=False)
            mlflow.log_metric("val_rmse", rmse)
```
the best val_rmse i got was 2.45

5.  2.185 is the closest

6.  Version number
