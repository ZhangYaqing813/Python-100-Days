# row = input('请输入行数：')
# for i in range(int(row)):
#     for _ in range(i + 1):
#         print ('*',end='')
#     print()


# for i in range(int(row)):
#     for j in range(int(row)):
#         if j < int(row) -i -1:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()
    

 
# while row <=9:
#     col =1
#     while col <=row:
#         print ("%s*%s=%s"%(col,row,row*col),end="\t")
#         col+=1
#     print()
#     row+=1

# while row <= 9:
#     col =1 
#     while col <=(9-row+1):
#         print ("%s*%s=%s"%(col,row,row*col),end="\t")
#         col+=1
#     print()
#     row+=1
# col = 9 
# while col >=1:
#     row =1
#     while row <=col:
#         print("%s*%s=%s"%(col,row,col*row),end="\t")
#         row+=1
#     print()
#     col-=1





# def min_max(mi,ma,*args):
#     for tmp in args:
#         if mi > tmp:
#             mi=tmp
#         if tmp > ma:
#             ma=tmp
#     return ma,mi
    
# y=min_max(1,3,5,6,9,2,20)
# print(y)


# for i in range(1,10):
#     print("\t"*(i-1),end=("\t"))
#     for j in range(i,10):
#         print ("%sX%s=%s"%(j,i,j*i),end="\t")
#     print()
    
# for x in range(1,10):
#     for y in range (x,10):
#         print ("%sX%s=%s"%(x,y,y*x),end="\t")
#     print()

# for a in range(1,10):

#     for b in range(1,a):
#         print ("%sX%s=%s"%(b,a,a*b),end="\t")
#     print ()


# for c in range(1,10):
#     print("\t"*(10-c),end="\t")
#     for d in range(1,c+1):
#         print ("%sX%s=%s"%(d,c,d*c),end="\t")
#     print()




n=5

# for i in range(1,6):    
#     if i <=n :
#         print("*"*i)
#     else: 
#         for j in range(n,1,-1):
#             print("*"*j)



for i in range(1,7):
    if i >n:
        # for j in range(n+1,1-1):
        j=n-1
        while j>=1:
            print("* "*j)
            j-=1
    else:
        print("* "*i)