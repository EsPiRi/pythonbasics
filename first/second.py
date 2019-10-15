#boolean data type

bool1=4==2*3
bool2=10<2*2**3
bool3=8>2*4+1
print(bool1)
print(bool2)
print(bool3)
print("\n\n")
#lists
my_list=[bool1,bool2,bool3]
colors=["red","orange","yellow","green","indigo","white"]

print(colors[0])    #red
print(colors[4])    #indigo
print(len(colors))  #6
print(colors)   #print the list of the colors

#designing the list for the rainbow colors
colors.remove("white")
colors.append("violet")
print(colors)

colors.insert(4,"blue")
print(colors)

#slicing list
print(colors[3:6])

#dictionary
menu={"spam":12.50,"carbonara":20,"salad":15}
print(len(menu))
print(menu)
menu["cake"]=6
print(menu)

del menu["spam"]
print(menu)

menu["carbonara"]=22
print(menu)

dict.clear(menu)
print(menu)

del menu
print(menu)