#---------------------------
#Austin Jian and Evan Zhao
#ICS201-2
#Summative
#---------------------------

#Import tkinter modules 
from tkinter import * 
from tkinter import ttk
from tkinter.tix import * 

#Defines some fonts
arial14Bold = 'Arial 14 bold'
calibri12 = 'Calibri 12'
helvetica14 = 'Helvetica 14'
helvetica8 = 'Helvitica 7'
calibri16 = 'Calibri 16'
calibri10 = 'Calibri 10'
calibri10Bold = 'Calibri 10 bold'

#Creates a dictionary with double-digit numbers and respective letter 
letterValues = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g', '17': 'h', '18': 'i', '19': 'j', '20': 'k', '21': 'l', '22': 'm', '23': 'n', '24': 'o', '25': 'p', '26': 'q', '27': 'r', '28': 's', '29': 't', '30': 'u', '31': 'v', '32': 'w', '33': 'x', '34': 'y', '35': 'z'}

#Defines a function to check if the user entered number is valid
def validityCheck(checker, base, answer):
    #Checks if there is more than one decimal or negative sign in user input
    if checker.count(".")>1 or checker.count("-")>1:
      #Returns error message
      answer.set("Error")
    #Checks if the appropriate characters are in the user input
    for valid in checker:
      if valid not in ".-01" and base == 2 or valid not in ".-012" and base == 3 or valid not in ".-0123" and base == 4 or valid not in ".-01234" and base == 5 or valid not in ".-012345" and base == 6 or valid not in ".-0123456" and base == 7 or valid not in ".-01234567" and base == 8 or valid not in ".-012345678" and base == 9 or valid not in ".-0123456789" and base == 10 or valid not in ".-0123456789a" and base == 11 or valid not in ".-0123456789ab" and base == 12 or valid not in ".-0123456789abc" and base == 13 or valid not in ".-0123456789abcd" and base == 14 or valid not in ".-0123456789abcde" and base == 15 or valid not in ".-0123456789abcdef" and base == 16 or valid not in ".-0123456789abcdefg" and base == 17 or valid not in ".-0123456789abcdefgh" and base == 18 or valid not in ".-0123456789abcdefghi" and base == 19 or valid not in ".-0123456789abcdefghij" and base == 20 or valid not in ".-0123456789abcdefghijk" and base == 21 or valid not in ".-0123456789abcdefghijkl" and base == 22 or valid not in ".-0123456789abcdefghijklm" and base == 23 or valid not in ".-0123456789abcdefghijklmn" and base == 24 or valid not in ".-0123456789abcdefghijklmno" and base == 25 or valid not in ".-0123456789abcdefghijklmnop" and base == 26 or valid not in ".-0123456789abcdefghijklmnopq" and base == 27 or valid not in ".-0123456789abcdefghijklmnopqr" and base == 28 or valid not in ".-0123456789abcdefghijklmnopqrs" and base == 29 or valid not in ".-0123456789abcdefghijklmnopqrst" and base == 30 or valid not in ".-0123456789abcdefghijklmnopqrstu" and base == 31 or valid not in ".-0123456789abcdefghijklmnopqrstuv" and base == 32 or valid not in ".-0123456789abcdefghijklmnopqrstuvw" and base == 33 or valid not in ".-0123456789abcdefghijklmnopqrstuvwx" and base == 34 or valid not in ".-0123456789abcdefghijklmnopqrstuvwxy" and base == 35 or valid not in ".-0123456789abcdefghijklmnopqrstuvwxyz" and base == 36:
        #Returns error message
        answer.set('Error')

#Function that returns number value after given letter
def return_key(val):
  #Loops in the dictionary to find the corresponding letter 
  for key, value in letterValues.items():
    if value==val:
      return key

#Creates a function to convert between base values
def convert():

  #Initial value for answer
  answer.set('')
  
  #Gets needed information from gui
  numConvert = txt_userNumber.get()
  convertFrom = fromBase.get()
  convertTo = toBase.get()
  
  #Makes numConvert case insensitive
  numConvert = numConvert.lower()
  
  #Turns the selected base conversion to integers
  convertFrom = int(convertFrom[:2])
  convertTo = int(convertTo[:2])

  #Checks if user input is valid
  validityCheck(numConvert, convertFrom, answer)
  convertResult = 'Error'

  if answer.get() != 'Error':

    #Defines a variable to store base 10 value of user input
    base10ConvertNumber = 0

    #Creates a list to keep track of the result digits
    convertRemainderList = []

    #Checks if the user input is negative
    if numConvert[:1] == "-":
      negativeNumber = True
      numConvert = numConvert.replace("-", "")
    else:
      negativeNumber = False
      
    #Checks if the user input is a decimal
    if "."in numConvert:
      integerValue = numConvert[:numConvert.find(".")]
    else:
      integerValue = numConvert
    #Turns the user input into a string
    integerValue = str(integerValue)

    #Reverses the order of user input string
    integerValue = integerValue[::-1]

    #Algorithm to find base 10 value of user input
    #For loop to cycle through user input
    for exponent in range(len(integerValue)):
      #Checks if there are any letters in user input
      #If there are letters, they return the letter's appropriate numerical value
      if return_key(integerValue[exponent])!= None:
        base10ConvertNumber += int(return_key(integerValue[exponent]))*convertFrom**exponent
      else:
        base10ConvertNumber += int(integerValue[exponent])*convertFrom**exponent

    #Algorithm to convert from base 10 to the destination base
    while base10ConvertNumber!=0:
      #Creates a variable to store the remainder 
      remainder = base10ConvertNumber%convertTo
      #Updates base 10 number value
      base10ConvertNumber //= convertTo
      remainder = str(remainder)
      #Gets appropriate letter based off numerical value
      remainderResult = letterValues.get(remainder)
      #Checks if numbers need to be substituted with letterValues
      if remainderResult != None:
        #adds character to the digit list
        convertRemainderList.append(remainderResult)
      else:
        #adds character to the digit list
        convertRemainderList.append(remainder)

    #Checks if the number is negative
    if negativeNumber == True:
      #Adds a negative sign if the resulting number is negative
      convertRemainderList.append("-")
    #Reverses the digit list to give the correct answer
    convertRemainderList.reverse()

    #Checks if the user input has decimal points
    if '.' in numConvert:
      
      #Takes the decimal point value from the user input
      decimalPointValue = numConvert[numConvert.find(".")+1:numConvert.find(".") + 5]
      #Variable to store the decimal value final result
      decimalPointSum = 0

      #Algorithm to convert decimal point value into base 10
      #For loop to cycle through each digit of the decimal point value
      for exponent in range(-1, -len(decimalPointValue)-1, -1):
        #Checks if there are letters in the decimal point value, and if there is, it returns the letter value.
        if return_key(decimalPointValue[-exponent-1])!= None:
          
          decimalPointSum += int(return_key(decimalPointValue[-exponent-1]))*convertFrom**exponent
        else:
          decimalPointSum += int(decimalPointValue[-exponent-1])*convertFrom**exponent
  
      decimalPointSum = round(decimalPointSum,2)
      decimalPointSum = str(decimalPointSum)

      #Creates a list to store the decimal point values
      integerList = []
      convertDecimalInteger = 1

      #Creates infinite loop
      while True:
        #If there are more than 2 decimal points, the loop breaks
        if len(integerList)>=2:
          break

        #Algorithm to turn decimal point value into destination base decimal point value
        #Creates variables to store the integer portion of the algorithm
        convertDecimalInteger = eval(decimalPointSum)*convertTo
        convertDecimalInteger = str(convertDecimalInteger)
        #Takes the decimal point portion after multiplication
        decimalPointSum = convertDecimalInteger[convertDecimalInteger.find('.'):convertDecimalInteger.find('.')+5]
        #Takes integer portion
        convertDecimalInteger = convertDecimalInteger[:convertDecimalInteger.find('.')]

        #If both the integer and decimal point value are zero, the loop breaks
        if convertDecimalInteger == '0' and decimalPointSum == '0':
          break
        #Gets letter based off numerical value according to the appropriate base
        convertDecimalIntegerLetter = letterValues.get(convertDecimalInteger)
        if convertDecimalIntegerLetter != None:
          integerList.append(convertDecimalIntegerLetter)
        else:
          integerList.append(convertDecimalInteger)
      #Turns list into a string
      integerListResult = ''.join(integerList)
      #Appends to resulting list
      convertRemainderList.append(".")
      convertRemainderList.append(integerListResult)
    
    convertResult = ''.join(convertRemainderList)
    
    #Checks if result should be 0, and displays answer
    if convertResult == "" and numConvert != "":
      answer.set("0")
    else:
      answer.set(convertResult)

  #Appends the user inputted things into historyConvert.txt
  storeConvertHistory = open("historyConvert.txt", "a")
  storeConvertHistory.write(f"{numConvert} in base {convertFrom} → {convertResult} in base {convertTo}\n")

#Defines a function to calculate simple operations in any base
def calculate():
   #Initial value for answer
  operationAnswer.set('')
  
  #Gets needed numbers from GUI
  calculateBaseNum = base.get()
  numCalculate1 = userFirstNumber.get()
  numCalculate2 = userSecondNumber.get()
  operation = mathOperations.get()

  #Turns calculateBaseNum into an integer
  calculateBaseNum = int(calculateBaseNum[:2])

  #Checks if user inputs are valid
  validityCheck(numCalculate1, calculateBaseNum, operationAnswer)
  validityCheck(numCalculate2, calculateBaseNum, operationAnswer)

  if operationAnswer.get() != 'Error':
    calculateDecimalNumber1 = 0
    calculateDecimal2 = 0

    #Checks if each user inputted number is negative
    if numCalculate1[:1] == "-":
      negativeNumber1 = True
      numCalculate1 = numCalculate1.replace("-", "")
    else:
      negativeNumber1 = False

    if numCalculate2[:1] == "-":
      negativeNumber2 = True
      numCalculate2 = numCalculate2.replace("-", "")
    else:
      negativeNumber2 = False

    #Checks if user input is a float
    if "." in numCalculate1:
      calculateIntegerValue1 = numCalculate1[:numCalculate1.find(".")]
    else:
      calculateIntegerValue1 = numCalculate1

    #Turns integer portion of user input into a base 10 value
    calculateIntegerValue1 = str(calculateIntegerValue1)
    calculateIntegerValue1 = calculateIntegerValue1[::-1]
    for exponent in range(len(calculateIntegerValue1)):
      if return_key(calculateIntegerValue1[exponent])!= None:
        calculateDecimalNumber1 += int(return_key(calculateIntegerValue1[exponent]))*calculateBaseNum**exponent
      else:
        calculateDecimalNumber1 += int(calculateIntegerValue1[exponent])*calculateBaseNum**exponent

    #turns decimal point portion into base 10 value
    if '.' in numCalculate1:
      decimalPointValue = numCalculate1[numCalculate1.find(".")+1:numCalculate1.find(".") + 5]
      decimalPointSum = 0
      for exponent in range(-1, -len(decimalPointValue)-1, -1):
        if return_key(decimalPointValue[-exponent-1])!= None:
          decimalPointSum += int(return_key(decimalPointValue[-exponent-1]))*calculateBaseNum**exponent
        else:
          decimalPointSum += int(decimalPointValue[-exponent-1])*calculateBaseNum**exponent
      decimalPointSum = round(decimalPointSum,2)
      calculateDecimalNumber1 += decimalPointSum

    #Turns the user input to negative if the input was negative
    if negativeNumber1:
      calculateDecimalNumber1*=-1
    
    #Checks if user input is a float
    if "." in numCalculate2:
      calculateIntegerValue2 = numCalculate2[:numCalculate2.find(".")]
    else:
      calculateIntegerValue2 = numCalculate2
    #Turns integer portion of user input into base 10 value
    calculateIntegerValue2 = str(calculateIntegerValue2)
    calculateIntegerValue2 = calculateIntegerValue2[::-1]
    for exponent in range(len(calculateIntegerValue2)):
      if return_key(calculateIntegerValue2[exponent])!= None:
        calculateDecimal2 += int(return_key(calculateIntegerValue2[exponent]))*calculateBaseNum**exponent
      else:
        calculateDecimal2 += int(calculateIntegerValue2[exponent])*calculateBaseNum**exponent

    #Turns decimal point portion of user input into base 10 value
    if '.' in numCalculate2:
      decimalPointValue = numCalculate2[numCalculate2.find(".")+1:numCalculate2.find(".") + 5]
      decimalPointSum = 0
      for exponent in range(-1, -len(decimalPointValue)-1, -1):
        if return_key(decimalPointValue[-exponent-1])!= None:
          decimalPointSum += int(return_key(decimalPointValue[-exponent-1]))*calculateBaseNum**exponent
        else:
          decimalPointSum += int(decimalPointValue[-exponent-1])*calculateBaseNum**exponent
      decimalPointSum = round(decimalPointSum,2)
      calculateDecimal2 += decimalPointSum

    #Turns user input negative if needed
    if negativeNumber2:
      calculateDecimal2 *= -1

    #Creates list to keep track of result
    calculateRemainderList = []
    
    #Performs appropriate math operation on the user inputs
    if operation == "+ (addition)":
      calculateDecimalNumber = calculateDecimalNumber1 + calculateDecimal2
    elif operation == "- (subtraction)":
      calculateDecimalNumber = calculateDecimalNumber1 - calculateDecimal2
      calculateDecimalNumber = round(calculateDecimalNumber, 2)
    elif operation == "x (multiplication)":
      calculateDecimalNumber = calculateDecimalNumber1 * calculateDecimal2
    elif operation == "÷ (division)":
      calculateDecimalNumber = calculateDecimalNumber1 / calculateDecimal2
    elif operation == "^ (exponent)":
      calculateDecimalNumber = calculateDecimalNumber1 ** calculateDecimal2
    calculateDecimalNumber = str(calculateDecimalNumber)

    #Checks for a negative sign in the user input
    if calculateDecimalNumber[:1] == "-":
      negativeResult = True
      calculateDecimalNumber = calculateDecimalNumber.replace("-", "")
    else:
      negativeResult = False

    #Turns the result back into an int/float
    calculateDecimalNumber = eval(calculateDecimalNumber)
    #Checks if it is a decimal in between 0 and 1
    if calculateDecimalNumber>0 and calculateDecimalNumber<1:
      #If it is, adds 0 into the result list
      calculateRemainderList.append("0")
    #Stores integer portion of result into a variable
    intCalculateDecimalNumber = int(calculateDecimalNumber)
    #While loop to convert result into other bases
    while intCalculateDecimalNumber!=0:
      #Creates a variable to store the remainders, which is then transferred to a list later on
      remainder = intCalculateDecimalNumber%calculateBaseNum
      #Updates the integer portion of the result 
      intCalculateDecimalNumber //= calculateBaseNum
      #Appends the remainder to result list
      remainder = str(remainder)
      #Checks if program needs to get appropriate letter based off number
      remainderResult = letterValues.get(remainder)
      if remainderResult != None:
        calculateRemainderList.append(remainderResult)
      else:
        calculateRemainderList.append(remainder)
    #Checks if the result is true. If it is, a negative sign will be added
    if negativeResult == True:
      calculateRemainderList.append("-")
    calculateRemainderList.reverse()

    #Checks if the result has decimal points
    if "." in str(calculateDecimalNumber):
      calculateDecimalNumber = str(calculateDecimalNumber)
      #Stores the decimal point value into a variable
      decimalPointNumb = calculateDecimalNumber[calculateDecimalNumber.find("."):calculateDecimalNumber.find(".")+5] 
      #Algorithm to convert decimal point value into the destination base 
      integerList = []
      #Makes sure the result is no more than 2 decimals
      while True:
        if len(integerList)>=2:
          break

        #Adds the decimal points to the result
        calculateDecimalInteger = eval(decimalPointNumb)*calculateBaseNum
        calculateDecimalInteger = str(calculateDecimalInteger)
        decimalPointNumb = calculateDecimalInteger[calculateDecimalInteger.find('.'):calculateDecimalInteger.find('.')+5]
        calculateDecimalInteger = calculateDecimalInteger[:calculateDecimalInteger.find('.')]
        #Checks if the integer portion and decimal portion is 0
        if calculateDecimalInteger == '0' and decimalPointNumb == '0':
          #breaks the loop
          break
        calculateDecimalIntegerLetter = letterValues.get(calculateDecimalInteger)
        #Replaces number values with letters if needed
        if calculateDecimalIntegerLetter != None:
          integerList.append(calculateDecimalIntegerLetter)
        else:
          integerList.append(calculateDecimalInteger)
      integerListResult = ''.join(integerList)
      calculateRemainderList.append(".")
      calculateRemainderList.append(integerListResult)

    result = ''.join(calculateRemainderList)

  #Assigns result as error accordingly
  if operationAnswer.get() == "Error":
      result = "Error"
    
  #Displays result
  if result == "" and (numCalculate1 != "" or numCalculate2 != ""):
    result = 0
  operationAnswer.set(result)
    
  #Appends the user inputted things into historyOperate.txt
  storeOperateHistory = open("historyOperate.txt", "a")
  storeOperateHistory.write(f"{numCalculate1} {operation[:1]} {numCalculate2} in base {calculateBaseNum} = {result}\n")

#Defines a function to reset convert tab to initial values
def convertReset():
  #Resets GUI
  txt_userNumber.delete(0, END)
  toBaseClicked.set("10 (decimal)")
  fromBaseClicked.set("10 (decimal)")
  answer.set('')
  #Resets history file
  with open("historyConvert.txt", "r+") as file:
    file.truncate(0)

#Defines a function to reset operation tab to initial 
def operationReset():
  #Resets GUI
  txt_userFirstNumber.delete(0, END)
  txt_userSecondNumber.delete(0,END)
  mathClicked.set("+ (addition)")
  baseClicked.set("10 (decimal)")
  operationAnswer.set('')
  #Resets history file
  with open("historyOperate.txt","r+") as file:
    file.truncate(0)
  
#Defines a function to view conversion calculator history
def historyConvert():
  
  #Reads the historyConvert.txt file
  displayConvertHistory = open("historyConvert.txt", "r")
  convertLines = ""

  #Loop inside the file content
  for line in displayConvertHistory:
    line.strip()
    #Add all the content to convertLines
    convertLines += f"{line}\n"

  #Checks if convertLines is empty and display message
  if convertLines == "":
    convertLines = "Your base conversion history will show up here"

  #Create a new window to display the history as a label
  convertHistory = Tk()
  convertHistory.title('Convert History')
  lbl_convertHistory = Label(convertHistory, text = convertLines, font = calibri10)
  lbl_convertHistory.grid(row = 0, column = 0)

#Defines a function to view operation calculator history
def historyOperate():

  #Reads the historyOperate.txt file
  displayOperateHistory = open("historyOperate.txt", "r")
  operateLines = ""

  #Loop inside the file content
  for line in displayOperateHistory:
    line.strip()
    #Add all the content to operateLines
    operateLines += f"{line}\n"

  if operateLines == "":
    operateLines = "Your base calculator history will show up here"
    
  #Creates a new window to display the history as a label
  operateHistory = Tk()
  operateHistory.title('Calculator History')
  lbl_operateHistory = Label(operateHistory, text = operateLines, font = calibri10)
  lbl_operateHistory.grid(row = 0, column = 0)

#Creates a Tkinter window
window = Tk()
window.title('Base Calculator and Converter')
window.geometry('400x550')

#Creates two tabs in window with ttk
tabControl = ttk.Notebook(window)
baseConversion = ttk.Frame(tabControl)
baseOperation = ttk.Frame(tabControl)
tabControl.add(baseConversion, text ='Base Conversion')
tabControl.add(baseOperation, text ='Base Calculator')
tabControl.pack(expand = 1, fill = "both")

#Creates a heading label for base conversions
lbl_titleConversion = Label(baseConversion, text = 'Base Conversion', font = arial14Bold)
lbl_titleConversion.grid(row = 0, column = 0, padx = 30, pady = 10)

#Creates a label for entry
lbl_inputConversion = Label(baseConversion, text = 'Enter a number to be converted:', font = calibri12)
lbl_inputConversion.grid(row = 1, column = 0, sticky = W, padx = 20, pady = 10)

#Creates an entry for user to enter a number to convert
userNumber = StringVar()
txt_userNumber = Entry(baseConversion, textvariable = userNumber, width = 29, font = helvetica14)
txt_userNumber.grid(row = 2, column = 0, sticky = W, padx = 20)

#Creates a label for the base to be converted from
fromBaseLabel = Label(baseConversion, text = 'From Base', font = calibri12)
fromBaseLabel.grid(row = 3, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a style for the comboboxes 
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground = "white", background= "white")

#A list for the base options
baseOptions = ['2 (binary)', '3', '4', '5', '6', '7', '8 (octal)', '9', '10 (decimal)', '11', '12', '13', '14', '15', '16 (hex)', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']

#Sets an initial value for the base comboboxes
fromBaseClicked = StringVar()
fromBaseClicked.set("10 (decimal)")

#Creates a combobox/dropdown menu for the base to be converted from
fromBase = ttk.Combobox(baseConversion, textvariable = fromBaseClicked, values = baseOptions, width = 28, font = helvetica14, state = 'readonly')
fromBase.grid(row = 4, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a label for the base to be converted to
toBaseLabel = Label(baseConversion, text = 'To Base', font = calibri12)
toBaseLabel.grid(row = 5, column = 0, sticky = W, padx = 20, pady = 5)

#Sets an initial value for the comboboxes
toBaseClicked = StringVar()
toBaseClicked.set("10 (decimal)")

#Creates a combobox/dropdown menu for the base to be converted to
toBase = ttk.Combobox(baseConversion, textvariable = toBaseClicked, values = baseOptions, width = 28, font = helvetica14, state = "readonly")
toBase.grid(row = 6, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a button that uses the convert function 
btn_convert = Button(baseConversion, command = convert, text = "Convert", font = helvetica14, bg = 'green', fg = 'white')
btn_convert.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 20)

#Creates a button that uses the convertReset function
btn_reset = Button(baseConversion, command = convertReset, text = "Reset", font = helvetica14, bg = 'gray', fg = 'white')
btn_reset.grid(row = 7, column = 0, sticky = W, padx = 130, pady = 20)

#Creates a label for the answer widget
lbl_result = Label(baseConversion, text = 'Result', font = calibri16)
lbl_result.grid(row = 8, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a label that displays the result from the convert function  
answer = StringVar()
lbl_answer = Label(baseConversion, width = 25, height = 2, textvariable = answer, bg = 'white', fg = 'black', font = calibri16)
lbl_answer.grid(row = 9, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a button that uses the historyConvert function
btn_historyConvert = Button(baseConversion, command = historyConvert, text = 'History', width = 2, height = 2, font = helvetica8)
btn_historyConvert.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)

# START OF BASE OPERATION GUI

#Creates a heading label for base operations
lbl_baseOperationTitle = Label(baseOperation, text = 'Base Calculator', font = arial14Bold)
lbl_baseOperationTitle.grid(row = 0, column = 0, columnspan = 2, padx = 30, pady = 10)

#Creates a label for the base of the operation 
baseLabel = Label(baseOperation, text = 'Select your base', font = calibri12)
baseLabel.grid(row = 1, column = 0, sticky = W, padx = 20, pady = 5)

#Sets an initial value for the comboboxes
baseClicked = StringVar()
baseClicked.set("10 (decimal)")

#Creates a combobox/dropdown menu for the base 
base = ttk.Combobox(baseOperation, textvariable = baseClicked, values = baseOptions, width = 28, font = helvetica14, state = "readonly")
base.grid(row = 2, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a label for first entry of number
lbl_inputFirstNumber = Label(baseOperation, text = 'Enter the first number:', font = calibri12)
lbl_inputFirstNumber.grid(row = 3, column = 0, sticky = W, padx = 20, pady = 10)

#Creates an entry for the first number to operate
userFirstNumber = StringVar()
txt_userFirstNumber = Entry(baseOperation, textvariable = userFirstNumber, width = 29, font = helvetica14)
txt_userFirstNumber.grid(row = 4, column = 0, sticky = W, padx = 20)

#Creates a label for the math operation
lbl_mathOperation = Label(baseOperation, text = 'Math operation', font = calibri12)
lbl_mathOperation.grid(row = 5, column = 0, sticky = W, padx = 20, pady = 5)

#A list for the math operation options
operationOptions = ['+ (addition)', '- (subtraction)', 'x (multiplication)', '÷ (division)', "^ (exponent)"]

#Sets an initial value for the math operation combobox
mathClicked = StringVar()
mathClicked.set("+ (addition)")

#Creates a combobox/dropdown menu for the math operation
mathOperations = ttk.Combobox(baseOperation, textvariable = mathClicked, values = operationOptions, width = 20, font = calibri10, state = "readonly")
mathOperations.grid(row = 6, column = 0, sticky = W, padx = 20, pady = 5)

#Creates a label for second entry of number
lbl_inputSecondNumber = Label(baseOperation, text = 'Enter the second number:', font = calibri12)
lbl_inputSecondNumber.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)

#Creates an entry for the second number to operate
userSecondNumber = StringVar()
txt_userSecondNumber = Entry(baseOperation, textvariable = userSecondNumber, width = 29, font = helvetica14)
txt_userSecondNumber.grid(row = 8, column = 0, sticky = W, padx = 20)

#Creates a button that uses the calculate function
button_convert = Button(baseOperation, command = calculate, text = "Calculate", font = helvetica14, bg = 'green', fg = 'white')
button_convert.grid(row = 9, column = 0, sticky = W, padx = 20, pady = 10)

#Creates a button that uses the operationReset function
button_reset = Button(baseOperation, command = operationReset, text = "Reset", font = helvetica14, bg = 'gray', fg = 'white')
button_reset.grid(row = 9, column = 0, sticky = W, padx = 143, pady = 10)

#Creates a label for the answer widget
lbl_operationResult = Label(baseOperation, text = 'Result', font = calibri16)
lbl_operationResult.grid(row = 10, column = 0, sticky = W, padx = 20, pady = 10)

#Creates a label that displays the result from the convert function
operationAnswer = StringVar()
lbl_operationAnswer = Label(baseOperation, width = 25, height = 2, textvariable = operationAnswer, bg = 'white', fg = 'black', font = calibri16, borderwidth = 1)
lbl_operationAnswer.grid(row = 11, column = 0, sticky = W, padx = 20, pady = 10)

#Creates a button that uses the historyOperate function
btn_historyOperate = Button(baseOperation, command = historyOperate, text = 'History', width = 2, height = 2, font = helvetica8)
btn_historyOperate.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 5)

#Continues the program
window.mainloop()
