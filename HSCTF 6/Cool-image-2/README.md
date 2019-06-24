## Problem information
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Cool Image 2</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Forensics</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>My friend sent me this image, but I can't open it. Can you help me open the image?</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{sorry_about_the_extra_bytes}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>cool.png</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td>Forensics<br>cppio</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td>Try looking at the raw contents of the file.</td>
  </tr>
</table>

## Solution
Let's see the raw contents of the file.

```
$ hexdump cool.png -C -n 500
00000000  49 20 66 6f 75 6e 64 20  74 68 69 73 20 63 6f 6f  |I found this coo|
00000010  6c 20 66 69 6c 65 2e 20  49 74 73 20 72 65 61 6c  |l file. Its real|
00000020  6c 79 20 63 6f 6f 6c 21  0a 89 50 4e 47 0d 0a 1a  |ly cool!..PNG...|
00000030  0a 00 00 00 0d 49 48 44  52 00 00 04 b6 00 00 00  |.....IHDR.......|
00000040  59 08 06 00 00 00 23 3b  ad d1 00 00 00 04 67 41  |Y.....#;......gA|
00000050  4d 41 00 00 b1 8f 0b fc  61 05 00 00 00 06 62 4b  |MA......a.....bK|
00000060  47 44 00 ff 00 ff 00 ff  a0 bd a7 93 00 00 00 09  |GD..............|
00000070  70 48 59 73 00 00 0b 13  00 00 0b 13 01 00 9a 9c  |pHYs............|
00000080  18 00 00 00 07 74 49 4d  45 07 e3 05 1f 0f 0b 16  |.....tIME.......|
00000090  80 e2 20 92 00 00 20 00  49 44 41 54 78 da ec 5d  |.. ... .IDATx..]|
000000a0  65 78 14 57 17 7e ef cc  4a 36 1b 37 02 09 09 2e  |ex.W.~..J6.7....|
000000b0  45 8b 57 28 2e 6d 69 a9  01 a5 94 16 aa 54 68 29  |E.W(.mi......Th)|
...
```

usually png files shall start with `89 50 4E 47`, so let's remove the bytes before them. Let's `vim` the file to get some look:

```
$vim files/cool.png
I found this cool file. Its really cool!
<89>PNG^M
^Z
^@^@^@^MIHDR^@^@^D¶ ^@^@^@Y^H^F^@^@^@#;­ Ñ^@^@^@^DgAMA
...
```

So this one is easy to deal with cause extra characters are in a single line. `dd` in the vim file and `:wq`.

and we could see the flag.

![](./flag.png)