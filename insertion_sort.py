ls=[]
ser=int(input("how many elements: "))
if ser>=1 and ser <=8:
    print("enter the number")
    for a in range (0,ser):
       bin=int(input(""))
       ls.append(bin)

    n=len(ls)
    for i in range(1,n):
        key =ls[i]
        j=i-1
        while j>=0 and key <ls[j]:
            ls[j+1]=ls[j]
            j-=1
            ls[j+1]=key
    print("the selection sort of the elements: ",ls)
else:
    print("invalid range of the elements")
