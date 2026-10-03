import sys
import subprocess

def launcher(game_script):
    subprocess.Popen([sys.executable, "-m", "pgzrun", game_script])