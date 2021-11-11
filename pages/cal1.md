title: LU Decomposition
date: 2021-10-30
category: Linear Algebra
    

[link to Head 1](#head)

<!--- first question -->
&#128037   \(\begin{flalign}
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
\text{are inverse to each other?}  &
\end{flalign}\)


<!--- first answer -->

$$
\because 
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
&#128037 

Why does \(L=E_{21}^{-1}*E_{31}^{-1}*E_{32}^{-1}\)
have advantage over \(L^{-1} = E_{32}*E_{31} *E_{21}\)? 

$$
\begin{alignat}{2}
 L^{-1} &= E_{32}*E_{31} *E_{21}  \\
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
&= 
  \begin{bmatrix}
  1 & 0 & 0   \\  
  0 & 1 & 0  \\ 
  0 & -l_{32} & 1  
  \end{bmatrix} * 
\begin{bmatrix}
  1 & 0 & 0  \\
  -l_{21} & 1 & 0  \\
  -l_{31} & 0 & 1 
  \end{bmatrix} &&\quad &&\text{Matrix multiplication mixed up all three numbers below.} \\
&=
  \begin{bmatrix}
  1 & 0 & 0   \\  
  -l_{21} & 1 & 0  \\ 
  \underline{-l_{31} + l_{21} * l_{32}} & -l_{32} & 1  
  \end{bmatrix} &&\quad &&\text{The entry at \(L^{-1}_{31}\) is an arithmetic combination of three elements} \\
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
  \end{bmatrix}   &&\quad &&\text{Each multiplier \(l_{ij}\) goes directly into its i, j position unchanged, which is what we like.}
\end{alignat}
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

``` python
from sympy import *
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
```

### head { #head}

## head 1 {#head-1}

### head 2 {#head-2}


##### head 3

\(y = x^2\)
When \(a \ne 0\), there are two solutions to $ax^2 + bx+c=0$ and they are $x = {-b \pm \sqrt{b^2 - 4ac} \over 2a}.$
Here's the \$.


LUdecomposition with Sympy

\begin{bmatrix}
1 & 2 & 3 \\
a & b & c
\end{bmatrix}  



