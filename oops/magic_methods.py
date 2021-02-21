class IntegerNumber:

    def __init__(self, num=0):
        if type(num)== int:
            self.__num = num
        else:
            self.__num = 0
            raise ValueError("Argument 'num' must be an Integer Number")

    def __str__(self):
        return f'<<IntegerNumber>> value is {str(self.__num)}'

    def __repr__(self):
        return f'<<IntegerNumber>>(value is {str(self.__num)})'


    ''' 
        Magic Method     used for overload Binary Operator    Example
        --------------  ---------------------------------     -------
        __add__                 +	                          object.__add__(self, other)
        __sub__                 -	                          object.__sub__(self, other)
        __mul__                 *	                          object.__mul__(self, other)
        __floordiv__            //	                          object.__floordiv__(self, other)
        __truediv__             /	                          object.__truediv__(self, other)
        __mod__                 %	                          object.__mod__(self, other)
        __pow__                 **	                          object.__pow__(self, other[, modulo])
        __lshift__              <<	                          object.__lshift__(self, other)
        __rshift__              >>	                          object.__rshift__(self, other)
        __and__                 &	                          object.__and__(self, other)
        __xor__                 ^	                          object.__xor__(self, other)
        __or__(                 |	                          object.__or__(self, other)

    '''
    def __add__(self, other):
        if type(other) == IntegerNumber:
            return IntegerNumber(self.__num + other.__num)
        elif type(other) == int:
            return IntegerNumber(self.__num + other)
        else:
            raise ValueError("Argument must be an object of class IntegerNumber or int")
    '''
        Extended Assignments Operator	Magic Method
                            +=	        object.__iadd__(self, other)
                            -=	        object.__isub__(self, other)
                            *=	        object.__imul__(self, other)
                            /=	        object.__idiv__(self, other)
                            //=	        object.__ifloordiv__(self, other)
                            %=	        object.__imod__(self, other)
                            **=	        object.__ipow__(self, other[, modulo])
                            <<=	        object.__ilshift__(self, other)
                            >>=	        object.__irshift__(self, other)
                            &=	        object.__iand__(self, other)
                            ^=	        object.__ixor__(self, other)
                            |=	        object.__ior__(self, other)
    '''
    def __iadd__(self, other):
        if type(other) == IntegerNumber:
            self.__num = self.__num + other.__num
            return self
        elif type(other) == int:
            self.__num = self.__num + other
            return self
        else:
            raise ValueError("Argument must be an object of class IntegerNumber or int")
    '''
        Unary Operators Operator	Magic Method
                        -	        object.__neg__(self)
                        +	        object.__pos__(self)
                        abs()	    object.__abs__(self)
                        ~	        object.__invert__(self)
                        complex()	object.__complex__(self)
                        int()	    object.__int__(self)
                        long()	    object.__long__(self)
                        float()	    object.__float__(self)
                        oct()	    object.__oct__(self)
                        hex()	    object.__hex__(self
        
    '''
    def __int__(self):
        return int(self.__num)

    '''
        Comparison Operators	Magic Method
                    <	        object.__lt__(self, other)
                    <=	        object.__le__(self, other)
                    ==	        object.__eq__(self, other)
                    !=	        object.__ne__(self, other)
                    >=	        object.__ge__(self, other)
                    >	        object.__gt__(self, other)
        
    '''
    def __eq__(self, other):
        if type(other) == IntegerNumber:
            return True if self.__num == other.__num else False
        elif type(other) == int:
            return True if self.__num == other else False
        else:
            return False


def main():
    num1 = IntegerNumber(10)
    print(num1)

    num2 = IntegerNumber(20)
    print(num2)

    num3 = num1 + num2
    print(num3)

    num4 = int(num1)
    print(num4)

    num3 +=num4
    print(num3)

    if(num4 == num1):
        print("num1 and num4 are same value")
    else:
        print("num1 and num4 are not same value")

if __name__ == "__main__":
    main()