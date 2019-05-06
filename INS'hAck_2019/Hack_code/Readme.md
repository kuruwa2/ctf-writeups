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

最後找到了長為128的[tap](128.txt/)，給了我們三個flag。

```
First flag is INSA{N0t_bad_f0r_a_start}. The next flag will be awarded at <= 135.
```

```
INSA{135_is_pretty_g0Od_but_how_l0w_c4n_u_gO}. Get your next flag at <= 128
```

```
INSA{Getting_cl0ser}. The last flag is waiting for you at 126 !
```

但是到結束為止，我沒辦法在往下壓tap的數量，結束後才找到由OTA的__@luca__提出的[作法](refine.py/)。給了我們最後的[答案](sol126.txt/)
