x=3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)
#transformandolo en string
y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))
# solo division
print('*' * 10) 
#manera matemática
print(y, x)
tolerance = 0.0001
print(abs(x -y) < tolerance)