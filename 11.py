# # # exceptions  - events that intrupts the execution of our program 


# # # try:
# # #     a = int(input("enter your number : - "))
# # #     b = 0
# # #     print(a/b)
# # # except ZeroDivisionError:
# # #     print("you cannot divide a number with zero")
# # # except ValueError:
# # #     print("check your values")
# # # except TypeError:
# # #     print("check types")
# # # finally:
# # #     print("this will always execute !!!!!!!")
# # # # except Exception as eroor:
# # # #     print("an error occured",eroor)
# # # print("mohan das @!!@@#@$@!$@#$#@$#")


# # # # ZeroDivisionError 
# # # # ValueError
# # # # TypeError

# # # AssertionError 
# # # assert

# # # age = 4
# # # assert age > 18 , "age have to be  greater"
# # # raise(IndentationError("my name is not hari"))

# # # class Myerror(Exception):
# # #     pass

# # # name = "mohan"
# # # if name != "hari":
# # #     raise Myerror("name should be hari")

# # # a = [1,2,3,4,5,3,2,1,4,1,1,1,1,1,6,7,8,5,6,7,9,10]
# # # b = []
# # # for i in a:
# # #     if i not in b :
# # #         b.append(i)
# # # print(b)

# # # a = 3 
# # # b = 7 
# # # c = a
# # # a = b
# # # b = c
# # # print(a)
# # # print(b)

# # # without using a third varible 

# # a = 5 
# # b = 7 

# # a = a + b # 12
# # b = a - b  # 5
# # a = a - b   # 7 

# # # a,b = b,a
# # # print(a)
# # # print(b)



# # split the list midways into 2 lists 

# # a = [11,12,13,14,15,16,17,18,19,20,21]
# # b = []
# # c = []
# # mid = len(a)//2
# # for i in range(len(a)):
# #     # print(i,a[i])
# #     if i <= mid :
# #         b.append(a[i])
# #     else:
# #         c.append(a[i])

# # print(b)
# # print(c)



# # [11,12,13,14,15,16]
# # [17,18,19,20,21]
# # find largest and smallest numer from a list 
# a = [100,-6,589,10,2,3,-999,18,23,9]
# # without using
# print(max(a))
# print(min(a))

# # largest num 
# # smallest num 


for i in range(6,10):
    if i == 5:
        print('its 5 ')
        break
else:
    print('nmo')