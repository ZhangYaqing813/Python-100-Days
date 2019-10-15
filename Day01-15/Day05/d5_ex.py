# number= input("enter a number ")
# number=int(number)
# for i in range(number):
#     h= i // 100
#     m= i %100//10
#     l = i %100%10

#     sum = h**3+m**3+l**3

#     if sum == i:
#         print(sum,'\n','-----')


# for i in range (1,number):
#     nu=[]
#     tmp = i//2
#     for j in range(1,tmp+1):
#         if  i %j == 0:
#             nu.append(j)
#     y=0
#     for x in nu:
#         y+=x
#     if y == i:
#         print(i)



# 公鸡数量为 g 价格为5
#母鸡数量为f      价格为3
#小鸡数量为100-f-g  价格为1/3

#5*g+3*f+(100-f-g)/3


# for g in range(20):
#     for f in range(34):
#         if 15*g+9*f+(100-f-g) == 300:
#             print(g,f,(100-g-f))



# for i in range(1,10):
#     print ()
#     for j in range(1,i+1):
#         print ("%s*%s=%s" %(j,i,i*j),end='\t')
        


# while  True:
#     number=input("enter a number:\n")
#     number = int(number)
#     if number < 10 and number >0:
#         print("this is a goog number")
#     if number >=10 and number <= 99 :
#         if number//10 == number%10:
#             print(number)
#         else:
#             print("%s not ok " %number)     
#     elif number >100: 
#         if number //100 == number %10 :
#             print(number)
#         else:
#             print("%s not ok " %number)
    
#     if number==0:
#         exit()




# num = int(input('请输入一个正整数: '))
# temp = num
# num2 = 0
# while temp > 0:    #第一次 temp=121  二次：temp=12
#     num2 *= 10         #第一次 num2=0     二次： num=10
#     num2 += temp % 10  #第一次 num =1   二次 num=10+2 12
#     temp //= 10  #第一次 temp =12   
# if num == num2:
#     print('%d是回文数' % num)
# else:
#     print('%d不是回文数' % num)


num=[1,2,3,4,5,6,7,8,9]
p=[]
for index ,i in enumerate(num):
    hig=len(num)-1
    if hig <=1:
        print("only one ")
        exit()
    if index >  hig:
        index-=hig
        p.append(num.pop(index))
    else:
        index+=2
        p.append(num.pop(index))
print(p)