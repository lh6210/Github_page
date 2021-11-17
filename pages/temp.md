title: title 2
date:  2021-10-03
category: la 
keywords: sympy


## head 3

### this is the second line

\begin{flalign}
& \text{Why } L_{31}  = \left( \begin{smallmatrix}
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
\end{flalign}


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


Why is \($L = \left( \begin{smallmatrix}
1 & 0 \\
0 & 1
\end{smallmatrix} \right)$\) better than $\(y = x^2\)$ ?








