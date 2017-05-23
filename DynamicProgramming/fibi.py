fib_dict = {}

def fib(int_in):
    if int_in in fib_dict:
        return fib_dict[int_in]

    if int_in <= 2:
        return 1
    else:
        fib_dict[int_in] = fib(int_in - 1) + fib(int_in - 2)
        return fib_dict[int_in]

for ii in range(1,20):
    print("fib(" + str(ii) + ") = " + str(fib(ii)))
