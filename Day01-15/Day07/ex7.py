import os
import time
import random

def running():
        content = '<--hello<---'
        while True:
                os.system('cls')
                print(content)
                time.sleep(1)
                content = content[1:] + content[0]


def get_code(code_len=4):
        allchars="1234567890asdfghjklzxcvbnmASDFGHJKLQWERTYU"
        #获取自定义字符串长度， last_pos
        last_los = len(allchars) -1   
        code = ''
        for _ in range(code_len):
        #index 保存随机获取到的字符串角标，
                index = random.randint(0,last_los)
                code += allchars[index]
        return code

def getsuffix(filename,host_dot=False):
        pos = '.'
        for i in range (len(filename)-1):
                if filename[i] == pos:
                        index = i+1
        if host_dot == False:
        
                return filename[index:]
        else:
                return filename[index-1:]


def max(x):
        #确保m1 是大于m2 的，m1 永远保存的是最大的一个，m2 保存的是第二大的
        m1,m2 = (x[0],x[1] if x[0] > x[1] else (x[1],x[0]))
        for index in range(2,len(x)):
                if x[index] > m1:
                        m2=m1
                        m1 = x[index]
                elif x[index] > m2 :
                        m2 = x[index]
        return m1,m2 


def whichday(year,month,date):
        monthdays=[
                [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ]
        flag = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        total = 0
        if flag:
                for index in range(month -1):
                        total += monthdays[1][index]
                return total+date
        else:
                
                for index in range(month -1):
                        total += monthdays[1][index]
                return total+date
                
        
        """
        获取输入年份是闰年还是平年，闰年为TRUE，平年为FALSE
        year_type=year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][year_type]（解释，如果year_type 是TRUE，列表中的第二个元素生效，如果
        是FALSE 则第一个元素生效。）
        
        """
        month_day=[
                [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][flag]
        
        for i in range(month-1):
                total += month_day[i]
        return total+day


def random_slecet(balls_no):
        allballs=[x for x in range(1,34)]
        #定义随机选择的最大范围值
        nubmer=len(allballs)-1
        s_balls=[]
        for _ in range(balls_no):
                index = random.randint(0,nubmer)
                s_balls.append(allballs[index])
        return s_balls

        


def main():
        f=random_slecet(balls_no=6)
        print(f)
        pass

if __name__ == '__main__':
    main()
