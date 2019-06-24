## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Chicken Crossing</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Forensic</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{2_get_2_the_other_side}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>hsctf-chicken_crossing.jpg</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

#### Message
Written by: Jeremy Hui
Keith is watching chickens cross a road in his grandfather’s farm. He once heard from his grandfather that there was something significant about this behavior, but he can’t figure out why. Help Keith discover what the chickens are doing from this seemingly simple behavior.


## Solution
A simple string search solves the problem.
```
$ strings hsctf-chicken_crossing.jpg | grep hsctf{
hsctf{2_get_2_the_other_side}
```
