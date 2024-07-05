import os
import platform


def system_info():
    print("Kernel version:")
    print(platform.release())
    print("\nDisk space:")
    os.system("df -h")
    print("\nMemory use:")
    os.system("free -m")


if __name__ == "__main__":
    system_info()
