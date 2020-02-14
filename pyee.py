even_squares = [num*num for num in range(10) if num%2==0]
d= ", ".join([even_square for even_square in even_squares])
print(d)