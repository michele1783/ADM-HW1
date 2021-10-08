#1.Introduction

#Say "Hello, World!" With Python
if __name__ == '__main__':
    print ("Hello, World!")

#Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0 and (n>=2 and n<=5 or n > 20):
        print("Not Weird")
    elif n % 2 != 0 or (n % 2 == 0 and n >=6 and n<=20):
        print("Weird")
        
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
    for i in range(0,n):
        print(i**2)
        
#Write a function
def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
year = int(input())
print(is_leap(year))

#Print function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')
        
#2. Basic Data Types

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

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    print(arr[-2])

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
    
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lista = student_marks[query_name]
    media = sum(lista)/len(lista)
    print("%.2f" % media)
    
#Lists
if __name__ == '__main__':
    n = int(input())
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

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#3.String

#sWAP cASE
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    print("Hello %s %s! You just delved into python." % (first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
##Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
##Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
##Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
##Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
##Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
def wrap(string, max_width):
    risultato=textwrap.fill(string,max_width)
    return risultato
    
#Find a string
def count_substring(string, sub_string):
    c = 0
    for i in range(0,len(string)+1-len(sub_string)):
        if sub_string == string[i:i+len(sub_string)]:
            c = c + 1
    return c
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#String Validators
if __name__ == '__main__':
    s = input()
    e = 0
    for i in s:
        if True==i.isalnum():
            e = 1
    if e != 0:
        print(True)
    else:
        print(False)
    
    
    d = 0
    for i in s:
        if True==i.isalpha():
            d = 1
    if d != 0:
        print(True)
    else:
        print(False)
    
    b = 0
    for i in s:
        if True==i.isdigit():
            b = 1
    if b != 0:
        print(True)
    else:
        print(False)
    
    a = 0
    for i in s:
        if True==i.islower():
            a = 1
    if a != 0:
        print(True)
    else:
        print(False)
   
    
    c = 0
    for i in s:
        if True==i.isupper():
            c = 1
    if c != 0:
        print(True)
    else:
        print(False)

#String Formatting
def print_formatted(number):
    # your code goes here
    spazio = len(bin(number)[2:])
    for decimale in range(1, number+1):
        dec = str(decimale)
        ottale = oct(decimale)[2:]
        esadec = hex(decimale)[2:].upper()
        binaria = bin(decimale)[2:]
        print(dec.rjust(spazio), ottale.rjust(spazio), esadec.rjust(spazio), binaria.rjust(spazio))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Designer Door Mat
## Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
benv = "WELCOME"
for i in range(1, n, 2):
    schema = ".|." * i
    print(schema.center(m, "-"))
print(benv.center(m,"-"))
for i in range(n-2, -1, -2):
    schema = ".|." * i
    print(schema.center(m, "-"))
    
#Capitalize
def solve(s):
    for letter in s.split():
        s = s.replace(letter,letter.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

#Minion Game
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
if __name__ == '__main__':
    s = input()
    minion_game(s)

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
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Alphabet Rangoli
import string
def print_rangoli(size):
    alfabeto = string.ascii_lowercase
    lista = []
    for i in range(n):
        riga = "-".join(alfabeto[i:n])
        lista.append((riga[::-1]+riga[1:]).center(4*n-3, "-"))
    print('\n'.join(lista[:0:-1]+lista))

#4.Numpy

#Arrays
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    result = numpy.array(arr,float)
    result = numpy.flip(result)
    return result

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

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

#Zeros and Ones
import numpy
integers = list(map(int, input().split()))
print(numpy.zeros(integers, dtype = int))
print(numpy.ones(integers, dtype = int))

#Eye and Identity
import numpy
N, M = map(int, input().split())
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(N,M,))

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
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),11))

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

#Inner and Outer
import numpy
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(numpy.inner(A, B))
print(numpy.outer(A, B))

#Polynomials
import numpy
coeff = list(map(float, input().split()))
x = float(input())
valore = print(numpy.polyval(coeff,x))

#Linear Algebra
import numpy
N = int(input())
A=[]
for i in range(N):
    A.append(list(map(float, input().split())))
result = (numpy.linalg.det(A))
result = print(round(result, 2))

#Concatenate
import numpy
a, b, c = map(int,input().split())
array_1 = numpy.array([input().split() for i in range(a)],int)
array_2 = numpy.array([input().split() for i in range(b)],int)
print(numpy.concatenate((array_1, array_2), axis = 0))

#5.Sets

#Introduction to Sets
def average(array):
    # your code goes here
        insieme=set(array)
        somma=sum(insieme)
        av=somma/len(insieme)
        return av

#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
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

#Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
paese=set()
for i in range(n):
    paese.add(input())
diversi=len(paese)
print(diversi)

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

#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
print(len(eng_stud.union(fr_stud)))

#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
print(len(eng_stud.intersection(fr_stud)))

#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
print(len(eng_stud.difference(fr_stud)))

#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
numero_eng = int(input())
eng_stud = set(map(int, input().split()))
numero_fr = int(input())
fr_stud = set(map(int, input().split()))
intersezione = len(eng_stud.intersection(fr_stud))
unione = len(eng_stud.union(fr_stud))
print(unione - intersezione)

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
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

#The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
lista_persone = list(map(int, input().split()))
stanze = set(lista_persone)
capitano = sum(stanze)*K-sum(lista_persone)
print(capitano // (K-1))

#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
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

#6.Date and Time

#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
input_data = input().split()
mese = int(input_data[0])
giorno = int(input_data[1])
anno = int(input_data[2])
data = calendar.weekday(anno, mese, giorno)
if data == 0:
    print("MONDAY")
elif data == 1:
    print("TUESDAY")
elif data == 2:
    print("WEDNESDAY")
elif data == 3:
    print("THURSDAY")
elif data == 4:
    print("FRIDAY")
elif data == 5:
    print("SATURDAY")
elif data == 6:
    print("SUNDAY")

#Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(tempo_1, tempo_2):
    formato= '%a %d %b %Y %H:%M:%S %z'
    tempo_1 = datetime.strptime(tempo_1, formato)
    tempo_2 = datetime.strptime(tempo_2, formato)
    differenza = abs((tempo_1-tempo_2).total_seconds())
    return str(int(differenza))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


#7.Exceptions

#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
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


#8.Built-ins

#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
voti = []
for subject in range(X):
    voti = voti + [map(float, input().split())]
    
for student_marks in zip(*voti):
    print(sum(student_marks)/X)


#9. Python Functionals

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
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
#10. Collections

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
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

#Collections.OrderedDict()
dizionario=dict()
for i in range(int(input())):
    nome, prezzo=input().rsplit(' ',1)
    if nome in dizionario:
        dizionario[nome]=int(dizionario[nome])+int(prezzo)
    else:
        dizionario[nome]= prezzo
for nome, prezzo in dizionario.items():
    print(nome, prezzo)
    
#Collections.namedtuple()
from collections import namedtuple
N = int(input())
fields = input().split()
totale = 0
for i in range(N):
    studenti = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = studenti(MARKS, CLASS, NAME, ID)
    totale = totale + int(student.MARKS)
print('{:.2f}'.format(totale / N))

#11.Regex and Parsing

#Re.split()
regex_pattern = r"[,.]"    # Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))

#Validating phone numbers
import re
N = int(input())
for i in range(N):
    number = input()
    output = re.findall(r"^[789]\d{9}$",number)
    if(len(output)==1):
        print("YES")
    else:
        print("NO")

#Group(), Groups() & Groupdict()
import re
stringa = r"([a-zA-Z0-9])\1+"
substr = re.search(stringa ,input())
if substr:
    print(substr.group(1))
else:
    print(-1)

#Re.findall() & Re.finditer()
import re
vocali = 'aeiou'
consonanti = 'wqrtspyfdghkjlcxzvbmn'
match = re.findall(r'(?<=[' + consonanti + '])([' + vocali + ']{2,})(?=[' + consonanti + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))

#Detect Floating Point Number
from re import match, compile
decimale = compile('^[-+]?[0-9]*\.[0-9]+$')
for i in range(int(input())):
    print(bool(decimale.match(input())))
    
#Validating UID
import re
for i in range(int(input())):
    uid = input()
    uid = "".join(sorted(uid))
    if len(uid) == 10 and (re.search(r"\d{3}",uid) and re.search(r"[A-Z]{2}",uid) and not re.search(r"(\w)\1",uid) and not re.search(r"[^A-Za-z0-9]",uid)):
        print("Valid")
    else:
        print("Invalid")

#12.Closure and Decorators

#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        f(['+91 ' + numero[-10:-5] + ' ' + numero[-5:] for numero in l])
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


#Algorithms

#Birthday Cake Candles

#!/bin/python3
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

#Number Line Jumps

#!/bin/python3
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

#Viral Advertising

#!/bin/python3
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

#Recursive Digit Sum

#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    def somma(numero):
        if numero < 10:
            return numero
        s = sum(int(i) for i in str(numero))
        return somma(s)
    x = somma(int(n))
    return somma(x*k)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

#Insertion Sort - Part 1 (22.5/30 points so it is not totally correct!)

#!/bin/python3
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
