seconds = [100, 50, 1000, 5000, 1000, 500]

min = [seg // 60 for seg in seconds] # / / <- redondea hacia abajo y deja int

print(min) # [1, 0, 16, 83, 16, 8]
