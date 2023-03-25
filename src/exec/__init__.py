import os
import random
import docker
from strip_ansi import strip_ansi

def execute_command(command: str):
    try:
        client = docker.from_env()
        container = client.containers.run(
            image=os.getenv('DOCKER'),
            command=command,
            detach=True,
            remove=True,
            cpu_shares=1024,
            mem_limit='1g'
        )

        out = strip_ansi(container.logs().decode("utf-8"))

        return (out, "")
    except Exception as e:
        return ("", str(e))

def get_file(code: str):
    filename = f"./snowbot-{random.randint(100, 500)}-source.sn"
    with open(filename, "a") as f:
        f.write(code)
    return filename


def execute_code(code: str):
    command = "snowball run -f \"" + get_file(code) + "\""
    return execute_command(command)

