# leson number 1
# What is print and how it's work?
# print python ka build in function ha ,aur iska kaam output yani
#  terminal par message show karana ha matlab vo jo bhi hum print ka andar
#  likhta ha vo show karana ha 

# example:print("Ali")
# isma hum aik naam print ka zariya apna output screen /terminal pa show kara raha ha 


# Syntax of Print() 

#Obj(object)
# object wo hota hain jo aap print() ka through output screen par dikhana chahta ho

# print("Ali",21)

# example: print("Ali",21)
# isma jo Ali aur 21 hai vo object ha joka hum output screen par show karana chahta ha


# Sep(seperation)
# jab aap multiple values print karta ho,to aunka beech ma jo symbol ya space lagta hai,
# usko sep control karta ha

# print("Ali",21,"Hello", sep="/")

# example:print("Ali",21,"Hello", sep="/")
# isma jo har values ka bad  jo / aaraha ha vo sep control kar raah ha 


#end(ending)
# print ka bad kya likha jai ausa end control karta hai,by default
#  print ka bad new line lagta ha lekin aap isa change kar sakta ha 

# print("hello",end="***")
# print("World")

# example:print("hello",end="***")
# print("World")
# isma first print aur second print ka beech ma stars aajaenga ye next line ma nho honge


#File
# jo bhi hum likhta ha vo by default,output terminal/screen par dekhai deta ha.
# lekin aap file parameter use karke output file me bhi likh sakhte ha 

# with open("outputchange.txt","w")as f:
#  print("this is my first Python class" , file=f)

# example: with open("outputchange.txt","w")as f:
#  print("this is my first Python class" , file=f)

# isma "outputchange.txt" ka naam ka file kholi ja rahi ha 
# "w" ka matlab hai write mode(nayi file banana),aur agr pehla se file hai to ausa overwrite kardena
# as f is file ko code ma "f" naam se use karega (ye file object ka shortcut naam ha) 
# with python ka ek smart way hai file handle karna ka. iska faida ye hota ha ka jab 
# file banjata ha to ausa automatic close kardeta ha 
# file=f ka matlab ha screen par dekhai na de is text ko file ma bhej do 
# aur f vo file object ha jo outputchange.txt sa connected ha 


#Flush
# flush batata ha ka output turant screen pa dekhana hai 
# ya python temporary memory ma temporary rakhna ha kuch seconds ka liya

# print("Abdullah","Ahmed",21,flush="true")
# print("Abdullah","Ahmed",21,flush="false")

# example:
# print("Abdullah","Ahmed",21,flush="true")
# true ka matlab output ko turant dekhao delay mat karo,
# issa hamara cpu pa load parta ha aur hamara program ka performance thora slow hojata ha 

# print("Abdullah","Ahmed",21,flush="false")
# false ka matlab ha output ko pehla temperory memory ma store karo,
# aur phit thori der bad output screen pa show karao issa hamara cpu
# pa load nhi parta aur hamara program ka performance acha hota ha



# leson number 2
# What is Variable and how it's work?:
# variable aik container ki tarah hota ha jisma aap koi bhi value store karat ho
# aur assaign value ka matlab ek variable ka anday koi bhi value store karna hota ha
# name = "Ali"
# age = 21

# example:name = "Ali"
# isma Ali value ha aur name variable ha aur = ka matlab ha ka Ali ko name ka andar rakh do