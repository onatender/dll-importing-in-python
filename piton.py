import ctypes

my_dll = ctypes.WinDLL(r'C:\Users\ONAT\Desktop\dll calistirma\mydll.dll')

arg_types = [ctypes.c_int, ctypes.c_int]

return_type = ctypes.c_int

my_function = my_dll.multiply
print(my_function.multiply)
my_function.argtypes = arg_types
my_function.restype = return_type

print(my_function(3,5))