


if __name__ == "__main__":
    try:
        f = open("textefile.txt", "r")
        content = f.read()
        f.close()
    except FileNotFoundError:   #Exception si le fichier n'existe pas
        print("File not found")
    except PermissionError:    #Exception si le fichier n'est pas accessible
        print("You don't have permission to read this file")
    except FileExistsError:   #Exception si le fichier existe déjà
        print("File already exists")
    except IOError:  #Exception si le fichier n'est pas accessible
        print("File not found")
    else:   
        print(content)
    finally:    #finally est présent pour excécuter le code quelque soit la présence ou non d'erreur
        f = open("textefile.txt", "r")
        content = f.read()
        f.close()