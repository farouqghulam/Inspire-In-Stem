from tkinter.font import names


#name = "joes cafe"
#print(name)

first_name = "joe"
last_name = "doe"

#full_name = first_name + ' ' + last_name
#print(full_name)

full_name = f"{first_name} {last_name}"
#print(full_name)   

movies = ["the holy grail ,the life of brian ,the meaning of life"]
#print(movies[0])

cast = ['berlin','jones','pelin','zerin']
#print(len(cast))
#print(cast[1])

cast.append("power")
#print(cast)

movies.append("money heist")
#print(movies)

cast.pop()
#print(cast)

cast.extend(["power", "chapman"])
#print(cast)

cast.remove("power")
#print(cast)

cast.insert(0,'power')
#print(cast)

cast.extend(["lucifer", "nikita","empire" ])
#print(cast)

cast.remove("power")
#print(cast)

print(cast[0])

names = ['michael', 'mutko']
isinstance(names, list)