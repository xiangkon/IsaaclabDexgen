#!/usr/bin/env python3
# print_attr.py
import h5py, sys, pathlib

def dump_attrs(name, obj):
    """回调函数：递归打印所有 Group/Dataset 的属性"""
    if obj.attrs:
        print(f"\n>>> {name} 的属性:")
        for k, v in obj.attrs.items():
            print(f"   {k}  -->  {v}  (type: {type(v).__name__})")

file_path = sys.argv[1]
with h5py.File(file_path, 'r') as f:
    f.visititems(dump_attrs)