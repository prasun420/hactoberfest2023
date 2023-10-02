def getfirstletter(n):
    l1=['apple','ball','cat','Car','costume','Dress','dog','debjani','Box','ant','axe','Beautiful','cartoon','Ditch','district']
    for i in l1:
        if(i[0].lower()==n.lower()):
            print(i)


char=input("Enter first letter to search for: ")
getfirstletter(char)
