from scipy.spatial.transform import Rotation as R

# 预期的ZYX欧拉角（角度制，顺序：Z, Y, X）
expected_euler_zyx = [0,-30, -90]

# 从欧拉角创建旋转对象
rot_expected = R.from_euler('zyx', expected_euler_zyx, degrees=True)

# 转换为四元数（格式：[x, y, z, w]）
expected_quat = rot_expected.as_quat()
print("预期欧拉角对应的四元数:", expected_quat)


from scipy.spatial.transform import Rotation as R

# 输入的四元数（格式：[x, y, z, w]）
input_quat = [-0.1830127, -0.1830127, -0.6830127, 0.6830127]

# 从四元数创建旋转对象
rot = R.from_quat(input_quat)

# 转换为ZYX顺序的欧拉角（角度制）
euler_zyx = rot.as_euler('zyx', degrees=True)
print("ZYX欧拉角（Z, Y, X）:", euler_zyx)