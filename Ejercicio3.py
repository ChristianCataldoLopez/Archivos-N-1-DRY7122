acl = int (input("Ingrese su acl: "))
if acl >= 1 and acl <= 99:
    print ("La acl",acl,"corresponde a una estandar")
elif acl >= 100 and acl < 199:
    print ("La acl",acl,"corresponde a una extendida")
else:
    print ("El numero",acl,"NO corresponde a una ACL")
