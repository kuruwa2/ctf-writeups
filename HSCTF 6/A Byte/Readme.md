# A byte

## Description

Just one byte makes all the difference.

[a-byte](a-byte)

## Solution

Looking the assembly code by r2. In the main function, the input message is check whether the strlen is 0x23=35.

```
0x0000078e      e85dfeffff     call sym.imp.strlen         ; size_t strlen(const char *s)
0x00000793      8945c4         mov dword [local_3ch], eax
0x00000796      837dc423       cmp dword [local_3ch], 0x23 ; '#'
```
