def listfun():
    cList = ['red','blue','green','yellow']
    print("\nList :")
    print(cList)

    print("\n I like 2 more colours")
    cList.append ('purple')
    print("\nList after adding:")
    print(cList)

    print("I dont like green")
    cList.remove('green')
    print("\nList after removing:")
    print(cList)

    print("\n I dont want the colour on top")
    cList.pop()
    print("\nList after popping an elememt:")
    print(cList)

    print("I want the colours to be in proper order")
    cList.sort()
    print("\nList after sorting:")
    print(cList)

    cList.sort(reverse=True)
    print("\nList in decending order:")
    print(cList)

    cList = ['red','blue','green','yellow']
    print("\nList :")
    print(cList)
    cList2 = ['white','grey']
    cList3 = cList+cList2
    print("\nList after coipying:")
    print(cList3)
listfun()

def tuplefun():
    ctuple1 = ('red','blue','green','yellow')
    ctuple2 = (1,2,7,5)
    print("\n I like colours and numbers !!!")
    ctuple3 = ctuple1 + ctuple2
    print("All colours and numbers together:")
    print(ctuple3)

    print("\nI want the sum of the numbers ")
    Sum = sum(ctuple2)
    print("\nThe sum of numbers is : ")
    print(Sum)

    print("\n I want to print the colours twice")
    print(ctuple1*2)
    
tuplefun()

def setfun():
    cset = {"red","green","blue"}
    print(cset)

    print("\n I like black also")
    cset.add("black")
    print(cset)

    cset = {"red","green","blue"}
    pset = {"ram","sita","riya"}
    likes = cset.union(pset)
    print(likes)

    print("\n I want the length !!")
    print("\nThe length is :",len(cset))

    print("\nI hate red!!")
    cset.discard("red")
    print("\n I like only these colours:",cset)
setfun()


    


