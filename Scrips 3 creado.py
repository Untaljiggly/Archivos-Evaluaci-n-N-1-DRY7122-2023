numero_acl = input("Ingrese el número de ACL IPv4: ")

if int(numero_acl) >= 1 and int(numero_acl) <= 99:
    print("El número de ACL IPv4 corresponde a una ACL Estándar")
elif int(numero_acl) >= 100 and int(numero_acl) <= 199:
    print("El número de ACL IPv4 corresponde a una ACL Extendida")
else:
    print("El número de ACL IPv4 no corresponde a una lista de acceso")
