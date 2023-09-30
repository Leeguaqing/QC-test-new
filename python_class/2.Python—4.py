def good_job(salary,bonus, subsidy=500, *args,**kwargs):
    sum1 = salary + bonus + subsidy#sum1实现功能
    for i in args:
        sum1 += i
    for j in kwargs:
        sum1 += kwargs[j]
    return sum1 ,salary#定义了一个返回值==两个返回值用逗号隔开
result =good_job(8000,2000,800) #用函数名进行函数的调用--函数才会被执行--实参

#if result > 10000:
#print("这个是一个不借的工作!")
#else:
#print("我还可以找到更好的工作!")
print(result)

for i in range(6):
    print(i)