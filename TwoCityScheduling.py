# def solve(costs,a,b,sum,i):
#     if a==0 and b==0:
#         return sum
#     if a==0 and b!=0:
#         sum+=costs[i][1]
#         return solve(costs,0,b-1,sum,i+1)
#     if a!=0 and b==0:
#         sum+=costs[i][0]
#         return solve(costs,a-1,0,sum,i+1)
#     else:
#         sum1=sum+costs[i][0]
#         sum2=sum+costs[i][1]
#         return min(solve(costs,a-1,b,sum1,i+1),solve(costs,a,b-1,sum2,i+1))
#
# recursive approach
if __name__ == '__main__':
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    # a = len(costs) // 2
    # b = len(costs) // 2
    # sum = 0
    # print(solve(costs, a, b, sum,0))


# optimized
    a = sorted(costs, key=lambda x: x[0] - x[1])
    Sa = 0
    Sb = 0
    for i in range(len(a) // 2):
        Sa += a[i][0]
    for i in range(len(a) // 2, len(a)):
        Sb += a[i][1]
    print( Sa + Sb)