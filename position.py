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

    new_order = ['time', 'q0', 'q1', 'q2', 'q3', 'ax', 'ay', 'az', 'dt']
    df_u = df_u[new_order]
    # print(df_u)
    return df_u

df = match_quat_accel()
# print(df)




''''''
# # print(len(df))
# for i in range(len(df)):
#     time = df.loc[i, "time"]
#     dt = df.loc[i, "dt"]
#     q  = df.loc[i, ["q0","q1","q2","q3"]].values
#     a_b = df.loc[i, ["ax","ay","az"]].values
#     print(time, dt, q, a_b, "\n")

# print(dt, q, a_b)

# for cada instante k:
#     leer a_body(k)
#     leer q(k)


#     # from scipy.spatial.transform import Rotation as R

#     # r = R.from_quat([qx, qy, qz, q0])
#     # a_nav = r.as_matrix().T @ a_body

#     R = R(q)
#     a_nav = R^T a_body

#     # v = v + a_nav * dt
#     v(k) = v(k-1) + a_nav * dt

#     # p = p + v * dt
#     p(k) = p(k-1) + v(k) * dt

# interp_quaternion()

import numpy as np
from scipy.spatial.transform import Rotation as R

def ins_step(p, v, q, a_body, dt):
    """
    p      : posición inercial actual (3,)
    v      : velocidad inercial actual (3,)
    q      : cuaternión [q0, qx, qy, qz] (AHRS)
    a_body : aceleración lineal en body frame (3,)
    dt     : paso de tiempo [s]

    devuelve:
    p_new, v_new
    """

    # 1) Normalizar cuaternión (seguridad numérica)
    q = q / np.linalg.norm(q)

    # 2) Rotación body → inercial (pasiva)
    r = R.from_quat([q[1], q[2], q[3], q[0]])
    R_nb = r.as_matrix().T   # body → nav

    # 3) Aceleración en marco inercial
    a_nav = R_nb @ a_body

    # 4) Integración aceleración → velocidad
    v_new = v + a_nav * dt

    # 5) Integración velocidad → posición
    p_new = p + v_new * dt

    return p_new, v_new


'''N = 10
dt = 0.1

df = pd.DataFrame({
    "time": np.arange(N) * dt,
    "dt": [dt]*N,
    "q0": [1]*N,
    "q1": [0]*N,
    "q2": [0]*N,
    "q3": [0]*N,
    "ax": [0]*N,
    "ay": [0]*N,
    "az": [0]*N,
})'''


# a = 1.0  # m/s^2
# dt = 0.1
# N = 10

'''df = pd.DataFrame({
    "time": np.arange(N) * dt,
    "dt": [dt]*N,
    "q0": [1]*N,
    "q1": [0]*N,
    "q2": [0]*N,
    "q3": [0]*N,
    "ax": [a]*N,
    "ay": [0]*N,
    "az": [0]*N,
})'''


'''from math import sqrt

q0 = sqrt(2)/2
qz = sqrt(2)/2

df = pd.DataFrame({
    "time": np.arange(N) * dt,
    "dt": [dt]*N,
    "q0": [q0]*N,
    "q1": [0]*N,
    "q2": [0]*N,
    "q3": [qz]*N,
    "ax": [1]*N,   # acelera en X-body
    "ay": [0]*N,
    "az": [0]*N,
})'''


p = np.zeros(3)
v = np.zeros(3)

for k in range(1, len(df)):

    # dt = t[k] - t[k-1]
    time = df.loc[k, "time"]
    dt = df.loc[k, "dt"]
    quat  = df.loc[k, ["q0","q1","q2","q3"]].values
    a_body = df.loc[k, ["ax","ay","az"]].values

    p, v = ins_step(p, v, quat, a_body, dt)

    # print(f"t={time[k]:.3f}  p={p}  v={v}")
    print(f"t={time:.3f}  v={v}  p={p}")

    # print(dt, q, a_b, "\n")