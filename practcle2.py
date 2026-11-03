import os
import datetime
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import math
import random

# passengers = 83
# capacity = 12

# buses = math.ceil(passengers / capacity)
# print("Number of buses needed:", buses)


seconds =5461


hours =seconds // 3600
minutes =(seconds % 3600) // 60
seconds = seconds % 60

print("total Hours :",hours)
print("total  minutes:",minutes)
print("total seconds :",seconds)  



def simplify(n, d):
	divisor = math.gcd(n, d)
	return (n // divisor, d // divisor)


print(simplify(45, 60))

dist = 80
angle = 45
height = dist * math.tan(math.radians(angle))
print(round(height, 2))

random.seed(5)
rolls = [random.randint(1, 6) for _ in range(5)]
print(rolls, sum(rolls))

deck = list(range(1, 9))
random.shuffle(deck)
print(deck)
print(random.choice(["rock", "paper", "scissors"]))