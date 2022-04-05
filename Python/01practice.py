myDict = {
            "pankha" : "fan",
            "dabba" : "box",
            "vastu": "item" 
}
print("options are",myDict.keys())
a = input("enter the hindi word\n")

# Below line will not throw an error if the key is not present in the dictionary
print("the meaning of your word is:", myDict.get(a))