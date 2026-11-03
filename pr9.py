# simplify 45/ 60 using python

import math

def simplify(n, d):
	divisor = math.gcd(n, d)
	return (n // divisor, d // divisor)


print(simplify(45, 60))
