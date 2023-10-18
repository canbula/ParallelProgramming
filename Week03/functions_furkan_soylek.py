custom_power=lambda x=0,/,e=1 : x**e

def custom_equation(x:int=0,y:int=0,/,a:int=1,b:int=1,*,c:int=1) -> float:
    """
    Test Function Header.

    :param x: First Number
    :param y: Second Number
    :param a: Third Number
    :param b: Fourth Number
    :param c: Fifth Number
    :return: Given computation
    """
    return (x**a+y**b)/c

def fn_w_counter(*args,**kwargs) -> (int,dict[str,int]):
    if not hasattr(fn_w_counter,'users'):
        fn_w_counter.users={__name__:1}
        fn_w_counter.counter=1
    else:        
        if __name__ not in fn_w_counter.users:
            fn_w_counter.users[__name__]=1
        else:
            fn_w_counter.users[__name__]+=1
        fn_w_counter.counter+=1
    return (fn_w_counter.counter,fn_w_counter.users)


"""
###################################
        Furkan Soylek
https://leetcode.com/TB09/
https://github.com/TIMEBANDIT11111
###################################
"""
        

