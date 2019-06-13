# Double Trouble

## Description

What is a koala anyway?

[koala.png](koala.png)    [koala2.png](koala2.png)

## Solution

Try zsteg on both file.
```
> zsteg koala.png                   
imagedata           .. text: "\n\n\n\n\n\n !"
b1,b,lsb,xy         .. text: "%q&),52+"
b1,bgr,lsb,xy       .. text: "<https://www.mediafire.com/file/0n67qsooy8hcy30/hmmm.txt/fileA"
b2,b,lsb,xy         .. text: "6Z?gdF$T"
b2,b,msb,xy         .. text: "{sXsE4}8"
b3,bgr,msb,xy       .. text: "\";Cc_$y)*I"
b4,b,msb,xy         .. text: "%BE##cgv"
```
```
> zsteg koala2.png
imagedata           .. text: "\n\n\n\n\n\n !"
b1,b,lsb,xy         .. text: "%q&),52+"
b1,bgr,lsb,xy       .. text: "passkey: whatdowehavehereJo"
b2,b,lsb,xy         .. text: "6Z?gdF$T"
b2,b,msb,xy         .. text: "{sXsE4}8"
b3,g,lsb,xy         .. text: "Wg8je^i<"
b4,b,msb,xy         .. text: "%BE##cgv"
```
Visiting the website, we can download a [file](hmmm.txt).

Check what file type is it.
```
> file hmmm.txt
hmmm.txt: GPG symmetrically encrypted data (AES cipher)
```
Use gpg decrypt this file with key "whatdowehavehere" (16 words).

```
hsctf{koalasarethecutestaren'tthey?}
```
