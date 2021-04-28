import string
import random as rd


def passwordgenerate(l):

    password = ""
    ch = rd.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits,k=l-2)
    password = "".join(rd.choices(string.ascii_uppercase,k=1))
    for i in ch:
        password += i
    symbols = ["@","#","$"]
    sym = rd.choices(symbols,k=1)
    password += sym[0]
    return password

if __name__ == "__main__":
    try:
        while True:
            l = int(input("\nEnter the length of the Password : "))
            if l > 7 and l <= 20:
                password = passwordgenerate(l)
                print("\nYour Password is : ", password, "\n")
            else:
                print("\nYour password length is too SHORT or too LONG")
                print("Please enter atleast 8 unit of length")
    except ValueError:
        pass
