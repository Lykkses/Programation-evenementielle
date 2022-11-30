try:
    if __name__ == '__main__':
        a = float(input("a:"))
        b = float(input("b:"))
        res = a / b
        print(res)
except ZeroDivisionError:
    print("Division par zero!")
except ValueError:
    print("Entrée invalide!")

else:
    print("Pas de problèmes détéctés.")

finally:
    print("Fin du programme.")
