## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Slap</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Forensic</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Written by: Shray Vats, Jasper<br>
Don't get slapped too hard.
</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{twoslapsnonetforce}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>slap.jpg</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>




## Solution
A simple string search solves the problem.
```
$ strings slap.jpg |grep hsctf{

     <Iptc4xmpExt:CountryName>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut la bore et dolore magna aliqua. Massa id neque aliquam vestibulum morbi blandit cursu hsctf{twoslapsnonetforce} s risus. Sed viverra ipsum nunc aliquet bibendum. Nisl purus in mollis nunc sed. Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat. Magna eget est lorem ipsum dolor sit amet consectetur. Euismod in pellentesque massa placerat. Condimentum vitae sapien pellentesque habitant morbi. Cras sed felis eget velit aliquet sagittis id consectetur. Urna condimentum mattis pellentesque id nibh tortor. Odio aenean sed adipiscing diam donec adipiscing tristique risus nec. Faucibus nisl tincidunt eget nullam non nisi est sit amet. Enim nunc faucibus a pellentesque. Augue eget arcu dictum varius duis at consectetur. Morbi quis commodo odio aenean. Curabitur vitae nunc sed velit dignissim sodales ut. Id venenatis a condimentum vitae sapien pellentesque habitant. Erat nam at lectus urna duis.</Iptc4xmpExt:CountryName>
```

got the flag `hsctf{twoslapsnonetforce}`