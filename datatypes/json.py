#import json
Import json

#assign json data to a variable:  json_str
json_str = "valid json string"

#parse JSON string to python dict: json_dict
json_dict = json.load(json_str)

#we have a valid dictionary, let's iterate. (You could enclose the following within try-except blocks  to handle errors)
#iterate through your the dictionary, json_dict
for data in json_dict:
    #we now have access to the dictionaries keys and their values, lets loop through the values
    for elem in json_dict[data]:
        #the value is an array of dictionaries, lets loop through each dictionary looking for the name key-value pair
        for key in elem:
            if key == "id":
                #we now have the name key-value pair,  do what you want with it here
                print(elem[key])