import os
import random
import subprocess
import docker
from strip_ansi import strip_ansi

SNOWBALL = "/root/.snowball/bin/snowball"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../.."
BOT_ROOT = "/app"

def execute_command(command: str, executable: str, id: int):
    try:
        client = docker.from_env()

        container = client.containers.run(image = os.environ.get("DOCKER"),
                            detach = True,
                            tty = True,
                            volumes={f"{os.getcwd()}/code": {'bind': '/app/code', 'mode': 'rw'}},
                            privileged=True,
                            mem_limit="10g")
        cexit_code, clogs = container.exec_run(
            command,
        )

        clogs = strip_ansi(clogs.decode("utf-8", errors='ignore').replace("\\n", "\n").replace("\\t", "\t"))

        if cexit_code != 0:
            return (cexit_code, clogs)

        exit_code, logs = container.exec_run(
            executable,
        )

        logs = strip_ansi(logs.decode("utf-8", errors='ignore').replace("\\n", "\n").replace("\\t", "\t"))
        return (exit_code, logs)
    except Exception as e:
        return (1, str(e))

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
    executable = ' '.join(["./.sn/bin/file"])

    c = execute_command(command, executable, id)
    os.remove(main_file)

    return c
