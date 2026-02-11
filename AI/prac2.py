# print("Hello World")


# a, b = 10, 3
# sum = a + b
# print("Sum: ", sum)


# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print("Sum: ", x+y)


# num = (int(input("Enter a number: ")))
# if num % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")


# p = int(input("Enter first number: "))
# q = int(input("Enter second number: "))
# r = int(input("Enter third number: "))
# if p>q and p>r:
#     print("Greatest number is",p)
# elif q>p and q>r:
#     print("Greatest number is",q)
# else:
#     print("Greatest number is",r)


# sum = 0
# for i in range(1, 11):
#     sum += i
# print("Sum of first 10 numbers: ", sum)


# n = int(input("Enter a number: "))
# fact = 1
# for i in range(2, n+1):
#     fact *= i
# print("Factorial: ",fact)


# n = int(input("Enter a number: "))
# rev = 0
# while n >= 1:
#     rev = rev * 10 + n % 10
#     n // 10
# print("Reverse: ", rev)


# sub=int(input("Enter the number of subjects: "))
# subs=[]
# for i in range(0, sub):
#     s={}
#     print("\nSubject ", i+1)
#     s['name']=input("Enter name: ")
#     s['it1']=float(input("Enter IT 1 marks: "))
#     s['it2']=float(input("Enter IT 2  marks: "))
#     s['it3']=float(input("Enter IT 3 marks: "))
#     all = s['it1'] + s['it2'] + s['it3']
#     all -= min(s['it1'], s['it2'], s['it3'])
#     s['best'] = all
#     subs.append(s)
# t = 0
# print("\nReport Card\nSubject Name\tIT 1\tIT2\tIT3\tIT Average")
# for i in subs:
#     t += i['best']
#     print(i['name'],"\t\t",i['it1'],"\t",i['it2'],"\t",i['it3'],"\t",i['best'])
# print("\nTotal: ", t)


# def a(n1, n2):
#     print(n1 + n2)

# def s(n1, n2):
#     print(n1 - n2)

# def m(n1, n2):
#     print(n1 * n2)

# def d(n1, n2):
#     print(n1 / n2)

# def m(n1, n2):
#     print(n1 % n2)

# def fd(n1, n2):
#     print(n1 // n2)

# n1=float(input("Enter first number: "))
# n2=float(input("Enter second number: "))
# print("\nMenu\n1. Addition\t2. Subtraction\t3.Multiplication\t4. Division\t5. Modulus\t6. Floor Division\n")
# c=int(input("Enter your choice: "))
# match c:
#     case 1:
#         a(n1, n2)
#     case 2:
#         s(n1, n2)
#     case 3:
#         m(n1, n2)
#     case 4:
#         d(n1, n2)
#     case 5:
#         m(n1, n2)
#     case 6:
#         fd(n1, n2)


# s = "Goa College of Engineering"
# c, e = s[4:11], s[14:]
# print("Original:",s,"\nSliced:",c,"",e)


# st=input("Enter string 1: ")
# st2=input("Enter string 2: ")
# print("Length of string 1: ",len(st))
# print(st + st2)


# v = "aeiouAEIOU"
# inp=input("Enter a string: ")
# count_v, count_c = 0, 0
# for c in inp:
#     if c in v:
#         count_v += 1
#     else:
#         count_c += 1

# print("Number of vowels in ",inp,"=",count_v,"\nNumber of consonants in",inp,"=",count_c)


# stck=[]
# c = 0
# while c is not 5:
#     c=int(input("1. Push\t2. Pop\t3. Peek\t4. Display\t5. Exit\nEnter your choice: "))
#     match c:
#         case 1:
#             i=int(input("Enter number: "))
#             stck.append(i)
#         case 2:
#             if(len(stck) == 0):
#                 print("Stack Empty")
#             else:
#                 stck.pop()
#         case 3:
#             print(stck[-1])
#         case 4:
#             for j in stck:
#                 print(j, end=" ")
#             print()


# q=[]
# c = 0
# while c is not 5:
#     c=int(input("1. Enqueue\t2. Dequeue\t3. Peek\t4. Display\t5. Exit\nEnter your choice: "))
#     match c:
#         case 1:
#             i=int(input("Enter number: "))
#             q.append(i)
#         case 2:
#             if(len(q) == 0):
#                 print("Queue Empty")
#             else:
#                 q.pop(0)
#         case 3:
#             print(q[0])
#         case 4:
#             for j in q:
#                 print(j, end=" ")
#             print()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def display(head):
#     current = head
#     while current:
#         print(current.data, end=" -> ")
#         current = current.next
#     print("null")

# def insert_back(head, data):
#     newNode = Node(data)
#     if head is None:
#         return newNode
#     current = head
#     while current.next:
#         current = current.next
#     current.next = newNode
#     return head

# def delete_value(head, value):
#     if head is None:
#         return None
#     if head.data == value:
#         return head.next
#     current = head
#     while current.next and current.next.data != value:
#         current = current.next
#     if current.next:
#         current.next = current.next.next
#     return head

# head = None
# while True:
#     op = int(input("\nEnter 1 to add, 2 to remove, 3 to exit: "))
#     if op == 1:
#         n = int(input("Enter element to add: "))
#         head = insert_back(head, n)
#         display(head)
#     elif op == 2:
#         n = int(input("Enter element to delete: "))
#         head = delete_value(head, n)
#         display(head)
#     elif op == 3:
#         break