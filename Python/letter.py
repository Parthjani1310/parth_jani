letter = '''dear <|name|>,
greetings fron PJ info. We are very happy to tell you abot your selection..!
Have a lovely day ahead ...
you are selected..!
Thanks and regards,

date: <|date|>'''
name= input("Enter Your Name\n")
date= input("Enter Date\n")
letter= letter.replace("<|name|>",name)
letter= letter.replace("|date|",date)
print(letter)