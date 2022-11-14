import sys
sys.stdout.buffer.write(bytes("jjusko", 'utf-8'))
sys.stdout.buffer.write(b'\x00')
sys.stdout.buffer.write(bytes("aaaA+", 'utf-8'))