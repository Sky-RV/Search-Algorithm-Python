import colorama
import os
from pyfiglet import Figlet
from colorama import Fore, Back, Style

################################################ MAIN ################################################

def main():

    print(Style.RESET_ALL)

    option = input("Choose your option : ")

    if option == "1":
        linearSearch()

    elif option == "2":
        binarySearch()

    elif option == "3":
        binarySearchRecursion()

    elif option == "4":
        binarySearchTree()

    else:
      print(Fore.RED + "Error! \nPlease choose a valin number.")
      main()

################################################ BODY ################################################

os.system('cls')

banner = Figlet(font='banner3-D')

print(Fore.RED)
print(banner.renderText("Searchs"))
print(Style.RESET_ALL)

print("Lists of searchs : ")

searchsArray = ["Linear Search", "Binary Search", "Binary Search Recursion", "Binary Search Tree"]
listNumbers = "[{}] : "

for i in range(len(searchsArray)):
    print(Fore.GREEN)
    print(listNumbers.format(i+1) + Fore.LIGHTBLACK_EX + searchsArray[i])

main()
