#
def factors(num):
    factorList = []
    for i in range(1, num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList
print(factors(120))




















