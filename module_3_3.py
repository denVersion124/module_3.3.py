def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
list_ = [1,2,3]
print_params(4)
print_params(list_)
print_params(b = 25)
values_list = [1,"list", True]
values_dict = {"a": 1, "b": "piz", "c": False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1,True]
print_params(*values_list_2, 42)