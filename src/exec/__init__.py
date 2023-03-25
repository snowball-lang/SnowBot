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
            mem_limit='1g',
            volumes={
                os.getcwd(): {'bind': '/code', 'mode': 'rw'}
            }
        )

        out = strip_ansi(container.logs().decode("utf-8"))

        return (out, "")
    except Exception as e:
        return ("", str(e))

def get_file(code: str):
    filename = f"./code/snowbot-{random.randint(100, 500)}-source.sn"
    with open(filename, "a") as f:
        f.write(code)
    return filename


def execute_code(code: str):
    f = get_file(code)
    command = "snowball run -f \"" + f + "\""
    os.remove(f)
    
    return execute_command(command)

