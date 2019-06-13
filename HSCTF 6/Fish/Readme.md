# Fish

## Description

I got a weird image from some fish. What is this?

[fish.jpg](fish.jpg)

## Solution

Running ```strings``` command on [fish.jpg](fish.jpg) gives us the text ```bobross63```.

Try

```
> steghide extract -sf fish.jpg
Enter passphrase: bobross63
the file "flag.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "flag.txt".
> cat flag.txt
hsctf{fishy_fishy_fishy_fishy_fishy_fishy_fishy123123123123}
```

The flag is
```
hsctf{fishy_fishy_fishy_fishy_fishy_fishy_fishy123123123123}
```
