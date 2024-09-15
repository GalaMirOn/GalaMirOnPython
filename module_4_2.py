def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
# print(globals())
# inner_function()
"""
File "C:\PycharmProjects\PythonMirOn\Gala_Py\module_4_2.py", line 9, in <module>
    inner_function()
    ^^^^^^^^^^^^^^
NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
"""
