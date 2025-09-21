import math

def zyx_euler_to_quaternion(theta_z, phi_y, psi_x, degrees=True):
    """
    将ZYX欧拉角转换为四元数（w, x, y, z）
    
    参数:
        theta_z: 绕Z轴旋转角度（Yaw）
        phi_y: 绕Y轴旋转角度（Pitch）
        psi_x: 绕X轴旋转角度（Roll）
        degrees: 输入是否为角度制（True为角度，False为弧度）
    
    返回:
        tuple: 四元数 (w, x, y, z)
    """
    # 转换为弧度（如果输入是角度）
    if degrees:
        theta_z = math.radians(theta_z)
        phi_y = math.radians(phi_y)
        psi_x = math.radians(psi_x)
    
    # 计算半角
    half_theta = theta_z / 2.0
    half_phi = phi_y / 2.0
    half_psi = psi_x / 2.0
    
    # 计算三角函数值
    cos_t = math.cos(half_theta)
    sin_t = math.sin(half_theta)
    cos_p = math.cos(half_phi)
    sin_p = math.sin(half_phi)
    cos_r = math.cos(half_psi)
    sin_r = math.sin(half_psi)
    
    # 计算四元数各分量
    w = cos_t * cos_p * cos_r + sin_t * sin_p * sin_r
    x = cos_t * cos_p * sin_r - sin_t * sin_p * cos_r
    y = cos_t * sin_p * cos_r + sin_t * cos_p * sin_r
    z = sin_t * cos_p * cos_r - cos_t * sin_p * sin_r
    
    # 归一化（减少浮点误差影响）
    norm = math.sqrt(w**2 + x**2 + y**2 + z**2)
    return (x/norm, y/norm, z/norm, w/norm)

# 示例：ZYX欧拉角(90°, 0°, 0°)转换为四元数
if __name__ == "__main__":
    q = zyx_euler_to_quaternion(theta_z=0, phi_y=-50, psi_x=0)
    print(f"四元数 (w, x, y, z): {q}")
    # 输出应为 (0.7071, 0.0, 0.0, 0.7071) 左右（绕Z轴转90°的四元数）
