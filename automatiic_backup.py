import shutil
import os
from datetime import datetime


def backup_files(source, destination):
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = f"backup_{date}.tar.gz"
    backup_path = os.path.join(destination, backup_name)
    shutil.make_archive(backup_path.replace('.tar.gz', ''), 'gztar', source)
    print(f"Backup completed: {backup_path}")


if __name__ == "__main__":
    source_dir = input("Source directory: ")
    destination_dir = input("Destination directory: ")
    backup_files(source_dir, destination_dir)
