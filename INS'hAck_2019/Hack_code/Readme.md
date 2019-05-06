# HackCode

__Description__

We have a little budgeting issue with our latest red team campaign. Please help us figure it out :

https://hack-code.ctf.insecurity-insa.fr

This challenge has 4 different flags, better solutions will grant you more flags.


__SOLUTION__

題目網址給了包含10000筆route路徑的[檔案](route.txt/)，題目要求找到150個以下的router使得每行都至少有一個tap。

我寫了一個[__Greedy__](route2.py/)來找這些tap，演算法如下:

1. 對所有routes，找到存在於最多行的router，加入tap
2. 去掉這些有這個router的routes
3. 重複1.、2.直到routes為空
