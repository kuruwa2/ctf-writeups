# newcrypt
### Description
<img src="https://i.imgur.com/u7SChrz.png" width="100%">

### Solution

The script generated 4 numbers by:
```python=
for i in range(4):
    x = getPrime((1<<10)-random.randint(1<<0,1<<8))
    y = inverse(x,(self.p-1)*(self.q-1)//GCD(self.p-1,self.q-1))
    numbers.append(y)
```
The vulnerabililty here is that xs' bit length is small compared to n, so lattice-based attack could exploit it.

[Howgrave-Graham and Seifert’s Attack](https://eprint.iacr.org/2009/037.pdf) had concluded that when given 4 public exponents whose private components' bit length is below $\delta=0.441$ times the bit length of n, it's likely to factorize n efficiently.

![](https://i.imgur.com/BqOL6ey.png)

The bit length of x here is about $\frac{1024-128}{2048} = 0.4375$.

#### The math

<img src="https://latex.codecogs.com/gif.latex?e_id_i%3D1&plus;k_i%5Cfrac%7B%5Cphi%7D%7BG%7D">

By this relation of e and d, we can have 10 basic equations: ($G$ is GCD and $s=n-\phi$)

<img src="https://latex.codecogs.com/gif.latex?W_i%3A%20Ge_id_i-k_in%3DG-k_is'>
<img src="https://latex.codecogs.com/gif.latex?G_%7Bi%2Cj%7D%3A%20k_iGe_jd_j-k_jGe_id_i%3DG%28k_i-k_j%29'>

The basic idea is using these equations to construct a vector-matrix equation $xB=v$ where $B$ is an upper triangle matrix and

<img src="https://latex.codecogs.com/gif.latex?x%3D%28k_1k_2k_3k_4%2C%20d_1k_2k_3k_4%2C%20k_1d_2k_3k_4%2C%20d_1d_2k_3k_4%2C%20k_1k_2d_3k_4%2C%20...%2C%20d_1d_2d_3d_4%29">

For the purpose that will be mentioned later, we want to choose $G_{i,j}$ as many as possible and $W_i$ as less as possible.

My choice was:
<img src="https://latex.codecogs.com/gif.latex?k_1k_2k_3k_4%3Dk_1k_2k_3k_4%2C%20k_2k_3k_4W_1%2C%20k_3k_4G_%7B1%2C2%7D%2C%20k_3k_4W_1W_2%2C%5C%5C%20k_2k_4G_%7B1%2C3%7D%2C%20k_4W_1G_%7B2%2C3%7D%2C%20k_4W_2G_%7B1%2C3%7D%2C%20k_4W_1W_2W_3%2C%5C%5C%20k_2k_3G_%7B1%2C4%7D%2C%20k_3W_1G_%7B2%2C4%7D%2C%20G_%7B1%2C2%7DG_%7B3%2C4%7D%2C%20W_1W_2G_%7B3%2C4%7D%5C%5C%20G_%7B1%2C3%7DG_%7B2%2C4%7D%2C%20W_1W_3G_%7B2%2C4%7D%2C%20W_2W_3G_%7B1%2C4%7D%2C%20W_1W_2W_3W_4">

This lead to:

```
    B=[ [1,-n,0,n^2,0,0,0,-n^3,0,0,0,0,0,0,0,n^4],
        [0,e1,-e1,-e1*n,-e1,0,e1*n,e1*n^2,-e1,0,0,0,0,0,-e1*n^2,-e1*n^3],
        [0,0,e2,-e2*n,0,e2*n,0,e2*n^2,0,e2*n,0,0,0,-e2*n^2,0,-e2*n^3],
        [0,0,0,e1*e2,0,-e1*e2,-e1*e2,-e1*e2*n,0,-e1*e2,0,0,e1*e2,e1*e2*n,e1*e2*n,e1*e2*n^2],
        [0,0,0,0,e3,-e3*n,-e3*n,e3*n^2,0,0,0,-e3*n^2,0,0,0,-e3*n^3],
        [0,0,0,0,0,e1*e3,0,-e1*e3*n,0,0,e1*e3,e1*e3*n,0,0,e1*e3*n,e1*e3*n^2],
        [0,0,0,0,0,0,e2*e3,-e2*e3*n,0,0,-e2*e3,e2*e3*n,-e2*e3,e2*e3*n,0,e2*e3*n^2],
        [0,0,0,0,0,0,0,e1*e2*e3,0,0,0,-e1*e2*e3,0,-e1*e2*e3,-e1*e2*e3,-e1*e2*e3*n],
        [0,0,0,0,0,0,0,0,e4,-e4*n,0,e4*n^2,0,e4*n^2,e4*n^2,-e4*n^3],
        [0,0,0,0,0,0,0,0,0,e1*e4,-e1*e4,-e1*e4*n,-e1*e4,-e1*e4*n,0,e1*e4*n^2],
        [0,0,0,0,0,0,0,0,0,0,e2*e4,-e2*e4*n,0,0,-e2*e4*n,e2*e4*n^2],
        [0,0,0,0,0,0,0,0,0,0,0,e1*e2*e4,0,0,0,-e1*e2*e4*n],
        [0,0,0,0,0,0,0,0,0,0,0,0,e3*e4,-e3*e4*n,-e3*e4*n,e3*e4*n^2],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,e1*e3*e4,0,-e1*e3*e4*n],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,e2*e3*e4,-e2*e3*e4*n],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,e1*e2*e3*e4] ]
```

and 
<img src="https://latex.codecogs.com/gif.latex?v%3D%5Bk_1k_2k_3k_4%2C%5C%20%281-k_1s%29k_2k_3k_4%2C%5C%20%28k_1-k_2%29k_3k_4%2C%5C%20%281-k_1s%29%281-k_2s%29k_3k_4%2C%5C%5C%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%28k_1-k_3%29k_2k_4%2C%5C%20%281-k_1s%29%28k_2-k_3%29k_4%2C%5C%20%28k_1-k_3%29%281-k_2s%29k_4%2C%5C%20%5CPi_%7Bi%3D1%7D%5E3%281-k_is%29k_4%2C%5C%5C%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%28k_1-k_4%29k_2k_3%2C%5C%20%281-k_1s%29%28k_2-k_4%29k_3%2C%5C%20%28k_1-k_2%29%28k_3-k_4%29%2C%5C%20%281-k_1s%29%281-k_2s%29%28k_3-k_4%29%2C%5C%5C%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%5C%20%28k_1-k_3%29%28k_2-k_4%29%2C%5C%20%281-k_1s%29%281-k_3s%29%28k_2-k_4%29%2C%5C%20%281-k_2s%29%281-k_3s%29%28k_1-k_4%29%2C%5C%20%5CPi_%7Bi%3D1%7D%5E4%281-k_is%29%5D">

Every row of $B$ is a vector much bigger than $v$ and $v$ is linear combination of these rows.

To apply lattice attack, we still need that $v$ to be balanced. Notice that $e_i\approx n$, $d_i\approx n^\delta$, $k_i\approx n^\delta$, $s\approx n^{0.5}$, so $v$ is dominated by the last component $\Pi(1-k_is)\approx n^{2+4\delta}$.

Hence we need to multiply both $B$ and $v$ by a diagonal matrix $D$

```
diagonal_matrix([n^2,n^1.5,n^(2+delta),n,n^(2+delta),
                 n^(1.5+delta),n^(1.5+delta),n^0.5,
                 n^(2+delta),n^(1.5+delta),n^(2+2*delta),n^(1+delta),
                 n^(2+2*delta),n^(1+delta),n^(1+delta),1])
```

Now we can apply LLL algorithm to obtain $v$ and $x$, then calculate $\phi=e_1\times\frac{d_1k_2k_3k_4}{k_1k_2k_3k_4}$. If $\phi$ is calculated correctly, the roots of $x^2-(n+1-\phi)x+n=0$ will be p and q consequently.

The only thing left is that we don't know the GCD of $p-1$ and $q-1$, it could be any even number. Hence for every possible $G$, we need to multiply $e$ by $G$ first. It turned out that the GCD is just $2$ though.


#### Reason why not choose $W_i$ but $G_{i,j}$

![](https://i.imgur.com/o5qJ6Yl.png)

Using the theorem, to increase the success rate of the attack, we need the volume of $B$ to be as large as possible. It means large components of $D$, which means small right hand side of each equation we choose.

By some observation, all the right hand side of the equations consists of $k_1, k_2, k_3, k_4$.

When choosing $G_{i,j}$, we elimintae $k_i$ and $k_j$ but only multiply the number by $(k_i-k_j)$. On the other hand, choosing $W_i$ multiplies the number by $k_is$, which is much larger.

We can even calculate the upperbound of bit length of $d_i$ by the theorem.

<img src="https://latex.codecogs.com/gif.latex?%7C%7Cv%7C%7C%5Capprox%20n%5E%7B2&plus;4%5Cdelta%7D%5Cleq%20n%5E%7B%5Cfrac%7B1%7D%7B16%7D%2832&plus;13%5Cdelta&plus;22.5%29%7D%5Capprox%204%28e_1%5E8e_2%5E8e_3%5E8e_4%5E8n%5E%7B13%5Cdelta&plus;22.5%7D%29%5E%7B%5Cfrac%7B1%7D%7B16%7D%7D%3D%5Csqrt%7Bn%7Dvol%28B%29%5E%7B%5Cfrac%7B1%7D%7Bn%7D%7D%5C%5C%20%5CRightarrow%5Cdelta%5Cleq%5Cfrac%7B15%7D%7B34%7D%3D0.441...">


#### [The script](newcrypt.py)
