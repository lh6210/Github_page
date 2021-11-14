We are taking a 3 by 3 matrix for this demonstration.


Given $ A = \begin{bmatrix}
2 & 1 \\\\
6 & 8 \end{bmatrix}$


``` python
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

`#!math p(x|y) = \frac{p(y|x)p(x)}{p(y)}`

LUdecomposition with Sympy

\begin{bmatrix}
1 & 2 & 3 \\
a & b & c
\end{bmatrix}  



