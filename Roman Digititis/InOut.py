from NumberInfo import NumberInfo

class InOut(object):
    """class for input and output operations"""

    @staticmethod
    def inputStartingData_Console():
        enteredNum = []
        print("Input startind data:")
        while bool(1):
            line = input()
            if line and (line != '0'):
                enteredNum.append(NumberInfo(int(line)))
            else:
                break     
        return enteredNum

    @staticmethod   
    def outputResult_Console(array):
        print("\nResult:")
        for i in range(len(array)):
            print(f"{array[i].startingNumber}: {array[i].i_count} i, " + 
                 f"{array[i].v_count} v, {array[i].x_count} x, " +
                f"{array[i].l_count} l, {array[i].c_count} c")

    @staticmethod
    def inputStartingData_File(inputFile):
        enteredNum = []
        file = open(inputFile)
        while bool(1):
            line = file.readline()
            if line and (line != '0'):
                enteredNum.append(NumberInfo(int(line)))
            else:
                break
        file.close()
        return enteredNum
      
    @staticmethod   
    def outputResult_File(array, resultFile, inputFile):
        fileResult = open(resultFile, 'w+')
        fileInput = open(inputFile)
        fileResult.write("StartingData:\n")
        fileResult.write(fileInput.read())
        fileResult.write("\n\nResult:\n")
        for i in range(len(array)):
            fileResult.write(f"{array[i].startingNumber}: {array[i].i_count} i, " + 
                 f"{array[i].v_count} v, {array[i].x_count} x, " +
                f"{array[i].l_count} l, {array[i].c_count} c\n")
        fileResult.close()
        fileInput.close()