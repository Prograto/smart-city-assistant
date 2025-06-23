import pandas as pd
import io

def detect_anomalies(file_bytes):
    df = pd.read_csv(io.BytesIO(file_bytes))
    
    # Assumes the second column contains numeric KPI values
    values = df.iloc[:, 1]
    mean = values.mean()
    std = values.std()

    # Flag values that are more than 3 std deviations away
    anomalies = df[values > mean + 3 * std]

    return anomalies.to_dict(orient="records")
