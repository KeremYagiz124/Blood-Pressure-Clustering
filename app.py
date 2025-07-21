import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def parse_blood_pressure(bp):
    try:
        systolic, diastolic = bp.split("/")
        return int(systolic), int(diastolic)
    except Exception as error:
        return np.nan, np.nan

def main():
    # Read Excel data
    data = pd.read_excel("blood_pressure.xlsx")

    data[["morning_systolic", "morning_diastolic"]] = data["Morning BP"].apply(lambda x: pd.Series(parse_blood_pressure(x)))
    data[["evening_systolic", "evening_diastolic"]] = data["Evening BP"].apply(lambda x: pd.Series(parse_blood_pressure(x)))

    features = data[["morning_systolic", "morning_diastolic", "evening_systolic", "evening_diastolic"]].dropna()

    kmeans = KMeans(n_clusters=2, random_state=42)
    clusters = kmeans.fit_predict(features)
    features["cluster"] = clusters

    cluster_means = features.groupby("cluster").mean()[["morning_systolic", "evening_systolic"]]
    risky_cluster = cluster_means.mean(axis=1).idxmax()

    features["risk"] = features["cluster"].apply(lambda x: "Risk" if x == risky_cluster else "Normal")

    # Merge with original data
    data = data.join(features["risk"])

    risk_count = data["risk"].value_counts().get("Risk", 0)
    total = data["risk"].count()
    overall_risk = "High Blood Pressure / Heart Risk" if risk_count / total >= 0.5 else "Normal Blood Pressure"

    print("Daily Risk Assessments")
    print(data[["Date", "risk"]])
    print("\nOverall Evaluation:", overall_risk)

if __name__ == '__main__':
    main()
