# # import datetime
# # print("The date and time is: ", datetime.datetime.now()) 
# # mystr = "Hello"
# # translate = {"car": "auto", "cat": "kissa", "beautiful": "kaunis"}
# # tr = input("enter a eng word:")
# # print(translate["car"])

# # x= [1,2,3,5]
# # grade = {"John": 10, "Ela":8.8, "Ola":8.2}
# # print(sum(grade.values()))
# # print("the average is", sum(grade.values())/len(grade))

# #  def mean(value):
# #     if type(value) == dict:
# #         the_mean = sum(value.values() / len(value))
# #     else:
# #         the_mean = sum(value) / len(value)
# #     return the_mean
# # #print(mean(grade))
# # if 3>1:
# #     print("Greater")
# # else:
# #     print("not greater")

# # def weather(temp):
# #     if temp > 7:
# #         return "warm"
# #     else:
# #         return "Cold"
# # user = int(input("enter temperature:"))
# # print(weather(user))

# name = input("Enter your name: ") # This will prompt to input name and then to say hello 
# surname = input("Enter your surname: ") # This will prompt to input name and then to say hello 

#message = "Hello %s %s!" % (name, surname)
# print(message)
# message  = f"Hello {name} {surname} !" # this is nicer version
# print(message)
# msg = ("Hello {}, {}").format(name, surname)
# print(msg)

student = {"John": 8.3, "Ela": 8.9, "Ola": "9.5"}

for k, n in student.items():
    print("The name is ", k, ": the grade is", n)  

# for grades in student.values():
#     print(grades)  