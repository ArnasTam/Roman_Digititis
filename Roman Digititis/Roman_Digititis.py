#---------------------------------------------
# 344 - Roman Digititis
# Arnas Tamašauskas IFF-9/11
#---------------------------------------------
from InOut import InOut
from NumberInfo import NumberInfo


inputFile = "StartingData.txt"
resultFile = "Result.txt"

# Using console 
#allNumbers = InOut.inputStartingData_Console()
#InOut.outputResult_Console(allNumbers)

# Using files
allNumbers = InOut.inputStartingData_File(inputFile)
InOut.outputResult_File(allNumbers, resultFile, inputFile)
