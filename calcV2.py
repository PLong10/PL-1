import sys

if len(sys.argv) > 3:
    firstnumber = sys.argv[1]
    type = sys.argv[2]
    secondnumber = sys.argv[3]

    print(firstnumber + type + secondnumber + '=') 

    

    if type == '+':
        print (float (firstnumber) + float (secondnumber))
    
    if type == '-':
        print (float (firstnumber) - float (secondnumber))
    
    if type == '*':
        print (float (firstnumber) * float (secondnumber))
    
    if type == '/':
        print (float (firstnumber) / float (secondnumber))
    
    if type == '**':
        print (float (firstnumber) ** float (secondnumber))

