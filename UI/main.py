import sys
import ctypes
import os
import tkinter as tk
from tkinter import messagebox

# 1. 加载 C 动态库
if os.name == 'nt':  # Windows
    lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), '..', 'core', 'core.dll'))
else:  # Linux / macOS
    lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), '..', 'core', 'libcore.so'))

# 2. 声明函数签名
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

lib.get_version.restype = ctypes.c_char_p

def on_calc():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
    except ValueError:
        messagebox.showwarning("错误", "请输入整数")
        return

    # 调用 C 函数
    result = lib.add(a, b)
    result_label.config(text=f"结果: {result}")

if __name__ == "__main__":
    version = lib.get_version().decode('utf-8')
    
    root = tk.Tk()
    root.title("加法计算器(C内核+Python UI)")
    root.geometry("300x250")

    # 版本信息
    tk.Label(root, text=f"内核版本: {version}").pack(pady=5)

    # 输入框
    tk.Label(root, text="加数 1:").pack(pady=2)
    entry1 = tk.Entry(root)
    entry1.insert(0, "10")
    entry1.pack(pady=2)

    tk.Label(root, text="加数 2:").pack(pady=2)
    entry2 = tk.Entry(root)
    entry2.insert(0, "20")
    entry2.pack(pady=2)

    # 计算按钮
    btn = tk.Button(root, text="计算 A + B", command=on_calc)
    btn.pack(pady=10)

    # 结果显示
    result_label = tk.Label(root, text="")
    result_label.pack(pady=5)

    root.mainloop()