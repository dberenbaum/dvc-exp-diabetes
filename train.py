import joblib
import yaml
from sklearn.datasets import load_diabetes
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split


# Load params.
with open("params.yaml") as f:
    params = yaml.safe_load(f)

# Load data.
data_dict = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=0)

# Fit model.
regr = ElasticNet(alpha=params["alpha"], l1_ratio=0.9)
regr.fit(X_train, y_train)

# Evaluate model.
metrics = {}
metrics["r2"] = regr.score(X_test, y_test)
with open("metrics.yaml", "w") as f:
    yaml.dump(metrics, f)

# Save model.
joblib.dump(regr, "model.joblib")
