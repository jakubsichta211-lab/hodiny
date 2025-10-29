#string(str)
jozo=input("zadaj mi :")#len(jozo)kolko znakov
#jozo[3]stvrty znak  0,1,2,3,...
# su tam niake built in funkcie takze ich zavolame jozo.isupper()
print(jozo)
#iteracia(prechhod retazca)
for i in range (len(jozo)):
    print (jozo[i], i)
for i in jozo:
    print(i)