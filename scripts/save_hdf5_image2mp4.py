import h5py
import numpy as np
import cv2
import os

def hdf5_to_video(hdf5_path, output_video_path, fps=30.0, frame_size=(640, 480)):
    """
    将 HDF5 文件中的摄像头图像数据转换为视频文件
    
    Args:
        hdf5_path (str): 输入 HDF5 文件路径
        output_video_path (str): 输出视频文件路径
        fps (float): 视频帧率
        frame_size (tuple): 帧尺寸 (width, height)
    """
    # 创建视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4编码
    out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)
    
    # 读取 HDF5 数据
    with h5py.File(hdf5_path, 'r') as f:
        # 获取摄像头数据 (shape: [steps, height, width, channels])
        images = f['obs/images_fpv'][:]
        
        print(f"Processing {images.shape[0]} frames...")
        
        # 转换为 0-255 的 uint8 格式 (RGB)
        images_uint8 = (images * 255).astype(np.uint8)
        
        # 转换为 BGR 格式 (OpenCV 使用)
        images_bgr = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in images_uint8]
        
        # 写入视频帧
        for i, frame in enumerate(images_bgr):
            out.write(frame)
            if i % 100 == 0:
                print(f"Processed frame {i}/{len(images_bgr)}")
    
    # 释放资源
    out.release()
    print(f"Video saved to: {output_video_path}")

# 使用示例
if __name__ == "__main__":
    # 配置路径 (根据您的实际路径修改)
    hdf5_path = "data/demo_0/obs/images_fpv.hdf5"  # 实际路径可能需要调整
    output_video_path = "output_video.mp4"
    
    # 检查文件是否存在
    if not os.path.exists(hdf5_path):
        raise FileNotFoundError(f"HDF5 file not found at: {hdf5_path}")
    
    # 转换并保存视频
    hdf5_to_video(
        hdf5_path=hdf5_path,
        output_video_path=output_video_path,
        fps=30.0,
        frame_size=(640, 480)  # 与摄像头分辨率匹配
    )