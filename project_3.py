# Individual Project №3
# Developer: Moiseenko Victoria
# The idea: find the number of different words that can be composed by rearranging the letters of the given word with
# symbols from a to e.

word = str(input())  # Type a word in lower case a-e only
length = len(word)

ka = 0
kb = 0
kc = 0
kd = 0
ke = 0

for a in range(length):  # Counting the num of a letters
    letter = word[a]
    if letter == 'a':
        ka += 1

fa = 1
for a in range(1, ka + 1):
    fa *= a

for b in range(length):  # Counting the num of b letters
    letter = word[b]
    if letter == 'b':
        kb += 1

fb = 1
for b in range(1, kb + 1):
    fb *= b

for c in range(length):  # Counting the num of c letters
    letter = word[c]
    if letter == 'c':
        kc += 1

fc = 1
for c in range(1, kc + 1):
    fc *= c

for d in range(length):  # Counting the num of d letters
    letter = word[d]
    if letter == 'd':
        kd += 1

fd = 1
for d in range(1, kd + 1):
    fd *= d

for e in range(length):  # Counting the num of e letters
    letter = word[e]
    if letter == 'e':
        ke += 1

fe = 1
for e in range(1, ke + 1):
    fe *= e

length = len(word)  # Counting the factorial of total num of outcomes
factorial = 1

for i in range(1, length + 1):
    factorial *= i

denominator = 1

if ka != 0:
    denominator *= fa
if kb != 0:
    denominator *= fb
if kc != 0:
    denominator *= fc
if kd != 0:
    denominator *= fd
if ke != 0:
    denominator *= fe

if denominator == 1:
    if  ka != 0 or kb != 0 or kc != 0 or kd != 0 or ke != 0:
        print(factorial)
    else:
        print(1)
else:
    p = factorial / denominator  # The num of different words
    print(p)