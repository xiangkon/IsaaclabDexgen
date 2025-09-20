#!/usr/bin/env python3
import h5py
import sys
import json

def modify_env_name(file_path):
    # 以读写模式打开HDF5文件
    with h5py.File(file_path, 'r+') as f:
        # 检查data组是否存在
        if 'data' not in f:
            print("错误：文件中不存在'data'组")
            return
        
        data_group = f['data']
        
        # 检查env_args属性是否存在
        if 'env_args' not in data_group.attrs:
            print("错误：'data'组中不存在'env_args'属性")
            return
        
        try:
            # 读取属性值并解析为字典
            env_args_str = data_group.attrs['env_args']
            env_args = json.loads(env_args_str)
            
            # 打印原始值
            print(f"原始env_name: {env_args['env_name']}")
            
            # 修改env_name
            env_args['env_name'] = "Isaac-PickPlace-GR1T2-Abs-Mimic-WithCamera-v0"
            
            # 转换回字符串并写回属性
            data_group.attrs['env_args'] = json.dumps(env_args)
            
            # 验证修改结果
            updated_args_str = data_group.attrs['env_args']
            updated_args = json.loads(updated_args_str)
            print(f"修改后env_name: {updated_args['env_name']}")
            print("属性修改成功")
            
        except json.JSONDecodeError:
            print("错误：无法解析'env_args'属性值为JSON格式")
        except KeyError as e:
            print(f"错误：属性中不存在{str(e)}键")
        except Exception as e:
            print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python modify_hdf5_attr.py <hdf5文件路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    modify_env_name(file_path)
