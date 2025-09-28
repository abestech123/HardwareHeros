python
import platform
import psutil
def detect_hardware():
    print("Hardware Detection Results:")
    print("---------------------------")
    print(f"CPU: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Threads: {psutil.cpu_count(logical=True)}")
    print(f"RAM: {psutil.virtual_memory().total / (1024.0 ** 3):.2f} GB")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"GPU: Not detected (add GPU detection code if needed)")
detect_hardware()
