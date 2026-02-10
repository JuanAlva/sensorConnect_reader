import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos (ajusta el nombre del archivo)
df = pd.read_csv(
    "SensorConnectData6.csv",
    skiprows=lambda x: x < 4,   # DATA_START
    header=None
)

df.columns = ["time", "q0", "q1", "q2", "q3", "valid"]

# Convertir tiempo a segundos relativos
df["time"] = pd.to_datetime(df["time"])
t0 = df["time"].iloc[0]
df["t"] = (df["time"] - t0).dt.total_seconds()

''' Cuaternion vs tiempo '''
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

import numpy as np
''' Normalización del cuaterión en el tiempo'''
# norm_q = np.sqrt(
#     df["q0"]**2 +
#     df["q1"]**2 +
#     df["q2"]**2 +
#     df["q3"]**2
# )

# plt.figure()
# plt.plot(df["t"], norm_q)
# plt.axhline(1.0, linestyle="--")
# plt.xlabel("Tiempo [s]")
# plt.ylabel("||q||")
# plt.title("Norma del cuaternión")
# plt.grid()
# plt.show()

''' Cuaternión a Euler'''
# def quat_to_euler(q0, q1, q2, q3):
#     import numpy as np

#     roll = np.arctan2(
#         2*(q0*q1 + q2*q3),
#         1 - 2*(q1*q1 + q2*q2)
#     )

#     pitch = np.arcsin(
#         2*(q0*q2 - q3*q1)
#     )

#     yaw = np.arctan2(
#         2*(q0*q3 + q1*q2),
#         1 - 2*(q2*q2 + q3*q3)
#     )

#     return roll, pitch, yaw

# r, p, y = quat_to_euler(df.q0, df.q1, df.q2, df.q3)

# # grados
# r = np.degrees(r)
# p = np.degrees(p)
# y = np.degrees(y)

# plt.figure()
# plt.plot(df["t"], r, label="Roll")
# plt.plot(df["t"], p, label="Pitch")
# plt.plot(df["t"], y, label="Yaw")
# plt.legend()
# plt.xlabel("Tiempo [s]")
# plt.ylabel("Ángulo [deg]")
# plt.title("Orientación en ángulos de Euler")
# plt.grid()
# plt.show()



''' Vector rotado'''
# def quat_rotate(q, v):
#     q0, q1, q2, q3 = q
#     R = np.array([
#         [1-2*(q2**2+q3**2), 2*(q1*q2-q0*q3), 2*(q1*q3+q0*q2)],
#         [2*(q1*q2+q0*q3), 1-2*(q1**2+q3**2), 2*(q2*q3-q0*q1)],
#         [2*(q1*q3-q0*q2), 2*(q2*q3+q0*q1), 1-2*(q1**2+q2**2)]
#     ])
#     return R @ v

# g = np.array([0, 0, 1])

# gz = []
# for _, row in df.iterrows():
#     v = quat_rotate([row.q0, row.q1, row.q2, row.q3], g)
#     gz.append(v[2])

# plt.figure()
# plt.plot(df["t"], gz)
# plt.xlabel("Tiempo [s]")
# plt.ylabel("g_z rotado")
# plt.title("Dirección de la gravedad estimada")
# plt.grid()
# plt.show()
