import subprocess


def manage_service(service_name, action):
    command = ['sudo', 'systemctl', action, service_name]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    service = input("Enter service name: ")
    action = input("Enter action: ")
    manage_service(service, action)
