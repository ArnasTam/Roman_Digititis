class NumberInfo(object):
    """A class for the number itself and the amount of letters that would be used for roman digits"""

    # initial given number
    startingNumber = 0
    # amount of roman letters
    i_count = 0
    v_count = 0
    x_count = 0
    l_count = 0
    c_count = 0

    def __init__(self, num):
        if (num > 100) or (num < 1):
            raise ValueError("The specifed number is not in the range of 1 to 100")
        else:
            self.startingNumber = num
            self.addRomanLetterCount_All()

    def addRomanLetterCount_All(self):
        for i in range(1,self.startingNumber + 1):
           self.addRomanLetterCount_Single(i)
            
    def addRomanLetterCount_Single(self, num):
        hundrets = num // 100
        tens = num % 100 // 10
        ones = num % 100 % 10

        # ones
        if (ones // 5 != 0) and (ones != 9):
            self.v_count += 1
            self.i_count += ones % 5
        elif (ones != 4) and (ones != 9):
            self.i_count += ones
        elif (ones == 9):
            self.x_count += 1
            self.i_count += 1
        elif (ones == 4):
            self.v_count += 1
            self.i_count += 1    

        # tens 
        if (tens // 5 != 0) and (tens != 9):
            self.l_count += 1
            self.x_count += tens % 5
        elif (tens != 4) and (tens != 9):
            self.x_count += tens
        elif (tens == 9):
            self.c_count += 1
            self.x_count += 1
        elif (tens == 4):
            self.l_count += 1
            self.x_count += 1
        
        # hundreds
        if (hundrets == 1):
            self.c_count += 1

