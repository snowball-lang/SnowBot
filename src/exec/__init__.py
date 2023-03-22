import subprocess
import random

def execute_command(command: str):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return (output, error)

def get_file(code: str):
    with open(f"snowbot-{random.randint(100, 500)}-source.sn", "a") as f:
        f.write(code)
        return f


def execute_code(code: str):
    command = "snowball -F " + code
    output, error = execute_command(command)
