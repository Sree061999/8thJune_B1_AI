a = 5 ** 9
print(a)
b = 3 // 2
print(b)
c = 7 // 3
print(c)
d = 7/3
print(d)
e = 6 == 6
print(e)
a1 = 20
a1+= 30
a1%= 3
print(a1)
f = True * False
print(f)
g = True & False
print(g)
h = True and False
print(h)
i = ((6>3) and (7<4) or (18==3)) and (9>3)
print(i)
j = True is False
print(j)
#k = False in "False"
#print(k)
l = ((True == False) or (False > True)) and (False <= True)
print(l)
#3.nice to have it here
s1 = "Nice to have it"
s2 = "here"
print("{} {}".format(s1,s2))

#4.print hello from the list
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#5.Adding s1 and s2 in the list a
a[0] = s1
a[5] = s2
print(a)

#6.print black, white
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#7.Pangram
a = set(input())
s = set('abcdefghijklmnopqrstuvwxyz')
if s == a:
    print("String is pangram")
else:
    print("Sorry")

#8. n+nn+nnn
n = int(input("Enter a number:"))
e = '{0}+{0}{0}+{0}{0}{0}'.format(n)
print(e)

#9. sort sentence
sen = input("Enter a string")
sen = sorted(sen.split(","))
print(",".join(sen))



