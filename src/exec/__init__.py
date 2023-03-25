import os
import random
import subprocess
import docker
from strip_ansi import strip_ansi

SNOWBALL = "/root/.snowball/bin/snowball"

def execute_command(command: str, id: int):
    try:
        client = docker.from_env()

        container = client.containers.run(
            image=os.environ.get("DOCKER"),
            command=command,
            volumes={f"{os.getcwd()}/code": {'bind': '/app/code', 'mode': 'rw'}},
        )

        # Print the container output
        logs = container.decode('utf-8')

        return (logs, 0)
    except Exception as e:
        return (str(e), 1)

def get_file(code: str, id: int):
    filename = f"./code/snowbot-{id}-source.sn"
    with open(filename, "a+") as f:
        f.write(code)
    return filename

def execute_code(code: str):
    id = random.randint(100, 500)
    f = get_file(code, id)
    files = [f for f in os.listdir(".") if os.path.isfile(f)]

    print(files)
    command = ' '.join([SNOWBALL, "run", "-f", f])
    os.remove(f)

    return execute_command(command, id)

