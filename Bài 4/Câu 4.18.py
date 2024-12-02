print("Le Hoa Hiep")
print("235752021610073")
def fibonacci(n):
  fib = [0, 1]
  while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])
  return fib
n = int(input("Nhập số nguyên n: "))
ket_qua = fibonacci(n)
print("Các số Fibonacci nhỏ hơn", n, "là:", ket_qua)
