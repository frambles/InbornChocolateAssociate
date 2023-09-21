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
    for i in range(30):

      print(f"running iteration {i}...")
      fib_time = perf_counter()
      fib_val = fib_bad(i)
      fib_time = perf_counter() - fib_time
      
      fact_time = perf_counter()
      fact_val = fact(i)
      fact_time = perf_counter() - fact_time
      
      #print(f"{i}, {fib_val}, {exe_time}")
      csvwriter.writerow([i, fib_val, fact_val, fib_time, fact_time])

if __name__ == "__main__":
  main()