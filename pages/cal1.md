title: LU Decomposition of matrices
date: 2021-10-30
category: la  # la stands for Linear Algebra
keywords: LUdecomposition, Sympy
    


--> [Discussions](#disc) * 2 

--> [Lab](#lab) * 2 

-------------

##### Discussions {:#disc}
&#128037   1)  

\begin{flalign}
& \text{ Why } L_{31}  = \left( \begin{smallmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
l_{31} & 0 & 1
\end{smallmatrix} \right) \,
\text{and} \, 
E_{31} = \left( \begin{smallmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-l_{31} & 0 & 1
\end{smallmatrix} \right) \,
\text{are inverse to each other?}   &
\end{flalign}

<!--- first answer -->
$$
\( \because \)
\begin{flalign}  
L_{31} * E_{31} &= 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
l_{31} & 0 & 1
\end{bmatrix} 
*
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-l_{31} & 0 & 1
\end{bmatrix}
= I  & \\
\\
\text{Or} \\
\\
L_{31} * E_{31} * A &= 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
l_{31} & 0 & 1
\end{bmatrix}
*
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-l_{31} & 0 & 1
\end{bmatrix}
*
\begin{bmatrix}
& \text{row 1}& \\
& \text{row 2}& \\
& \text{row 3}& 
\end{bmatrix}_{\text{Matrix A}} & \\
&=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
l_{31} & 0 & 1
\end{bmatrix}
*
\begin{bmatrix}
& \text{row 1} & \\
& \text{row 2}& \\
& \text{row 3 } - l_{31} * \text{row 1}& 
\end{bmatrix}  \\
&=
\begin{bmatrix}
& \text{row 1}& \\
& \text{row 2}& \\
& \text{row 3}& 
\end{bmatrix}_{\text{Matrix A}} = A \\
\end{flalign}
$$


<!--- second question -->
&#128037  2) 

Why does \($L=E_{21}^{-1}*E_{31}^{-1}*E_{32}^{-1}$\)
have advantage over $\(L^{-1} = E_{32}*E_{31} *E_{21}\)$? 


$$
\( \because \)
\begin{flalign}
  L^{-1} &= E_{32}*E_{31} *E_{21} &&  \\
  &= \begin{bmatrix}
  1 & 0 & 0   \\  
  0 & 1 & 0  \\
  0 & -l_{32} & 1  
  \end{bmatrix} * 
\begin{bmatrix}
  1 & 0 & 0  \\
  0 & 1 & 0  \\
  -l_{31} & 0 & 1 
  \end{bmatrix}  *
  \begin{bmatrix} 1 & 0 & 0 \\
  -l_{21} & 1 & 0 \\
  0 & 0 & 1
  \end{bmatrix}  & \\ 
\phantom{L_{31} * E_{31} * A } &= 
  \begin{bmatrix}
  1 & 0 & 0   \\  
  0 & 1 & 0  \\ 
  0 & -l_{32} & 1  
  \end{bmatrix} * 
\begin{bmatrix}
  1 & 0 & 0  \\
  -l_{21} & 1 & 0  \\
  -l_{31} & 0 & 1 
  \end{bmatrix} &&\text{Matrix multiplication mixed up all three numbers below.} \\
&=
  \begin{bmatrix}
  1 & 0 & 0   \\  
  -l_{21} & 1 & 0  \\ 
  \underline{-l_{31} + l_{21} * l_{32}} & -l_{32} & 1  
  \end{bmatrix} &&\text{The entry at \(L^{-1}_{31}\) is an algebraic combination of three elements} \\
 \\ 
 \\
L &= E_{21}^{-1} * E_{31}^{-1} *E_{32}^{-1} \\
  &= \begin{bmatrix}
  1 & 0 & 0   \\  
  l_{21} & 1 & 0  \\ 
  0 & 0 & 1  
  \end{bmatrix}  * 
\begin{bmatrix}
  1 & 0 & 0  \\
  0 & 1 & 0  \\
  l_{31} & 0 & 1 
  \end{bmatrix}  *
  \begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & l_{32} & 1
  \end{bmatrix}  \\ 
&= 
  \begin{bmatrix}
  1 & 0 & 0   \\  
  l_{21} & 1 & 0  \\ 
  0 & 0 & 1  
  \end{bmatrix} * 
\begin{bmatrix}
  1 & 0 & 0  \\
  0 & 1 & 0  \\
  l_{31} & l_{32} & 1 
  \end{bmatrix}   \\
&=
  \begin{bmatrix}
  1 & 0 & 0   \\  
  l_{21} & 1 & 0  \\ 
  l_{31} & l_{32} & 1  
  \end{bmatrix}   &&\text{Each multiplier \(l_{ij}\) goes directly into its i, j position unchanged, which is what we like.} && \phantom{a^2}
\end{flalign}
$$

--------------------
### Labs {:#lab}
1) &#128037  Modify Sympy's LUdecomposition method so that it returns L, D, U instead of just L and U.

According to [Sympy](https://docs.sympy.org/latest/index.html)'s document, [LUdecomposition](https://docs.sympy.org/latest/modules/matrices/matrices.html#matrix-functions-reference) could factor out a given matrix.

Example: 

``` python
>>> from sympy.interactive.printing import init_printing  # line 1~4 set up the environment for computing
>>> init_printing(use_unicode=True)
>>> from sympy.matrices import Matrix 
>>> from sympy import symbols, shape, eye, sympify, Rational
>>> A =  Matrix([[4, 3], [6, 3]])
>>> A.LUdecomposition()

```
![LUdecomposition](static/lu1.png)

```python
>>> L, U, _ = A.LUdecomposition()
>>> L * U == A
True
```

The leftmost matrix is L, the middle matrix is U, and the rightmost one is P. That P is blank just means that there's no row exchanges during the LU decomposition.

The motivation of this modification is that we want to see the symmetric matrix $\(S= L*D*U = L*D*L^T\)$ more clearly.

``` python
def LU2(A):
    L, U, P = A.LUdecomposition()
    r = U.rank()
    m, n = shape(U)
    D = eye(r)
    for i in range(r):
        pivot = U[i, i]
        D[i, i] = pivot
        for j in range(i, n):
            U[i, j] = U[i, j] / sympify(pivot)    # sympify makes the quotient of the two integers an exact rational number
    return L, D, U, P
```
Here's the result of LUdecomposition:
``` python
>>> B = Matrix([[1, 0, 3], [-2, 3, 5], [Rational(1, 3), 0, -3]])
>>> S = B.T*B    # this step makes a symmetric matrix S; another trick is B*B.T
>>> S.LUdecomposition() 
```
![LU2](static/lu2.png)

Here's the result of LU2's output:
``` python
>>> LU2(S)
```
![lu3](static/lu3.png)

In this particular case (check symmetric matrices' $\(L*D*L^T \)$ decomposition), we could see clearly that D (the rightmost matrix) is the transpose of L (the leftmost matrix).


2) &#128037 LUdecompose rectangular shaped matrices A 

Sympy's LUdecomposition is a really sharp tool that it deals with both square and rectangular matrices. While we may not find decomposing rectangular matrics productive, let's just play for fun. 

For this practice, I picked one 2 by 3 matrix A and one 3 by 2 matrix B. I am going to use both Sympy's LUdecomposition and our lightly modified LU2 method to see the matrix decomposition again.

![rectangular matrices](static/lu4.png)

![rect matrics2](static/lu5.png)

One takeaway I got from this experiment is that A and D seem to share the same shape and rank, while L is always square and full rank.

This is the end of this article, and I hope you like it.


