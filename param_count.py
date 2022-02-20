def param_count(*args):
    count = 0
    for i in args:
        count = count + 1
    print(count)

param_count(2, 3, 4)
