from shellcode import shellcode
import sys
sys.stdout.buffer.write(bytes("/bin/sh", "utf-8"))
print(len(bytes("/bin/sh", "utf-8")))
sys.stdout.buffer.write(b'\x00')
