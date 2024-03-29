import statistics

sd =  [66, 66, 67, 69, 69, 72, 76, 77, 77, 74, 70, 66]
osaka = [9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 18, 12]

def f_to_c(temp):
    return (5/9)*(temp - 32)


print(statistics.median(osaka))
print(statistics.median(sd))
print(f_to_c(statistics.median(sd)))