# calc_lib.py

import math
import statistics
import numpy as np

class CalcLib:

    # -------------------------------
    # 🔢 Basic Arithmetic
    # -------------------------------
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    def modulus(self, a, b): return a % b
    def power(self, a, b): return a ** b
    def nth_root(self, a, n): return a ** (1/n)

    # -------------------------------
    # 🧮 Number Utilities
    # -------------------------------
    def factorial(self, n): return math.factorial(n)
    def gcd(self, a, b): return math.gcd(a, b)
    
    def lcm(self, a, b):
        return abs(a*b) // math.gcd(a, b) if a and b else 0
    
    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def fibonacci(self, n):
        seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq[:n]

    # -------------------------------
    # 📐 Trigonometry
    # -------------------------------
    def sin(self, x): return math.sin(x)
    def cos(self, x): return math.cos(x)
    def tan(self, x): return math.tan(x)
    def asin(self, x): return math.asin(x)
    def acos(self, x): return math.acos(x)
    def atan(self, x): return math.atan(x)
    
    def deg_to_rad(self, deg): return math.radians(deg)
    def rad_to_deg(self, rad): return math.degrees(rad)

    # -------------------------------
    # 📊 Statistics
    # -------------------------------
    def mean(self, data): return statistics.mean(data)
    def median(self, data): return statistics.median(data)
    def mode(self, data): return statistics.mode(data)
    def stdev(self, data): return statistics.stdev(data)
    def variance(self, data): return statistics.variance(data)

    # -------------------------------
    # 🔢 Algebra / Calculus
    # -------------------------------
    def quadratic_roots(self, a, b, c):
        d = b**2 - 4*a*c
        if d < 0:
            return "Complex Roots"
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return (r1, r2)
    
    def derivative(self, func, x, h=1e-5):
        return (func(x + h) - func(x - h)) / (2*h)
    
    def integral(self, func, a, b, n=1000):
        h = (b - a) / n
        s = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            s += func(a + i*h)
        return s * h

    # -------------------------------
    # 📈 Matrix Operations (NumPy)
    # -------------------------------
    def matrix_add(self, A, B): return np.add(A, B)
    def matrix_multiply(self, A, B): return np.dot(A, B)
    def matrix_transpose(self, A): return np.transpose(A)
    def matrix_inverse(self, A): return np.linalg.inv(A)
    def matrix_determinant(self, A): return np.linalg.det(A)

    # -------------------------------
    # 🔥 Extra Utility
    # -------------------------------
    def log(self, x, base=math.e): return math.log(x, base)
    def exp(self, x): return math.exp(x)
    def round_to(self, n, decimals=0): return round(n, decimals)
    def percentage(self, part, whole): return (part/whole)*100 if whole != 0 else 0
    
    def compound_interest(self, principal, rate, time, n=1):
        # Formula: A = P * (1 + r/n)^(n*t)
        return principal * (1 + rate/n)**(n*time)
