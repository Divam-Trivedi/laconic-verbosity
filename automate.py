import json
ans = 'y'
while(ans == 'y'):
    patterns = []
    responses = []
    print("Enter the details accodingly as prompted ")
    # print("Category of information to be updated: ")
    tag  = input("Category of information to be updated")
    pt = 'y'
    while(pt=='y'):
        pattern = input("Enter the pattern expected from the user: ")
        pt = input("Would you like to add more pattern(s): ")
        patterns.append(pattern)
        if pt == 'y':
            continue
        else:
            break
    re = 'y'
    while(re=='y'):
        response = input("Enter the response to the patern(s) given by user: ")
        re = input("Would you like to add more response(s): ")
        responses.append(response)
        if re == 'y':
            continue
        else:
            break

    y = {}
    y["tag"] = tag
    y["patterns"] = patterns
    y["responses"] = responses
    y["context"] = []

    

    with open('intents.json','r+') as file:
        file_data = json.load(file)
        file_data["intents"].append(y)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    file.close()
    
    ans = input("Would you ike to continue? ")
    if re == 'y':
        continue
    else:
        break
    
    