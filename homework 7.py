import numpy as np
func = input("请输入函数")               #输入函数：如2*np.sin(np.pi*x)+np.cos(np.pi*x)
def f(x):
     return eval(func)                   #更改格式，使其可读成函数形式
con = 1                                   #控制1为一直运行循环，0为结束循环
while con==1:                            #构造死循环 con=0跳出循环
    a=float(input("请输入a值："))        #输入a值，左边值
    b=float(input("请输入b值："))        #输入b值，右边值
    e=float(input("请输入误差最小值："))        #输入e值，最小误差可接受值
    k=0                                   #k=0记录所需要的次数
    if f(a)*f(b)>0:                       #同为正或者同为负值，有多种情况
        print("你输入的范围没有根或有多个根值，请重新输入")
        continue      #重新循环
    else:
        while con==1:     #构造死循环 con=0跳出循环
             if f(a)*f(b)==0: #判断等于0的情况
                if f(a)==0:
                    print("a的值是：",a,"\nk的值是：",k)    #f(a）值为0，中断循环
                    con=0
                else:
                    print("b的值是：", b, "\nk的值是：", k) #f(b)的值为0，中断循环
                    con = 0
             else:                               #f(a)*f(b)<0的情况
                m=(a+b)/2                     #取中间值，二分法
                if np.abs(a-b)<e:              #绝对值小于，则满足最小误差条件
                    print("x的值是：", m, "\nk的次数是：", k,"\n此时误差是：",np.abs(a-b),"\nf（x）值为：",f(m))
                    con = 0
                else:
                    if f(a)*f(m)>0:          #进行二分法步骤，赋值，
                        a=m
                        k=k+1
                        continue
                    else:                     #进行二分法步骤，赋值，
                        b=m
                        k=k+1
                        continue
