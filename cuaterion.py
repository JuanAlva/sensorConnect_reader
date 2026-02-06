import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

def plot_quaternion_rotation(q_wxyz):
    """
    Visualizes a quaternion rotation by plotting original and rotated axes.

    Args:
        q_wxyz (list/array): The quaternion in [w, x, y, z] (scalar-first) format.
    """
    # Scipy uses scalar-last [x, y, z, w] format, so we reorder
    q_xyzw = [q_wxyz[1], q_wxyz[2], q_wxyz[3], q_wxyz[0]]
    
    # Define the rotation from the quaternion
    rotation = R.from_quat(q_xyzw)

    # Define original unit vectors (the basis vectors)
    i_hat = np.array([1, 0, 0])
    j_hat = np.array([0, 1, 0])
    k_hat = np.array([0, 0, 1])

    # Rotate the unit vectors
    i_hat_rot = rotation.apply(i_hat)
    j_hat_rot = rotation.apply(j_hat)
    k_hat_rot = rotation.apply(k_hat)

    # Set up the 3D plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(f'Quaternion Rotation Visualization (q={np.round(q_wxyz, 2)})')

    # Plot original axes (blue)
    ax.quiver(0, 0, 0, i_hat[0], i_hat[1], i_hat[2], color='b', label='Original X')
    ax.quiver(0, 0, 0, j_hat[0], j_hat[1], j_hat[2], color='b', label='Original Y')
    ax.quiver(0, 0, 0, k_hat[0], k_hat[1], k_hat[2], color='b', label='Original Z')

    # Plot rotated axes (red)
    ax.quiver(0, 0, 0, i_hat_rot[0], i_hat_rot[1], i_hat_rot[2], color='r', linestyle='--', label='Rotated X')
    ax.quiver(0, 0, 0, j_hat_rot[0], j_hat_rot[1], j_hat_rot[2], color='r', linestyle='--', label='Rotated Y')
    ax.quiver(0, 0, 0, k_hat_rot[0], k_hat_rot[1], k_hat_rot[2], color='r', linestyle='--', label='Rotated Z')

    # Set plot limits
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.legend()
    plt.show()

# Example usage:
# A quaternion representing a 90-degree rotation around the Z axis (w, x, y, z)
# For this rotation, w = cos(angle/2), z = sin(angle/2)
angle = np.pi / 2  # 90 degrees in radians
q_example = np.array([np.cos(angle/2), 0, 0, np.sin(angle/2)]) 

plot_quaternion_rotation(q_example)
