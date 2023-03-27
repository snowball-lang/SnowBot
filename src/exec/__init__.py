import os
import random
import subprocess
import docker
from strip_ansi import strip_ansi

SNOWBALL = "/root/.snowball/bin/snowball"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../.."
BOT_ROOT = "/app"

def execute_command(command: str, id: int):
    try:
        client = docker.from_env()

        container = box = client.containers.run(image = os.environ.get("DOCKER"),
                            detach = True,
                            tty = True,
                            volumes={f"{os.getcwd()}/code": {'bind': '/app/code', 'mode': 'rw'}},

                            command = "/bin/bash")
        exit_code, logs = container.exec_run(
            command,
        )

        print(logs)
        logs = strip_ansi(logs.decode("utf-8").replace("\\n", "\n").replace("\\t", "\t"))
        return (logs, exit_code)
    except Exception as e:
        return (str(e), 1)

def get_file(code: str, id: int):
    filename = f"code/snowbot-{id}-source.sn"
    root_file = f"{ROOT_DIR}//{filename}"
    bot_file = f"{BOT_ROOT}/{filename}"

    with open(root_file, "a+") as f:
        f.write(code)
    return bot_file, root_file

def execute_code(code: str):
    id = random.randint(100, 500)
    bot_file, main_file = get_file(code, id)

    command = ' '.join([SNOWBALL, "build", "-f", bot_file, "-s"])

    c = execute_command(command, id)
    os.remove(main_file)

    return c
