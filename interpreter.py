expression = input('Expression: ')
x, y ,z = expression.split()
x = float(x)
z = float(z)

match y:
    case '+':
        answer = (x + z)
    case '-':
        answer = (x - z)
    case '*':
        answer = (x * z)
    case '/':
        answer = (x / z)

answer = round(answer, 1)
print(answer)