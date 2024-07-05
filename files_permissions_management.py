import os


def set_permissions(path, mode):
    os.chmod(path, mode)
    print(f"Permissions set to {oct(mode)} for {path}")


if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    permissions_mode = input("Enter the permissions mode: ")
    set_permissions(file_path, permissions_mode)
