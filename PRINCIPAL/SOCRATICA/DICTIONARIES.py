# FriendsFace post
# user_id = 209
# message = "D5 E5 C5 C4 G4"
# Language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)
post = {"user_id":209,
        "message":"D5 E5 C5 C4 G4",
        "language": "English",
        "datetime": "20230215T124231Z",
        "location":(44.590533, -104.715556)
        }
print(type(post))
post_2 = dict(message= "SS Cotopaxi", language= "English")
print(post_2)
post_2["user_id"] = 209
post_2["datetime"] = "19771116T093001Z"
print(post_2)
if "location" in post_2:
    print(post_2["location"])
else:
    print("The Post does not contain a location value.")
try:
    print(post_2["location"])
except KeyError:
    print("The Post does not contain a location value.")
print(dir(post_2))
print(help(post_2.setdefault))
loc = post_2.get("location", None)
print(loc)
loc1 = post.get("location",None)
print(loc1)
for key in post.keys():
    value = post[key]
    print(key, "=", value)
print('-'*30)
for key, value in post.items():
    print(key,"=", value)

print('='*30)
for value in post.values():
    print(value)
print('~'*30)
for key in post.keys():
    print(key)
post_3 = post_2.copy()
post_2.clear()
post_2.setdefault('user_id',209)
print(post_2)
print(post_3)
try:
    print(type(post_2['user_id']))
except KeyError:
    print("The Post does not contain a location value.")
