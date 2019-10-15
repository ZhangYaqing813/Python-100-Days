import time
import math
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour=hour
        self._minute=minute
        self._second=second
        
    def run(self):
        self._second +=1
        if self._second == 60:
            self._second=0
            self._minute+=1
            if self._minute == 60:
                self._minute = 0 
                self._hour+=1
                if self._hour==24:
                    self._hour = 0
    
    def show(self):
        return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)
 
 
 
 
 
class point(object):
    def __init__(self,x=0,y=0):
        self.x = x 
        self.y = y

    def newpoint(self,nx,ny):
        self.x=nx
        self.y=ny
    
    def newdes(self,old):
        dx = self.x - old.x
        dy = self.y - old.y
        return math.sqrt(dx**2 + dy**2)
    
    def __str__(self):
        return '(%s,%s)' %(str(self.x),str(self.y))
   
    
def main():
    # clock = Clock(10,59,40)
    # while True:
    #     print(clock.show())
    #     time.sleep(1)
    #     clock.run()

    p1 = point(0,0)
    p2 = point (5,5)
    
    print(p1)
    
    p2.newpoint(10,10)
    print(p1.newdes(p2))
    



class student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def study(self,course_name):
        print("%s study %s" %(self.name,course_name))

    def watch(self):
        if self.age <=18:
            print("Only watch xiyangyang")
        else:
            print("You can see others")

def main():
    std1=student('zhangyaqing',20)
    std1.study('python')
    std1.watch()

    std2=student("da chui",15)
    std2.watch()


if __name__ == '__main__':
    main()

