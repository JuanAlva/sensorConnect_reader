import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

def body_axes_from_quaternion(q):
    """
    q = [q0, qx, qy, qz]
    devuelve ejes del cuerpo en el marco inercial
    """
    r = R.from_quat([q[1], q[2], q[3], q[0]])  # scipy usa [x,y,z,w]
    Rmat = r.as_matrix().T  # rotación pasiva

    x_b = Rmat @ np.array([1, 0, 0])
    y_b = Rmat @ np.array([0, 1, 0])
    z_b = Rmat @ np.array([0, 0, 1])

    return x_b, y_b, z_b

# import numpy as np

# leer archivo
data = np.loadtxt("quat3.csv", delimiter=",", skiprows=1)

timestamps = data[:, 0]          # unix ns
quaternions = data[:, 1:5]       # q0 qx qy qz

timestamps_sec = timestamps * 1e-9

print(type(quaternions))


# figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update_plot(q, t):
    ax.cla()

    x_b, y_b, z_b = body_axes_from_quaternion(q)

    ax.quiver(0,0,0, *x_b, color='r', length=1)
    ax.quiver(0,0,0, *y_b, color='g', length=1)
    ax.quiver(0,0,0, *z_b, color='b', length=1)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_title(f"IMU Orientation | t = {t:.3f} s")

    plt.draw()
    # plt.pause(0.01)

print(type(quaternions))

# === Animación respetando tiempo real ===
t0 = timestamps_sec[0]

for i in range(len(quaternions)):
    update_plot(quaternions[i], timestamps_sec[i] - t0)

    if i > 0:
        dt = timestamps_sec[i] - timestamps_sec[i - 1]
        plt.pause(dt)