import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Cargar datos (ajusta el nombre del archivo)
df = pd.read_csv(
    "SensorConnectData3.csv",
    skiprows=lambda x: x < 16,   # DATA_START
    header=None
)

df.columns = ["time", "q0", "q1", "q2", "q3", "valid"]

# Convertir tiempo a segundos relativos
df["time"] = pd.to_datetime(df["time"])
t0 = df["time"].iloc[0]
df["t"] = (df["time"] - t0).dt.total_seconds()

norm_q = np.sqrt(
    df["q0"]**2 +
    df["q1"]**2 +
    df["q2"]**2 +
    df["q3"]**2
)

plt.figure()
plt.plot(df["t"], norm_q)
plt.axhline(1.0, linestyle="--")
plt.xlabel("Tiempo [s]")
plt.ylabel("||q||")
plt.title("Norma del cuaternión")
plt.grid()
plt.show()
