import shlex
import subprocess


def execute_os_command(command: str):
    subprocess.Popen(shlex.split(command), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)