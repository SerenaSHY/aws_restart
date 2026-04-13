myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item))) # Traditional 

# Newer way to format string
# print(f"{item} is of the data type {type(item)}") 
    
    