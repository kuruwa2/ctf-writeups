## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Verbose</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>MISC</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Written by: dwang<br>
My friend sent me this file, but I don't understand what I can do with these 6 different characters...</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{esoteric_javascript_is_very_verbose}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>verbose.txt</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

## Solution

view source code, it is composed by six characters : `+`, `[`,`]`,`(`,`)` and `!`, which is likely to be `jsfuck`

use [jsfuck decoder](https://enkhee-osiris.github.io/Decoder-JSFuck/)

Result: 
```
var flag = "hsctf{esoteric_javascript_is_very_verbose}"; window.location = "https://hsctf.com";
```