## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>md5--</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Web</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>md5-- == md4.</br>
    	https://md5--.web.chal.hsctf.com
    </td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{php_type_juggling_is_fun}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td>Web<br>dwang</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

The original source code of the give website is given in the competition [./src.php](./src.php)

## Solution

after reading the source code, it is clear that our goal is to fulfill 

```
($_GET["md4"] == hash("md4", $_GET["md4"]))
```

Notice that `==` is used instead of `===`

> in php, `==` means equal after type juggling, while `===` means identical (in value and type)  
>for example:  
>var_dump("1" == "001"); *// 1 == 1 -> true*  
>var_dump("10" == "1e1"); *// 10 == 10 -> true*  

therefore the `==` here gives a way for me to abuse.

Goal : find a string **a** st. both **a** and **md4(a)** is `0e[0-9]+` 

write a script [./find.py](./find.py)* and itearate to find the desire string a.

```
[+] found! md4( 0e251288019 ) ---> 0e87495616364196127106940433240
```

visit **https://md5--.web.chal.hsctf.com/?md4=0e251288019**
and get the flag : hsctf{php_type_juggling_is_fun}


\* : The script was modified from the script written by bl4de


