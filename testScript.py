import time
import sympy
from sympy.abc import x, y
def f(x, n):
    S = 1
    for i in range(1, n+1):
        S *= (1 + y * x**i)
    return S
M   = f(x, 10)
M1  = M.expand()
M2  = M1.as_ordered_terms()
print M2
outputString = "\n======================================================\n" + time.asctime() + "\n" +  str(M2)
open('testScript_outputFile.txt', 'a').write(outputString)
