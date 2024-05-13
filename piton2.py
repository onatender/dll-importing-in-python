import clr
clr.AddReference(r"C:\Users\ONAT\Desktop\dll calistirma\mydll.dll")

from mydll import Class1

obj = Class1()

result = obj.multiply(15, 10)
print(result) 