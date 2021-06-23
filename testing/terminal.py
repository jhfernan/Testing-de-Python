import os


terminal_size = os.get_terminal_size()

print(terminal_size)
os.system('resize -s 30 80')
