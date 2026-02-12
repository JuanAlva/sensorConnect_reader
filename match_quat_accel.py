import pandas as pd

# --- cargar cuaterniones ---
df_q = pd.read_csv(
    "cuaterniones.csv",
    parse_dates=["Time"],
    dayfirst=True
)

df_q = df_q.rename(columns={
    "inertial-6286.188861:estOrientQuaternion[0-0]": "q0",
    "inertial-6286.188861:estOrientQuaternion[0-1]": "q1",
    "inertial-6286.188861:estOrientQuaternion[0-2]": "q2",
    "inertial-6286.188861:estOrientQuaternion[0-3]": "q3",
})

df_q = df_q[df_q["inertial-6286.188861:estOrientQuaternion:valid"] == 1]


# --- cargar aceleraciones ---
df_a = pd.read_csv(
    "accel.csv",
    skiprows=1,                 # salta DATA_START
    parse_dates=["Time"],
    dayfirst=True
)

df_a = df_a.rename(columns={
    "inertial-6286.188861:estLinearAccelX": "ax",
    "inertial-6286.188861:estLinearAccelY": "ay",
    "inertial-6286.188861:estLinearAccelZ": "az",
})

df_a = df_a[
    (df_a["inertial-6286.188861:estLinearAccelX:valid"] == 1) &
    (df_a["inertial-6286.188861:estLinearAccelY:valid"] == 1) &
    (df_a["inertial-6286.188861:estLinearAccelZ:valid"] == 1)
]


# --- MATCH TEMPORAL (INTERSECCIÓN) ---
df = pd.merge(
    df_q,
    df_a,
    on="Time",
    how="inner"
)

df = df.sort_values("Time").reset_index(drop=True)