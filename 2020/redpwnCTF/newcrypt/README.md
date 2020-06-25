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

<img src="https://latex.codecogs.com/gif.latex?e_id_i%3D1&plus;k_i%5Cfrac%7B%5Cphi%7D%7BG%7D")>

By this relation of e and d, we can have 10 basic equations: ($G$ is GCD and $s=n-\phi$)

$W_i: Ge_id_i-k_in=G-k_is$
$G_{i,j}: k_iGe_jd_j-k_jGe_id_i=G(k_i-k_j)$

The basic idea is using these equations to construct a vector-matrix equation $xB=v$ where $B$ is an upper triangle matrix and

$x=(k_1k_2k_3k_4, d_1k_2k_3k_4, k_1d_2k_3k_4, d_1d_2k_3k_4, k_1k_2d_3k_4, ..., d_1d_2d_3d_4)$

For the purpose that will be mentioned later, we want to choose $G_{i,j}$ as many as possible and $W_i$ as less as possible.

My choice was:
$k_1k_2k_3k_4=k_1k_2k_3k_4, k_2k_3k_4W_1, k_3k_4G_{1,2}, k_3k_4W_1W_2,\\
k_2k_4G_{1,3}, k_4W_1G_{2,3}, k_4W_2G_{1,3}, k_4W_1W_2W_3,\\
k_2k_3G_{1,4}, k_3W_1G_{2,4}, G_{1,2}G_{3,4}, W_1W_2G_{3,4}\\
G_{1,3}G_{2,4}, W_1W_3G_{2,4}, W_2W_3G_{1,4}, W_1W_2W_3W_4$

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
$v=[k_1k_2k_3k_4,\ (1-k_1s)k_2k_3k_4,\ (k_1-k_2)k_3k_4,\ (1-k_1s)(1-k_2s)k_3k_4,\\\ \ \ \ \ \ \ \ (k_1-k_3)k_2k_4,\ (1-k_1s)(k_2-k_3)k_4,\ (k_1-k_3)(1-k_2s)k_4,\ \Pi_{i=1}^3(1-k_is)k_4,\\\ \ \ \ \ \ \ \ (k_1-k_4)k_2k_3,\ (1-k_1s)(k_2-k_4)k_3,\ (k_1-k_2)(k_3-k_4),\ (1-k_1s)(1-k_2s)(k_3-k_4),\\\ \ \ \ \ \ \ \ (k_1-k_3)(k_2-k_4),\ (1-k_1s)(1-k_3s)(k_2-k_4),\ (1-k_2s)(1-k_3s)(k_1-k_4),\ \Pi_{i=1}^4(1-k_is)]$

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

$$
||v||\approx n^{2+4\delta}\leq n^{\frac{1}{16}(32+13\delta+22.5)}\approx 4(e_1^8e_2^8e_3^8e_4^8n^{13\delta+22.5})^{\frac{1}{16}}=\sqrt{n}vol(B)^{\frac{1}{n}}\\
\Rightarrow\delta\leq\frac{15}{34}=0.441...
$$


#### [The script](newcrypt.py)
