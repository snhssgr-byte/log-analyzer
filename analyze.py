import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("network_log.csv")

model = IsolationForest(contamination=0.05, random_state=0)
data["flag"] = model.fit_predict(data[["requests_per_min"]])

median = data["requests_per_min"].median()
suspicious = data[(data["flag"] == -1) & (data["requests_per_min"] > median)]

suspicious.to_csv("suspicious_ips.csv", index=False)
print(suspicious)
