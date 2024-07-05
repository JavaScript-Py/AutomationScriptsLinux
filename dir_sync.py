import subprocess


def sync_directories(source, destination):
    command = ['rsync', '-av', source, destination]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    source_dir = input("source directory: ")
    destination_dir = input("destination directory: ")
    sync_directories(source_dir, destination_dir)
