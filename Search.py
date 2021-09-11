import colorama
import os
from pyfiglet import Figlet
from colorama import Fore, Back, Style

################################################ CLASS ################################################

class BinarySearchTree_Node:

    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

    def Insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.Insert(val)
                return
            self.left = BinarySearchTree_Node(val)
            return
        if self.right:
            self.right.Insert(val)
            return
        self.right = BinarySearchTree_Node(val)

    def get_Min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def grt_Max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def Delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.Delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.Delete(val)
            return self
        if self.rigt == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.Delete(min_larger_node.val)
        return self

    def Exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.Exists(val)
        if self.right == None:
            return False
        return self.right.Exists(val)

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

################################################ LINEAR ################################################

def linearSearch():
    os.system('cls')
    print(Fore.YELLOW + "Linear Search\n\n")
    print(Style.RESET_ALL)

    array = input("Enter the list : ")
    array = array.split()
    array = [int(x) for x in array]

    print(Fore.CYAN)
    key = int(input("Enter the key : "))

    index = Linear_Search(array, key)

    if index < 0:
        print(Fore.RED + "{} was not found.".format(key))
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "{} was faound at index {}.".format(key, index))
        print(Style.RESET_ALL)


def Linear_Search(alist, key):

    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1

################################################ BINARY ################################################

def binarySearch():

    os.system('cls')
    print(Fore.YELLOW + "Binary Search\n\n")
    print(Style.RESET_ALL)

    array = input("Enter the list : ")
    array = array.split()
    array = [int(x) for x in array]

    print(Fore.CYAN)
    key = int(input("Enter the key : "))

    index = Binary_Search(array, key)

    if index < 0:
        print(Fore.RED + "{} was not found.".format(key))
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN + "{} was faound at index {}.".format(key, index))
        print(Style.RESET_ALL)

def Binary_Search(alist, key):

    start = 0
    end = len(alist)

    while start < end:
        mid = (start + end) // 2

        if alist[mid] > key:
            end = mid

        elif alist[mid] < key:
            start = mid + 1

        else:
            return mid
    return -1

################################################ Binary Search Recursion ################################################

def binarySearchRecursion ():
    os.system('cls')
    print(Fore.YELLOW + "Binary Search Recursion\n\n")
    print(Style.RESET_ALL)

    array = input("Enter the list : ")
    array = array.split()
    array = [int(x) for x in array]

    print(Fore.CYAN)
    key = int(input("Enter the key : "))

    index = Binary_Search_Recursion(array, 0, len(array)-1, key)

    if index != -1:
        print(Fore.GREEN + "{} was faound at index {}.".format(key, index))
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + "{} was not found.".format(key))
        print(Style.RESET_ALL)

def Binary_Search_Recursion (alist, low, high, key):

    if high >= low:

        mid = (high + low) // 2

        if alist[mid] == key:
            return mid

        elif alist[mid] > key:
            Binary_Search_Recursion(alist, low, mid-1, key)

        else:
            return Binary_Search_Recursion(alist, mid+1, high, key)

    else:
        return -1

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
