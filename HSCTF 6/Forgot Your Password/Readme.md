# Forgot Your Password

## Description

Help! I got this new lock for Christmas, but I've forgotten the first two values. I know the last value is hsctfissocoolwow.

I also managed to grab a copy of their secret key generator. Can you help me out?

Note: submit the first two combo values separated by a space in hex format.

[generator.py](generator.py)

## Solution

This generator takes two secret numbers and do several complicated operation, next().
```
def o(x,k):
	return x<<k
def m(a):
	return a&0xffffffffffffffff
def next():
	b = m(s[0]+s[1])
	h()
	return m(b)
def p(k, x):
	return x>>(64-k)
def x(b, a):
	return a^b
def oro(a, b):
	return a|b
def h():
	s1 = m(x(s[0],s[1]))
	s[0] = m(x(oro(o(s[0],55),p(55,s[0])),x(s1,(o(s1,14)))))
	s[1] = m(oro(o(s1,36),p(36,s1)))
```

In the last step, its output should be the hex encode of 'wowlooco' and the second last step's should be 'ssiftcsh', so the isp(bin2chr(next()))+isp(bin2chr(next())) would output 'hsctfissocoolwow'.

```
def bin2chr(data):
    result = ''
    while data:
        char = data & 0xff
        result += chr(char)
        data >>= 8
    return result

def isp(d):
	if all(c in ch for c in d):
		return d
	else:
		return d.encode('hex')
```

It is a SAT problem and is a perfect job for z3.

Lets claim two variable s[0] and s[1] as 65 bits vector.

```
s = [BitVec('s0',65),BitVec('s1',65)]
```
Like the [generator](generator.py), we do next() four times (the first two are not necessary).

And the next two next's outputs should be
```
>>> 'ssiftcsh'.encode('hex')
'7373696674637368'
>>> 'wowlooco'.encode('hex')
'776f776c6f6f636f'
```
Putting them together, the [script](reverse.py) gave me the secret number:

```
sat
[s1 = 15319349121703965325, s0 = 1975711866010926419]
```
Throwing them back to [generator](generator.py), the output is:
```
Thanks! Your numbers are: 
e06f76cd556604f0f21c34f1519d2fd2
73c8535ab0f954b5ad1cbab7abc18309
hsctfissocoolwow
```
So the flag is
```
e06f76cd556604f0f21c34f1519d2fd2 73c8535ab0f954b5ad1cbab7abc18309
```
