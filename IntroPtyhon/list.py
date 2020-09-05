name = ["Sam", "Amy", "Ben", "Ley"]
ls = ["Sam", 19, "apple", "PC", 123.4]
age = [19, 12, 20, 98]

# count form 0
# range goes form start to finish of a list
# length list

# .append()

agesum = 0
age.append(25)

# agesum += i   == agesum = agesum + i

for i in age:
    agesum += i

print (agesum)

avg = agesum / len(age)

print(avg)

#print(name)
#print(age)


