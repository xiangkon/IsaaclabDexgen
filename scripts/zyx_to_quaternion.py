from scipy.spatial.transform import Rotation as R
import numpy as np

# 定义ZYX欧拉角（单位：度，顺序为Yaw-Z, Pitch-Y, Roll-X）
yaw_z = -90  # 绕Z轴旋转90度
pitch_y = -30  # 绕Y轴旋转0度
roll_x = 0   # 绕X轴旋转0度

# 转换为弧度（scipy默认接受弧度，也可通过degrees=True指定角度）
euler_zyx = np.array([yaw_z, pitch_y, roll_x])

# 创建旋转对象（指定旋转顺序为'zyx'，即先Z、再Y、最后X）
rot = R.from_euler('zyx', euler_zyx, degrees=True)

# 转换为四元数（返回格式为 (x, y, z, w)）
quaternion = rot.as_quat()

print("四元数 (x, y, z, w):", quaternion)
# 输出（绕Z轴转90度的结果）：[0.         0.         0.70710678 0.70710678]