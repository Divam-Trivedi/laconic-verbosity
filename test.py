# # file = open('intents.json', '+r')
# # length = len(file.readlines())
# # array = []
# # tag = "tacher"
# # for i in range(length-2):
# #     array.append(file.readline())
# # # file.truncate(0)
# # # array.append('\{"tag": "'+tag+"',")
# # # array.append("}")
# # # array.append("]")
# # # array.append("}")
# # print(array)
# # # file.writelines(array)

# import json 
# y = {"emp_name":"Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#     }
# with open('intents.json','r+') as file:
#     file_data = json.load(file)
#     file_data["intents"].append(y)
#     file.seek(0)
#     json.dump(file_data, file, indent = 4)
 

y = {}
tag = "heejw"
y["tag"] = tag
print(y)