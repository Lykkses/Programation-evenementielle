
if __name__ == "main":
    try:
        with open ("textfile.txt", "r") as f:
            for i in f:
                l= l.rstrip("\n\r")
                print(l)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You don't have permission to read this file")
    except FileExistsError:
        print("File already exists")
    except IOError:
        print("File not found") 
    else:
        print("main")
    finally:
        with open ("textefile.txt", "r") as f:
            for i in f:
                l= l.rstrip("\n\r")
                print(l) 
