import subprocess
import random

def execute_command(command: str):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(error)
    return (output, error)

def get_file(code: str):
    filename = f"./snowbot-{random.randint(100, 500)}-source.sn"
    with open(filename, "a") as f:
        f.write(code)
    return filename


def execute_code(code: str):
    command = "snowball run -f \"" + get_file(code) + "\""
    return execute_command(command)

