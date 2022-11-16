try:
    f  = open('D:\Backup\Thomas\BUT RT 2\Prog_evenementielle\Exception\textefile.txt', 'r')
    read = f.read()
    print(read)
    
except FileNotFoundError:
    print("Le fichier n'existe pas!")

except IOError:
    print("Problème d'entrée/sortie!")

except PermissionError:
    print("Vous n'avez pas les droits!")

except FileExistsError:
    print("Le fichier existe déjà!")

else : # pas d'exception
    print("Le fichier existe et est ouvert.")

try :
    for line in f:
        print(line)
    
except IOError:
    print("Problème d'entrée/sortie!")

finally:
    print("Fermeture du fichier.")
    f.close()
    






