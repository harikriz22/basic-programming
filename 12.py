# # # # # # file handling

# # # # # # read

# # # # # # file1 = open("hello.txt","r")
# # # # # # print(file1.read())
# # # # # # file1.close()

# # # # # # overwrite

# # # # # # file2 = open("bye.txt","w")
# # # # # # file2.write("my name is mohan")
# # # # # # file2.close()

# # # # # # append

# # # # # # file3 = open("bye.txt","a")
# # # # # # # file3.write("hello\n")
# # # # # # for i in range(1,1001):
# # # # # #     file3.write(f"hello das {i}\n")
# # # # # # file3.close()

# # # # # # with open("bye.txt","a") as f :
# # # # # #     for i in range(1,1001):
# # # # # #         f.write(f"hello das {i}\n")


# # # # # # import os
# # # # # # make directory
# # # # # # os.mkdir("hello")
# # # # # # remove a file
# # # # # # os.remove("bye.txt")

# # # # # # rename a file
# # # # # # os.rename("hello.txt","data.txt")

# # # # # # file_path = "C:\\Users\\harik\\OneDrive\\Desktop\\basic.txt"

# # # # # # if os.path.exists(file_path):
# # # # # #     print("path exits")
# # # # # #     with open(file_path,"r") as f:
# # # # # #         print(f.read())
# # # # # # else:
# # # # # #     print("no such path")


# # # # # # check if a number is prime or not
# # # # # # print chessboard pattern


# # # # # num = int(input("enter your number : -"))
# # # # # prime = True
# # # # # if num == 1:
# # # # #     prime = False
# # # # # else:
# # # # #     for i in range(2, num):
# # # # #         if num % i == 0:
# # # # #             prime = False
# # # # #             print("not a prime")
# # # # #             break
# # # # #     else:
# # # # #         print("prime")

# # # # # # if prime == False:
# # # # # #     print("not a prime number")
# # # # # # else:
# # # # # #     print("prime")

# # # # # data = "aabbccddeeffaabbcceeddff" 
# # # # # result = {"a":1}
# # # # # for i in data:
# # # # #     if i not in result:
# # # # #         result[i] = 1
# # # # #     else:
# # # # #         result[] = result[i]+1

# # # # # print(result)

# # # # # import os 

# # # # # # os.mkdir("govind")
# # # # # # os.rename("10.py","ten.py")
# # # # # os.remove("data.txt")

# # # # # a = {1,2,3,4,5,1,2,3,4,5}
# # # # # # unordered 
# # # # # print(a)
# # # # # b = [1,2,3,4,5,6]
# # # # # c = (4,5,6,7,8,1,2,3,4,7)
# # # # # c[3] = 10
# # # # # immutable 
# # # # # d = {1:"1",2:"3"}

# # # # # turnery operator 

# # # # # if 5>7:
# # # # #     print("hello")
# # # # # else:
# # # # #     print("bye")

# # # # # print("hello") if 5>7 else print("bye")

# # # # # dict key value paired datatype 

# # # # # data = {"name":"mohan","age":45,"location":"kochi"}

# # # # # dict["key"] = "val"

# # # # # str immutable 
# # # # # list 

# # # # a = "mohan"
# # # # a[0] = "l"

# # # # recursion to recur to go back 


# # # # def nsum(0):
# # # #     if 0 == 0:
# # # #         return 0
# # # #     return 9+nsum(8)

# # # # print(nsum(10))
# # # # # nsum(n) = n + nsum(n-1)
# # # # nsum(10) = 10 + 9+8 +7+6+5+4+3+1+0

# # # # print chessboard pattern
# # # # W B W B W B W B 
# # # # B W B W B W B W
# # # # W B W B W B W B 
# # # # B W B W B W B W
# # # # W B W B W B W B 
# # # # B W B W B W B W
# # # # W B W B W B W B 
# # # # B W B W B W B W

# # # for i in range(1,6):
# # #     for j in range(1,6):
# # #         print(i,j)

# # # 1    1 2 3 4 5 
# # # 2    1 2 3 4 5
# # # 3    1 2 3 4 5
# # # 4    1 2 3 4 5 
# # # 5    1 2 3 4 5 

# # # map()
# # # filter()
# # # [1,.........,100]

# # # map() maps every elemts in a itreable to a function 
# # a= [1,2,3,4,5,6,7,8,9,10]
# # def even(num):
# #     if num % 2 == 0 :
# #         return num
# # result = list(filter(even,a))
# # print(result)

# N = int(input("enter your number : - "))
# fact = 1
# for i in range(1,N+1):
#     fact = fact * i

# print(fact)



# # reverse of a string without using [::-1]
# # color = "red"