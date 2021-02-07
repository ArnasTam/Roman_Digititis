import NumberInfo

class InOut(object):
    """class for input and output operations"""

    @staticmethod
    def inputStartingData():
        enteredNum = []
        while bool(1):
            number = int(input())
            if(number != 0):
                enteredNum.append(NumberInfo.NumberInfo(number))
            else:
                break      
        return enteredNum

    @staticmethod   
    def outputAnswer(array):
        for i in range(len(array)):
            print(f"{array[i].startingNumber}: {array[i].i_count} i, " + 
                 f"{array[i].v_count} v, {array[i].x_count} x, " +
                f"{array[i].l_count} l, {array[i].c_count} c")