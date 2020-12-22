import subprocess
result = subprocess.run(['ls', '-a', '/'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
print(result.stderr)


