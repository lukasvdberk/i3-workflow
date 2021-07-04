import shlex
import subprocess


def execute_os_command(command: str):
    subprocess.check_call(shlex.split(command), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)