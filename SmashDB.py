from sys import argv
from os.path import exists

script, inptFile = argv

if (exists(inptFile)):
    chrFile = open(inptFile)
    print(f"Name: {chrFile.readline()}", end = "")
    print(f"Franchise: {chrFile.readline()}", end = "")
    print(f"Signature Move: {chrFile.readline()}", end = "")
else:
    chrFile = open(inptFile, "w")
    chrName = input("Enter name: ")
    chrFranchise = input("Enter franchise: ")
    chrSigMove = input("Enter signature move: ")
    chrFile.write(chrName + "\n" + chrFranchise + "\n"
        + chrSigMove + "\n")

chrFile.close()
