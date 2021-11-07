title: My Second Blog
date: 2020-02-23
category: calculus 
    

\\(y = x^2\\)
When \\(a \ne 0\\), there are two solutions to $ax^2 + bx+c=0$ and they are $x = {-b \pm \sqrt{b^2 - 4ac} \over 2a}.$
Here's the \$.


LUdecomposition with Sympy

\begin{bmatrix}
1 & 2 & 3 \\\\
a & b & c
\end{bmatrix}  

$$
\begin{align}
y &= x \* x  \\\\ 
  &= x^2
\end{align}
$$

\\(\because\\)
\\(\rhd\\)


\\[
\begin{equation}
e = mc^2   2
\end{equation}
\\]




$$
\begin{equation}
    e^{\pi i} + 1 = 0  3
\end{equation}
$$


\begin{alignat}{2}
 L^{-1} &= E_{32}\*E_{31} \*E_{21}  \\\\
  &= \begin{bmatrix}
  1 & 0 & 0   \\\\  
  0 & 1 & 0  \\\\ 
  0 & -l_{32} & 1  
  \end{bmatrix} \* 
\begin{bmatrix}
  1 & 0 & 0  \\\\
  0 & 1 & 0  \\\\
  -l_{31} & 0 & 1 
  \end{bmatrix}  \*
  \begin{bmatrix} 1 & 0 & 0 \\\\
  -l_{21} & 1 & 0 \\\\
  0 & 0 & 1
  \end{bmatrix}  & \\\\ 
&= 
  \begin{bmatrix}
  1 & 0 & 0   \\\\  
  0 & 1 & 0  \\\\ 
  0 & -l_{32} & 1  
  \end{bmatrix} \* 
\begin{bmatrix}
  1 & 0 & 0  \\\\
  -l_{21} & 1 & 0  \\\\
  -l_{31} & 0 & 1 
  \end{bmatrix}  & \\\\
&=
  \begin{bmatrix}
  1 & 0 & 0   \\\\  
  -l_{21} & 1 & 0  \\\\ 
  \underline{-l_{31} + l_{21} \* l_{32}} & -l_{32} & 1  
  \end{bmatrix}  & \qquad \qquad &\text{The entry at \\(L^{-1}_{31}\\) is an arithmetic combination of three elements}
\end{alignat} 

\begin{flalign}
L &= E_{21}^{-1} \*E_{31}^{-1} \*E_{32}^{-1} \\\\
  &= \begin{bmatrix}
  1 & 0 & 0   \\\\  
  l_{21} & 1 & 0  \\\\ 
  0 & 0 & 1  
  \end{bmatrix}  \* 
\begin{bmatrix}
  1 & 0 & 0  \\\\
  0 & 1 & 0  \\\\
  l_{31} & 0 & 1 
  \end{bmatrix}  \*
  \begin{bmatrix}
  1 & 0 & 0 \\\\
  0 & 1 & 0 \\\\
  0 & l_{32} & 1
  \end{bmatrix} & \\\\ 
&= 
  \begin{bmatrix}
  1 & 0 & 0   \\\\  
  l_{21} & 1 & 0  \\\\ 
  0 & 0 & 1  
  \end{bmatrix} \* 
\begin{bmatrix}
  1 & 0 & 0  \\\\
  0 & 1 & 0  \\\\
  l_{31} & l_{32} & 1 
  \end{bmatrix}  & \\\\
&=
  \begin{bmatrix}
  1 & 0 & 0   \\\\  
  l_{21} & 1 & 0  \\\\ 
  l_{31} & l_{32} & 1  
  \end{bmatrix} & \qquad \qquad \text{Each multiplier l_{ij} goes directly into its i, j position unchanged} 
\end{flalign}



$$
\rhd
$$

# LU Factorization  
Let's have a look at how \\(L * U\\) works, specifically \\(E_{21} * E_{31} * E_{32} * U\\).    
We are taking a 3 by 3 matrix for this demonstration.


Given $ A = \begin{bmatrix}
2 & 1 \\\\
6 & 8 \end{bmatrix}$



    from sympy.interactive.printing import init_printing
    init_printing(use_unicode=True)
    from sympy.matrices import Matrix 
    from sympy import symbols, shape, eye, sympify


    def LU2(A):
        L, U, P = A.LUdecomposition()
        r = U.rank()
        m, n = shape(U)
        D = eye(r)
        for i in range(r):
            pivot = U[i, i]
            D[i, i] = pivot
            for j in range(i, n):
                U[i, j] = U[i, j] / sympify(pivot)
        return L, D, U, P
        
Inline `code` has `back-ticks around` it.

```javascript  
function fancyAlert(arg) {   
  if(arg) {   
    $.facebox({div:'#foo'})    
  }   
}   
```




