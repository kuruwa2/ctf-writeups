## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Networked Password</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Web</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Storing passwords on my own server seemed unsafe, so I stored it on a seperate one instead. However, the connection between them is very slow and I have no idea why.</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{sm0l_fl4g}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td>Web<br>cppio</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td>You know the flag format.</td>
  </tr>
</table>

## Solution
At first, I tried to insert 'h' and 'hsctf' into the filling blank.
We could feel a remarkable delay difference.

After some experiment (inserting 'h', 'hs', 'hsc', 'hsct', 'hsc.f', 'hsctf') we guess that the delay would be `0.2 + 0.5 * x`, where *x* is the length of the substring[0:the_first_mismatching_character_to_the_flag] of the inserted string.

Experimental insert result:

Inserted string| response delay(s)|
-----|-----|
a    | 0.2 |
h    | 0.7 |
hs   | 1.2 |
hsc  | 1.7 |
hsct | 2.2 |
hscta| 2.2 |
h...f| 0.7 |
hsctf| 2.7 |

Therefore, a [fuzzying script](./fuzzy.py) would solve the problem.

Remark: actually, the answer was manually fuzzed cause i was way too frustrated to the pwn problems.
