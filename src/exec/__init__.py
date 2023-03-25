import os
import subprocess
import random
import docker

def execute_command(command: str):
    client = docker.from_env()
    container = client.containers.run(
        image=os.getenv('DOCKER'),
        command=command,
        detach=True,
        remove=True,
        cpu_shares=1024,
        mem_limit='1g'
    )
    
    return (container.logs().decode("utf-8"), "")

def get_file(code: str):
    filename = f"./snowbot-{random.randint(100, 500)}-source.sn"
    with open(filename, "a") as f:
        f.write(code)
    return filename


def execute_code(code: str):
    command = "snowball run -f \"" + get_file(code) + "\""
    return execute_command(command)

