import random

def main():
    print("Hello")


my_string = "Hello, World!"
'''
print(my_string)
#[start:end:frequency]
print(my_string[0:5])
print(my_string[5:])
print(my_string[0:5:2])
print(my_string[::-1])
'''
my_list = [1,2,3,4,5,6,7,8]

print(my_list)
print(my_list[2])
print(my_list[0:2])
print(my_list[2::2])
print(my_list[::-1])

main()

print(5 // 2)
print(5 % 2)
print(int(5.5))
print(float("5.5"))
print(str(15))
print(str(15) + str(5))

print(random.choice(my_list))


for i in my_list:
    print(i)

if my_list[1] == 2:
    print("hi")
elif my_list[2] == 3:
    print("hello")
else:
    print("goodbye")
    # this is a comment
    a = 1 + 2
    if a == 5:
        print(a)

position = [(1,2),(3,4),(5,6)]

latlong = (54.3,33.2)


for x,y in position:
    for x2, y2 in positon:
        print("x: " + str(x))
        print("y: " + str(y))


print("No longer in the else statement")



