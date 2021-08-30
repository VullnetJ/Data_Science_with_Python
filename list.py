temp = [220,235, 340, 333, 0, -888, 245]

# new_temp = []
# for t in temps:
#     new_temp.append(t / 10)
# print(new_temp)
# new_temperature = [t/10 for t in temp]
# print(new_temperature)
# new_temperature = [t/10 for t in temp if t !=-888]
# print(new_temperature)
# new_temperature = [t/10 if t !=-888 else 0 for t in temp]
# print(new_temperature)

# def area(l, w):
#     return l*w
# def area(l=4, w=4): # l = 4 cant be assignet if w is empty or default 
#     return l*w    
# # print(area(l =2, w=5)) with key word arguments, and below it is without keyword arguments
# print(area(2, 5))

# def avg(*args):
#     return sum(args) / len(args)
# print(avg(1, 23, x =5, 6, 54))

def avg(**kw):
    return kw
print(avg(a = 5, b= 6, c = 3))