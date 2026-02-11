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
data = np.loadtxt("SensorConnectData5.csv", delimiter=",", skiprows=1)

timestamps = data[:, 0]          # unix ns
quaternions = data[:, 1:5]       # q0 qx qy qz

timestamps_sec = timestamps * 1e-9

print(type(quaternions))


# figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


def update_plot(q):
    ax.cla()

    x_b, y_b, z_b = body_axes_from_quaternion(q)

    ax.quiver(0,0,0, *x_b, color='r', length=1)
    ax.quiver(0,0,0, *y_b, color='g', length=1)
    ax.quiver(0,0,0, *z_b, color='b', length=1)

    # ax.set_xlim([-1, 1])
    # ax.set_ylim([-1, 1])
    # ax.set_zlim([-1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # ax.set_title(f"IMU Orientation | t = {t:.3f} s")

    plt.draw()
    plt.pause(0.01)

# quaternions = [
#     [1,0,0,0],
#     [0.993060, 0.010836, 0.001493, -0.117095],
#     [0.982994, 0.010856, 0.002036, -0.183305],
#     [0.964492, 0.010436, 0.002814, -0.263893],
#     [0.916572,-0.002301,0.003421,-0.399849,1],
#     [0.851283,-0.002912,0.002794,-0.524692],
#     [0.798445,-0.003463,0.002572,-0.602053],
#     [0.737033,-0.003908,0.002162,-0.675843],
#     [0.704061,-0.004142,0.001935,-0.710125],
#     [0.659807,-0.004340,0.001626,-0.751421],
#     [0.612778,-0.003175,-0.002206,-0.790246],
#     [0.586724,-0.004406,0.000784,-0.809775],
#     [0.570587,-0.004739,0.001396,-0.821222],
#     [0.539137,-0.004788,0.001188,-0.842204],
#     [0.517488,-0.004763,0.000967,-0.855676],
#     [0.485186,-0.004872,0.001084,-0.874397],
#     [0.471890,-0.004870,0.001307,-0.881643],
#     [0.461861,-0.004952,0.001592,-0.886937],
#     [0.456075,-0.004859,0.001514,-0.889927],
# ]
print(type(quaternions))

for q in quaternions:
    update_plot(q)

# q = leer_cuaternion()
# update_plot(q)

# === Animación respetando tiempo real ===
# t0 = timestamps[0]

# for i in range(len(quaternions)):
#     update_plot(quaternions[i], timestamps[i] - t0)

#     if i > 0:
#         dt = timestamps[i] - timestamps[i - 1]
#         plt.pause(dt)