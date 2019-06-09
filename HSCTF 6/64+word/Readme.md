# 64+word

__Description__

Help Keith with his word search!!!! Where is the flag?

[64word.txt](64word.txt)

__Solution__

It's a word search game in base64 format.

First I conver 'hsctf{' to base 64

```
>>> base64.b64encode(b'hsctf{')
b'aHNjdGZ7'
```

Then I tried to look for 'aHNj' in the file.

It is located in the 32nd line in the file and is diagonal.

Write a simple [script](solve.py) to retrieve and decode it.

 ```
 hsctf{b4s3_64_w0rd_s3arch3s_ar3_fu9?}
 ```
