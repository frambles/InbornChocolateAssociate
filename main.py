import csv

from time import perf_counter

def fact(n):
  if n > 0:
    return n*fact(n-1)
  else:
    return 1

def fib_bad(n):
  if n > 1:
    return fib_bad(n-1) + fib_bad(n-2)
  else:
    return 1

def main():
  with open("fib_bad.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile)
    for i in range(50):
      exe_time = perf_counter()
      fib_val = fib_bad(i)
      exe_time = perf_counter() - exe_time
      #print(f"{i}, {fib_val}, {exe_time}")
      csvwriter.writerow([i, fib_val, exe_time])

if __name__ == "__main__":
  main()