def fn(x=0,y=0,/,a=1,b=1,*,c=1):
    """This function performs complex operations.
     
     :param x:first number and positional-only
     :param y:second number and positional-only
     :param a:third number and positional-or-keyword
     :param b:fourth number and positional-or-keyword
     :param y:fifth number and keyword-only
     :return :Dividing the sum of x to the power of a and y to the power of b by c
    
    
    """
    return (x**a+y**b)/c
