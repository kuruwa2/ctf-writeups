## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Logo Sucks Bad</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Forensic</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Written by: Tux</br>This logo sucks bad.
    </td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>logo.png</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

## Solution
By reading the problem name, we notice it's LSB in abbriv.
Hence, a reasonable guess would be Least Significant Bit (LSB) stegonagraphy.

Using stegsolve.jar tool to generate the [lsb file](./lsb), which is the least significant bits of RGB layers.

```
$ strings lsb | grep hsctf{
Donec id viverra augue. Vivamus nullhsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}a neque, iaculis quis urna eget, gravida commodo quam. Vestibulum porttitor justo in suscipit rutrum. Sed id tristique ipsum. Nulla vel porta nisl. Quisque leo quam, placerat id neque eu, ullamcorper facilisis lacus. Maecenas magna eros, sollicitudin id est a, fermentum elementum leo. Vestibulum porttitor urna eget bibendum interdum. Mauris eget consequat est. Aenean hendrerit eleifend finibus. Sed eu luctus nulla, non tristique nunc. Cras aliquet vehicula tincidunt. Maecenas nec semper ipsum.
```

and we could find the flag.