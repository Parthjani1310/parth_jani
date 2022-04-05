myDict = { "vidyut" : "martial artist",
           "dhoni"  : "cricketer",
           "Marks"  : "5,4,9,7",
           "AnotherDict":{'virat':'run machine'},
           1:2           
}
print(myDict.keys()) #print the keys of dictionary
print(myDict.values()) # print the values of dictionary
print(myDict.items()) # print the (keys , values) for all contents of the dictionary
print(myDict)
updateDict = {
  "tej" : "friend"
}
myDict.update(updateDict) # update the dictionary by adding key-value pairs from updateDict 
print(myDict)
print(myDict.get("vidyut")) # Returns proper value in the dictionary
print(myDict.get("vidyut2")) # Returns None as vidyut2 is not present in the dictionary
print(myDict.get["vidyut2 "])  # Throws an error as vidyut2 is not present in the dictionary