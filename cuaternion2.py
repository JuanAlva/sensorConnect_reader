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

# Plot
plt.figure()
plt.plot(df["t"], df["q0"], label="q0")
plt.plot(df["t"], df["q1"], label="q1")
plt.plot(df["t"], df["q2"], label="q2")
plt.plot(df["t"], df["q3"], label="q3")
plt.legend()
plt.xlabel("Tiempo [s]")
plt.ylabel("Valor del cuaternión")
plt.title("Componentes del cuaternión")
plt.grid()
plt.show()
