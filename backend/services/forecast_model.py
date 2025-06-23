import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import io

def forecast_kpi(file_bytes) -> float:
    df = pd.read_csv(io.BytesIO(file_bytes))
    
    # Expecting two columns: Year and KPI_Value (e.g., Water_Usage)
    X = df.iloc[:, 0].values.reshape(-1, 1)  # e.g., Year
    y = df.iloc[:, 1].values  # e.g., KPI values

    model = LinearRegression()
    model.fit(X, y)

    next_year = np.array([[X[-1][0] + 1]])
    prediction = model.predict(next_year)

    return float(prediction[0]), int(next_year[0][0])
