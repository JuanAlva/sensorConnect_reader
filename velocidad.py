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

interp_quaternion()

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

