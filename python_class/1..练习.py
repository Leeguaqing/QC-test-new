"""a = [1,2,'6','summer']
dict_1 = {"class_id":45,'num':20}
list3 = ['周图','僧','旧模样','ouyang','Nacy','土豆江']

if 'i' in a:
    print('在列表里')
else:
    print("不在列表里")

if dict_1.get('num') > 5:
    print(dict_1['num'])

list1 = [20,3.14,True,"七木","荷花鱼",[1,2,3,4]]
print(list1[5][1])"""
count=0   #计数器
list1 = ['方方士','七木','荷花鱼','kingo','Amiee','焕蓝','十又','bingo','陌上寸草','大丑']
for name in list1:
#不打印“荷花鱼”
    if name == "荷花鱼":    #False(结果为false不执行里面语句)
        continue#跳出本次循环
    # break	#跳出整个循环
    print(name)
    count+=1	#每次循环+1
print(count)	#打印循环次数
print(len(list1))	#打印列表长度
