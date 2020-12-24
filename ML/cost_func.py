def cost_func(a, b, x, y):
    sum = 0
    for i in range(len(x)):
       sum = sum + (a * x[i] + b - y[i]) ** 2
    sum = sum/(2*len(x))
    return sum

if __name__ == '__main__':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    x = [float(item) for item in input("Enter x: ").split()]
    y = [float(item) for item in input("Enter y: ").split()]

    print("----------------")
    print("Cost: ", cost_func(a, b, x, y))
