import os
import time


def cleanup_temp_files(directory, age_in_days):
    now = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.stat(file_path).st_mtime < now - age_in_days * 86400:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed {file_path}")


if __name__ == "__main__":
    temp_dir = input("Enter the temp dir: ")
    days_old = input("number of days old:")
    cleanup_temp_files(temp_dir, days_old)
