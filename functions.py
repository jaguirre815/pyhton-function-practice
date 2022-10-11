

def max_num(num1, num2, num3):
 list = [num1, num2, num3]
 return max(list)

print(max_num(10, 15, 20))

def mult_list(a, b, c):
 list = [a, b, c]
 return a*b*c

print(mult_list(10, 10, 10))


def rev_string(string):
 return string[::-1]

print(rev_string(""))
print(rev_string("reverse"))
print(rev_string("big dog"))

def num_within(beginning, test, end):
 return test in range(beginning,end+1)

print(num_within(15, 25, 40))
print(num_within(15, 25, 20))

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("not enough rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_n = 2
    while len(triangle) < n:
      row = []
      row_before = triangle[row_n - 1]
      length = len(row_before)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_n-1][i-1]+triangle[row_n-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_n += 1
    for row in triangle:
      print(row)

pascal(4)
pascal(7)