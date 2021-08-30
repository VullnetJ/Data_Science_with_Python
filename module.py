# import time
# import os
# #import sys . sys.builtin_modules_names. sys.prefix
# # open /Users/jata/Desktop/Python/Library/Frameworks/Python.framework/
# while True:
#     if os.path.exists("fruit.txt"):
#         with open("fruit.txt") as file:
#             print(file.read()) #it will read always that file. 
            
#     else:
#         print("File does not exist")
#     time.sleep(10)

## >>> import sys>>> sys.prefix '/Library/Frameworks/Python.framework/Versions/3.8' --> from terminal write: open + >>> import sys
##>>> sys.prefix '/Library/Frameworks/Python.framework/Versions/3.8' --> the site-packages are where are installed other packages in python
# import time
# import os
# import pandas

# while True:
#     if os.path.exists("weather.csv"):
#          data = pandas.read_csv("weather.csv")
#          print(data.mean()["today"])  
#          print(data.mean()) 
#     else:
#         print("File does not exist")
#     time.sleep(10)