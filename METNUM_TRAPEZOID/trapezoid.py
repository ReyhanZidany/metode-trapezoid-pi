import numpy as np
import time

def trapezoid_integration(f, a, b, N):
    dx = (b - a) / N
    total_area = (f(a) + f(b)) / 2
    for i in range(1, N):
        x = a + i * dx
        total_area += f(x)
    total_area *= dx
    return total_area

def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = trapezoid_integration(f, 0, 1, N)
    end_time = time.time()
    elapsed_time = end_time - start_time
    rms_error = np.sqrt((pi_approx - pi_reference)**2)
    results.append((N, pi_approx, rms_error, elapsed_time))

# Menampilkan hasil
for result in results:
    print(f"N: {result[0]}, Pi Approx: {result[1]}, RMS Error: {result[2]}, Time: {result[3]} seconds")
