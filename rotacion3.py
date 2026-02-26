import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

def body_axes_from_quaternion(q):
    r = R.from_quat([q[1], q[2], q[3], q[0]])
    Rmat = r.as_matrix().T

    x_b = Rmat @ np.array([1, 0, 0])
    y_b = Rmat @ np.array([0, 1, 0])
    z_b = Rmat @ np.array([0, 0, 1])

    return x_b, y_b, z_b


# --- cargar data ---
data = np.loadtxt("cuaterniones_4.csv", delimiter=",", skiprows=1)
timestamps = data[:, 0] * 1e-9
quaternions = data[:, 1:5]

# --- figura ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# quivers iniciales
xq = ax.quiver(0,0,0, 1,0,0, color='r', length=1)
yq = ax.quiver(0,0,0, 0,1,0, color='g', length=1)
zq = ax.quiver(0,0,0, 0,0,1, color='b', length=1)

t0 = timestamps[0]
dt_anim = 1.0   # 1 segundo real

i = 0
while i < len(quaternions):
    q = quaternions[i]
    t = timestamps[i] - t0

    x_b, y_b, z_b = body_axes_from_quaternion(q)

    xq.remove()
    yq.remove()
    zq.remove()

    xq = ax.quiver(0,0,0, *x_b, color='r', length=1)
    yq = ax.quiver(0,0,0, *y_b, color='g', length=1)
    zq = ax.quiver(0,0,0, *z_b, color='b', length=1)

    ax.set_title(f"Orientación IMU | t = {t:.2f} s")

    plt.pause(dt_anim)

    # avanzar ~1 segundo en data (≈100 muestras)
    i += 100