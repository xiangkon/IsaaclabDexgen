import h5py
import numpy as np
import cv2
import os
import argparse

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
        images = f["data/demo_0/obs/images_fpv"][:]
        
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

def main():
    parser = argparse.ArgumentParser(description='Convert HDF5 camera data to video')
    parser.add_argument('--hdf5_path', type=str, help='Input HDF5 file path')
    parser.add_argument('--output_video_path', type=str, help='Output video file path')
    parser.add_argument('--fps', type=float, default=30.0, help='Video frame rate (default: 30.0)')
    parser.add_argument('--frame_size', type=str, default='640x480', 
                        help='Frame size as "widthxheight" (default: 640x480)')
    
    args = parser.parse_args()
    
    # 解析帧尺寸
    width, height = map(int, args.frame_size.split('x'))
    frame_size = (width, height)
    
    # 检查输入文件是否存在
    if not os.path.exists(args.hdf5_path):
        raise FileNotFoundError(f"HDF5 file not found at: {args.hdf5_path}")
    
    # 转换并保存视频
    hdf5_to_video(
        hdf5_path=args.hdf5_path,
        output_video_path=args.output_video_path,
        fps=args.fps,
        frame_size=frame_size
    )

if __name__ == "__main__":
    main()