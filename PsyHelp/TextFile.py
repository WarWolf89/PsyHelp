
saveFile = open("exampleFile.txt", "w")

numbersArray = []

for numbers in range(1,21):
   numbersArray.append(str(numbers))
   saveFile.writelines((numbersArray))

saveFile.close()
print(numbersArray)




