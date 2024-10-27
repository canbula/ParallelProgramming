custom_power = lambda x = 0,/, e = 1: x**e
def custom_equeation(x =0,y = 0,/,a =1 ,b =1 ,*,c =1)-> (float):
    """
    This function takes the power of 2 numbers, adds them and divides them.

    :param x : First number
    :param y: Second number
    :param a: Third number
    :param b: Fourth number
    :param c: Fifth number
    :return: taking the number x to the power of a ,
    taking the number y power of b then add them and divides by c.
    """
    return (x**a + y**b)/c
def fn_w_counter()-> (tuple) :
    fn_w_counter.count +=1
    dict = {'__name__': fn_w_counter.count}
    return (fn_w_counter.count,dict)
fn_w_counter.count=0
