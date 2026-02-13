import pandas as pd

def match_quat_accel():
    # --- cargar cuaterniones ---
    df_q = pd.read_csv("quat3.csv")

    df_q = df_q.rename(columns={
        "inertial-6286.188861:estOrientQuaternion[0-0]": "q0",
        "inertial-6286.188861:estOrientQuaternion[0-1]": "q1",
        "inertial-6286.188861:estOrientQuaternion[0-2]": "q2",
        "inertial-6286.188861:estOrientQuaternion[0-3]": "q3",
        "inertial-6286.188861:estOrientQuaternion:valid": "qValid",
    })

    # Comprobar si es un valor válido
    # df_q = df_q[df_q["inertial-6286.188861:estOrientQuaternion:valid"] == 1]

    # df_q["dt"] = df_q["Time"].diff() * 1e-9
    # print(df_q)

    df_q["time_comp"] = df_q["Time"] * 1e-8
    df_q["time_comp"] = df_q["time_comp"].astype(int)
    df_q["time_comp"]

    # df_q

    df_q["time_comp"] = df_q["Time"] * 1e-8
    df_q["time_comp"] = df_q["time_comp"].astype(int)
    df_q["time_comp"]

    # cargar aceleraciones
    df_a = pd.read_csv("accel3.csv")

    # renombrar columnas
    df_a = df_a.rename(columns={
        "inertial-6286.188861:estLinearAccelX": "ax",
        "inertial-6286.188861:estLinearAccelX:valid": "aXvalid",
        "inertial-6286.188861:estLinearAccelY": "ay",
        "inertial-6286.188861:estLinearAccelY:valid": "aYvalid",
        "inertial-6286.188861:estLinearAccelZ": "az",
        "inertial-6286.188861:estLinearAccelZ:valid": "aZvalid",
    })

    # quedarnos solo con datos válidos
    df_a = df_a[
        (df_a["aXvalid"] == 1) &
        (df_a["aYvalid"] == 1) &
        (df_a["aZvalid"] == 1)
    ]

    # df_a.drop(["aZvalid", "aYvalid", "aXvalid"], axis=1)

    df_a["time_comp"] = df_a["Time"]*1e-8
    df_a["time_comp"] = df_a["time_comp"].astype(int)
    df_a["time_comp"] 

    # df_a

    df_u = pd.merge(
        df_q,
        df_a,
        on="time_comp",
        how="inner"
    )
    # df_u

    df_u = df_u.rename(columns={"Time_x": "time"})
    df_u.drop(["Time_y"], axis=1, inplace=True)
    # df_u

    df_u["dt"] = df_u["time"].diff() * 1e-9
    # df_u

    new_order = ['time', 'q0', 'q1', 'q2', 'q3', 'az', 'ax', 'ay', 'dt']
    df_u = df_u[new_order]
    # print(df_u)
    return df_u

df = match_quat_accel()
# print(df)

# print(len(df))
for i in range(len(df)):
    dt = df.loc[i, "dt"]
    q  = df.loc[i, ["q0","q1","q2","q3"]].values
    a_b = df.loc[i, ["ax","ay","az"]].values
    print(dt, q, a_b, "\n")

# print(dt, q, a_b)