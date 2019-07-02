import subprocess
proc = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
proc.stdin.write(b"Hello World!")
