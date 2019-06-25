## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Locked Up</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Miscellaneous</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>My friend gave me a zip file with the flag in it, but the zip file is encrypted. Can you help me open the zip file?</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{w0w_z1ps_ar3nt_th@t_secUr3}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>locked.zip</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td>Miscellaneous<br>cppio</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td>Try opening it. What happens?</td>
  </tr>
</table>

## Solution
try to unzip the file without password.
```
   skipping: !lBo;!71}c'&!?m$NAtfBLH  incorrect password
   skipping: !l^-W~zN>?}i*{jRYG:=X=b:5Hdp7U  incorrect password
   skipping: !m9*t0r9Rf%V"           incorrect password
   skipping: !_bubre6A{|TB:Q`#X1Vu#Zm<V  incorrect password
    ...
```
dump the result into [zip_results](./zip_results.txt) for further analysis. However, a grep solves the problem

```
hsctf{w0w_z1ps_ar3nt_th@t_secUr3}
```