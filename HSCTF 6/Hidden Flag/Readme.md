# Hidden Flag

__Description__

This image seems wrong.....did Keith lose the key __again__?

[chall.png](chall.png)

__Solution__

An error occured when opening the file.

The hexdump of the file give me an interesting line in the last line.

![alt text](hexdump.png)

However, I don't have any idea where to use the key.

After trying a lot of different way to analyse the file, the [xortool](https://github.com/hellman/xortool) catch my eye.

![alt text](xortool.png)

The first key it use is literally invisible, and the first [file](xor.png) of the output give us the flag

![alt text](xor.png)

```
hsctf{n0t_1nv1s1bl3_an5m0r3?_39547632}
```
