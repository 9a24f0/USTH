import math

def sigmoid(theta, x):
    result = []
    for j in range(len(x[0])):
        p = 0
        for i in range(len(x)):
            p -= theta[i] * x[i][j]
        result.append(1/(1 + math.exp(p)))
    return result

def pre_process(x):
    return [[1] * len(x) , x]

if __name__ == '__main__':
   x = pre_process([float(item) for item in input("Enter x: ").split()])
   theta = [float(item) for item in input("Enter theta: ").split()]
   print(sigmoid(theta, x))
