import subprocess


def add_user(username):
    command = ['sudo', 'adduser', username]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)


def delete_user(username):
    command = ['sudo', 'deluser', username]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    n = input("To add an user 1, delete a user 2, then press enter")
    username = input("Enter username: ")
    match n:
        case '1':
            add_user(username)
            print("User added successfully")
        case '2':
            delete_user(username)
            print("User deleted")
