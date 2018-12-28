# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula area = (s*(s-a)*(s-b)*(s-c)) ** 0.5.
#Function to take the length of the sides of triangle from user should be defined in the parent
#class and function to calculate the area should be defined in subclass.
class Sides:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Area(Sides):
    def __init__(self):
        Sides.__init__(self,3)
    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = round(float((s*(s-a)*(s-b)*(s-c)) ** 0.5),2)
        print ("Semiperimeter of triangle is ", s)
        print('The area of the triangle is ', area)
t = Area()
si = t.inputSides()
di =t.dispSides()
ar = t.findArea()

#1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
#the list of words that are longer than n.

def filter_long_words(wordlist, length):
    return (word for word in wordlist if len(word) > length)

def main():
    words = input("Enter words, separated by spaces: ").split()
    n = int(input("Minimum length of words to keep: "))
    print("Words longer than {0} are {1}.".format(n,','.join(filter_long_words(words, n)))) 
main()
    
#2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
#Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.
 
def length(string):
    le = len(string)
    t = []
    for i in range(0,le):
        t.append(len(string[i]))    
    print("List of length of words :", t)
list_words = ["ab", "abc", "defg"] 
p = length (list_words)

#2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
#it is a vowel, False otherwise.

def vowel (char):
    vowel_list = ['a','e','i','o','u']
    return any (char in letter for letter in vowel_list)
input_char = input ("Enter a character: ") 
vowel_check = vowel(input_char)
vowel_check












