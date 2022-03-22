def karatsuba(x,y):
  n = max(x.bit_length(), y.bit_length())

  # trivial
  if n <= 1:
    return x*y

  # divide
  k = (n + 1) >> 1
  x1 = x >> k
  x0 = x - (x1 << k)
  y1 = y >> k
  y0 = y - (y1 << k)

  # recursions
  a = karatsuba(x1, y1)
  c = karatsuba(x0, y0)
  p = karatsuba(x0 + x1, y0 + y1)
  b = p - a - c

  # conquer
  return (a << (n + (n & 1))) + (b << k) + c

print(karatsuba(10,20))
