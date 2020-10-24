#Say "Hello, World!" With Python
print("Hello, World!")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n>= 2 and n<= 5:
    print("Not Weird")
elif n>= 6 and n<=20:
    print("Weird")
else:
    print("Not Weird")

#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
        
#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 != 0:
        leap =False
    elif year %100 !=0:
        leap=True
    elif year % 400 == 0:
        leap=True
    return leap

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    values=[]
for i in range(x+1):
    for j in range (y+1):
        for k in range (z+1):
            if i+j+k != n:
                values.append([i,j,k])
print(values)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    LENGHT_MARKS=3
    mean=sum(student_marks[query_name])/LENGHT_MARKS
    print("%.2f" % mean)
    
#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

#String Split and Join
def split_and_join(line):
    # write your code here
    new=line.split(" ")
    new="-".join(new)
    return new

#What's Your Name?
def print_full_name(a, b):
    print("Hello",end=" ")
    print(a,b,end="")
    print("! You just delved into python.")

#sWAP cASE
def swap_case(s):
    nuova_stringa=s.swapcase()
    return nuova_stringa

#Mutations
def mutate_string(string, position, character):
    nuova_string=string[:position]+character+string[position+1:]
    return nuova_string

#Find a string
def count_substring(string, sub_string):
    conta=0
    for i in range (0,len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            conta=conta+1

    return conta

#String Validators
if __name__ == '__main__':
    stringa = input()
    alphanum=alfabeto=digits=lowcase=upcase=False
    for i in stringa:
        if i.isalnum():
            alphanum=True
        if i.isalpha():
            alfabeto=True
        if i.isdigit():
            digits=True
        if i.islower():
            lowcase=True
        if i.isupper():
            upcase=True
    print(alphanum)
    print(alfabeto)
    print(digits)
    print(lowcase)
    print(upcase)
    
#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
    #Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    #Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
    #Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
def wrap(string, max_width):
    risultato=textwrap.fill(string,max_width)
    return risultato

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = list((map(int, input().split())))
    massimo=max(arr)
    runner=min(arr)
    for i in range (0,len(arr)):
        if arr[i]>runner and arr[i]< massimo:
            runner=arr[i]
    print(runner)

#Introduction to Sets
def average(array):
    # your code goes here
        insieme=set(array)
        somma=sum(insieme)
        av=somma/len(insieme)
        return av
        
#Set .add()
n=int(input())
paese=set()
for i in range(n):
    paese.add(input())
diversi=len(paese)
print(diversi)

#Nested Lists
if __name__ == '__main__':
    name=[]
    score=[]
    n=int(input())
    for i in range(n):
        name.append(input())
        score.append(float(input()))
    min1=min(score)
    d=len(score)
    for i in range(d-1,-1,-1):
        if score[i]==min1:
            score.pop(i)
            name.pop(i)
    min2=min(score)
    name2=[]
    for i in range(len(score)):
        if score[i]==min2:
            name2.append(name[i])
    name2.sort()
    for i in range(len(name2)):
        print(name2[i])
        
#Capitalize!
def solve(s):
    for letter in s.split():
        s=s.replace(letter,letter.capitalize())
    return s

#Lists
if __name__ == '__main__':
    n=int(input())
    lista=[]
    for i in range(n):
        utente=input().split(" ")
        azione=utente[0]
        if azione=="append":
            lista.append(int(utente[1]))
        elif azione=="insert":
            lista.insert(int(utente[1]),int(utente[2]))
        elif azione=="remove":
            lista.remove(int(utente[1]))
        elif azione=="pop":
            if (len(lista)!=0):
                lista.pop()
        elif azione=="sort":
            lista.sort()
        elif azione=="print":
            print(lista)
        elif azione=="reverse":
            lista.reverse()

#String Formatting
def print_formatted(number):
    # your code goes here
    spazio = len(bin(number))-2
    for decimale in range(1, number+1):
        dec = str(decimale)
        ottale = oct(decimale)[2:]
        esadec = hex(decimale)[2:].upper()
        binaria = bin(decimale)[2:]
        print(dec.rjust(spazio), ottale.rjust(spazio), esadec.rjust(spazio), binaria.rjust(spazio))

#Designer Door Mat
n, m = map(int,input().split())
benv = "WELCOME"
for i in range(1, n, 2):
    schema = ".|." * i
    print(schema.center(m, "-"))
print(benv.center(m,"-"))
for i in range(n-2, -1, -2):
    schema = ".|." * i
    print(schema.center(m, "-"))
    
#Symmetric Difference
m = int(input())
insieme_m = set(map(int,input().split()))
n = int(input())
insieme_n = set(map(int,input().split()))
diff1 = insieme_m.difference(insieme_n)
diff2 = insieme_n.difference(insieme_m)
symm_diff = diff1.union(diff2)
for i in sorted(symm_diff):
    print(i)

#Set .union() Operation
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
print(len(eng_stud.union(fr_stud)))

#Set .intersection() Operation
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
print(len(eng_stud.intersection(fr_stud)))

#Set .difference() Operation
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
print(len(eng_stud.difference(fr_stud)))

#Set .symmetric_difference() Operation
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
intersezione = len(eng_stud.intersection(fr_stud))
unione = len(eng_stud.union(fr_stud))
print(unione - intersezione)

#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for comando in range(N):
    utente = input().split(" ")
    azione = utente[0]
    if azione == "remove":
        s.remove(int(utente[1]))
    elif azione == "discard":
        s.discard(int(utente[1]))
    elif azione == "pop":
        s.pop()
print(sum(s))

#Set Mutations
elem_A= int(input())
A = set(map(int, input().split()))
N = int(input())
for comando in range(N):
    utente = input().split(" ")
    insieme = set(map(int, input().split()))
    azione = utente[0]
    if azione == "intersection_update":
        A.intersection_update(insieme)
    elif azione == "update":
        A.update(insieme)
    elif azione == "symmetric_difference_update":
        A.symmetric_difference_update(insieme)
    elif azione == "difference_update":
        A.difference_update(insieme)
print(sum(A))

#Check Subset
T = int(input())
for i in range(T):
    elem_A= int(input())
    A = set(map(int, input().split()))
    elem_B= int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))

#Check Strict Superset
A = set(map(int, input().split()))
N = int(input())
l=[]
for i in range(N):
    insieme = set(map(int, input().split()))
    l.append(str(A.issuperset(insieme)))

if "False" in l:
    print("False")
else:
    print("True")

#No Idea!
n,m = map(int, input().split())
array = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())
l_array=list(array)
set_A = set(A)
set_B = set(B)
happiness = 0
for i in range(n):
    if l_array[i] in set_A:
        happiness = happiness + 1
    elif l_array[i] in set_B:
        happiness = happiness - 1
    else:
        happiness = happiness
print(happiness)

#Exceptions
T = int(input())
for i in range(T):
    try:
        a,b = map(int,input().split())
        risultato= a // b
        print(risultato)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
        
#collections.Counter()
X = int(input())
from collections import Counter
scarpe = Counter(map(int, input().split()))
guadagno = 0
N = int(input())
for i in range(N):
    taglia, costo = map(int, input().split())
    if taglia in scarpe and scarpe[taglia] > 0:
        scarpe[taglia] = scarpe[taglia] - 1
        guadagno = guadagno + costo
print(guadagno)

#Number Line Jumps
import math
import os
import random
import re
import sys
    # Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for i in range (10000):
        if x1 + v1 * i == x2 + v2 *i:
            esito = "YES"
            break
        else:
            esito = "NO"
    return esito
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Birthday Cake Candles
import math
import os
import random
import re
import sys
    #
    # Complete the 'birthdayCakeCandles' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER_ARRAY candles as parameter.
    #
def birthdayCakeCandles(candles):
    # Write your code here
    conta = 0
    altezza_max = max(candles)
    for i in range (len(candles)):
        if candles[i] == altezza_max:
            conta = conta + 1
    return conta
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Viral Advertising
import math
import os
import random
import re
import sys
    # Complete the viralAdvertising function below.
def viralAdvertising(n):
    people = 5
    like = 0
    SHARE = 3
    COSTANTE = 2
    for giorni in range(n):
        like = like + people // COSTANTE
        people = people // COSTANTE * SHARE
    return like
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1
import math
import os
import random
import re
import sys
    # Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    a=list(arr)
    d=a[-1]
    i = -2
    while d<a[i]:
        a[i+1]=a[i]
        for j in range(len(a)):
            print(a[j], end = " ")
        if i>-len(a):
            i = i -1
        else:
            break
        print()
    B=set(a)
    l=list(B)
    l.append(d)
    l.sort()
    for j in range(len(a)):
        print(l[j], end = " ")
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Map and Lambda Function
cube = lambda x: x**3
def fibonacci(n):
    # return a list of fibonacci numbers
    caso_0=[]
    caso_1=[0]
    l_fib=[0,1]
    for i in range(n-2):
        numero_succ = l_fib[i] + l_fib[i+1]
        l_fib.append(numero_succ)
    if n == 0:
        return caso_0
    elif n==1:
        return caso_1
    else:
        return l_fib

#Arrays
def arrays(arr):
    # complete this function
    # use numpy.array
    numpy_array = numpy.array(arr,float)
    numpy_array = numpy_array[::-1]
    return numpy_array

#Shape and Reshape
import numpy
interi = list(map(int,input().split()))
array = numpy.array(interi)
print(numpy.reshape(array,(3,3)))

#Transpose and Flatten
import numpy
N, M = list(map(int,input().split()))
lista = []
for i in range(N):
    lista.append(list(map(int,input().split())))
array=numpy.array(lista)
print(numpy.transpose(array))
print(array.flatten())

#Sum and Prod
import numpy
N, M = list(map(int,input().split()))
lista = []
for i in range(N):
    lista.append(list(map(int,input().split())))
my_array=numpy.array(lista)
somma = numpy.sum(my_array, axis = 0)
print(numpy.prod(somma))

#Min and Max
import numpy
N, M = list(map(int,input().split()))
lista = []
for i in range(N):
    lista.append(list(map(int,input().split())))
my_array=numpy.array(lista)
minimi = numpy.min(my_array, axis = 1)
print(numpy.max(minimi))

#Mean, Var, and Std
import numpy
N, M = list(map(int,input().split()))
lista = []
for i in range(N):
    lista.append(list(map(int,input().split())))
my_array=numpy.array(lista)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(numpy.std(my_array, axis = None))

#Array Mathematics
import numpy
N, M = list(map(int,input().split()))
A = []
B = []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
A_array = numpy.array(A, float)
B_array = numpy.array(B, float)
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A, B))
print(numpy.power(A, B))

#Floor, Ceil and Rint
import numpy
A=list(map(float, input().split()))
A_array = numpy.array(A, float)
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(A_array))
print(numpy.ceil(A_array))
print(numpy.rint(A_array))

#Eye and Identity
import numpy
N, M = map(int, input().split())
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(N,M,))

#Polynomials
import numpy
coeff = list(map(float, input().split()))
x = float(input())
valore = print(numpy.polyval(coeff,x))

#Inner and Outer
import numpy
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(numpy.inner(A, B))
print(numpy.outer(A, B))

#Linear Algebra
import numpy
N = int(input())
A=[]
for i in range(N):
    A.append(list(map(float, input().split())))
result = (numpy.linalg.det(A))
result = print(round(result, 2))

#Dot and Cross
import numpy
N=int(input())
A=[]
B=[]

for i in range(N):
    A.append(list(map(int, input().split())))
for i in range (N):
    B.append(list(map(int, input().split())))
A_array=numpy.array(A)
B_array=numpy.array(B)
print(numpy.dot(A,B))

#Zeros and Ones
import numpy
integers = list(map(int, input().split()))
print(numpy.zeros(integers, dtype = int))
print(numpy.ones(integers, dtype = int))

#The Captain's Room
K = int(input())
lista_persone = list(map(int, input().split()))
stanze = set(lista_persone)
capitano = sum(stanze)*K-sum(lista_persone)
print(capitano // (K-1))

#Re.split()
regex_pattern = r"[,.]"    # Do not delete 'r'.

#The Minion Game
def minion_game(string):
    # your code goes here
    vocali = "AEIOU"
    punteggio_1 = 0
    punteggio_2 = 0
    for i in range(len(string)):
            if string[i] in vocali:
                punteggio_1 = punteggio_1 + len(string) - i
            else:
                punteggio_2 = punteggio_2 + len(string) - i
    
    if punteggio_1 > punteggio_2:
        print("Kevin "+str(punteggio_1))
    elif punteggio_2 > punteggio_1:
        print("Stuart "+str(punteggio_2))
    else:
        print("Draw")
        
#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        new_substring=""
        for i in substring:
            if i not in new_substring:
                new_substring = new_substring + i
        print(new_substring)
