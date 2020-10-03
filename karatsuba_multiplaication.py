# python function to multiply 2 numbers using the karatsuba algorithm 
# the example uses 2 - 64 digit strings to perform the operation
def karatsuba(m, n):
  m_l = len(m)
  n_l = len(n)
  # length of each number
  if m_l <= 1 or n_l <= 1: 
  # if the number is a single digit number, just return the product
    print("iteration " + str(i))
    i += 1
    return int(m) * int(n)
  else:
    # else recursively divide the humber into 2 parts until it reaches length <= 1
    a = n[:(n_l//2)]
    b = n[(n_l//2):]
    c = m[:(m_l//2)]
    d = m[(m_l//2):]
    return(((pow(10, m_l) * int(karatsuba(a, c))) + (pow(10, m_l//2) * (int(karatsuba(a, d)) + int(karatsuba(b, c)))) + int(karatsuba(b, d))))
    # the karatsuba formula for numbers "cd" and "ab" -- ((10^n * ac) + (10^n/2 * (ad + bc)) + bd)

print("mul: " + str(karatsuba("3141592653589793238462643383279502884197169399375105820974944592", "2718281828459045235360287471352662497757247093699959574966967627")))

# result for those 2 numbers would be 
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

