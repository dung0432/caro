def pos(x):
    if (x == 1): 
        u = 1
        v = 1
    elif (x == 2):
        u = 1
        v = 2
    elif (x == 3):
        u = 1
        v = 3
    elif (x == 4):
        u = 2
        v = 1
    elif (x == 5):
        u = 2
        v = 2
    elif (x == 6):
        u = 2
        v = 3
    elif (x == 7):
        u = 3
        v = 1
    elif (x == 8):
        u = 3
        v = 2
    elif (x == 9):
        u = 3
        v = 3
    else: 
        u = 0
        v = 0
    return u, v

def computer_cell(x, y):
    if (x== 1 and y == 1): return 1
    elif (x== 2 and y == 2): return 5
    elif (x== 3 and y == 3): return 9
    elif (x== 1 and y == 2): return 2
    elif (x == 1 and y == 3): return 3
    elif (x == 2 and y == 1): return 4
    elif (x == 2 and y == 3): return 6
    elif (x == 3 and y == 1): return 7
    else: return 8

def ghi():
    print("-------------------------------------------------------------------")
    print("|         ", arr[1][1], "         |         ", arr[1][2], "         |         ", arr[1][3],"         |")
    print("|-----------------------------------------------------------------|")
    print("|         ", arr[2][1], "         |         ", arr[2][2], "         |         ", arr[2][3],"         |")
    print("|-----------------------------------------------------------------|")
    print("|         ", arr[3][1], "         |         ", arr[3][2], "         |         ", arr[3][3],"         |")
    print("-------------------------------------------------------------------")


def check():
    if (arr[1][1] == value and arr[1][1] == arr[1][2] and arr[1][1] == arr[1][3]):
        return 1
    elif (arr[1][1] == computer_value and arr[1][1] == arr[1][2] and arr[1][1] == arr[1][3]):
        return 0
    elif (arr[2][1] == value and arr[2][1] == arr[2][2] and arr[2][1] == arr[2][3]):
        return 1
    elif (arr[2][1] == computer_value and arr[2][1] == arr[2][2] and arr[2][1] == arr[2][3]):
        return 0
    elif (arr[3][1] == value and arr[3][1] == arr[3][2] and arr[3][1] == arr[3][3]):
        return 1
    elif (arr[3][1] == computer_value and arr[3][1] == arr[3][2] and arr[3][1] == arr[3][3]):
        return 0
    elif (arr[1][1] == value and arr[1][1] == arr[2][1] and arr[1][1] == arr[3][1]):
        return 1
    elif (arr[1][1] == computer_value and arr[1][1] == arr[2][1] and arr[1][1] == arr[3][1]):
        return 0
    elif (arr[1][2] == value and arr[1][2] == arr[2][2] and arr[1][1] == arr[3][2]):
        return 1
    elif (arr[1][2] == computer_value and arr[1][2] == arr[2][2] and arr[1][2] == arr[3][2]):
        return 0
    elif (arr[1][3] == value and arr[1][3] == arr[2][3] and arr[1][3] == arr[3][3]):
        return 1
    elif (arr[1][3] == computer_value and arr[1][3] == arr[2][3] and arr[1][3] == arr[3][3]):
        return 0
    elif (arr[1][1] == value and arr[1][1] == arr[2][2] and arr[1][1] == arr[3][3]):
        return 1
    elif (arr[1][1] == computer_value and arr[1][1] == arr[2][2] and arr[1][1] == arr[3][3]):
        return 0
    elif (arr[1][3] == value and arr[1][3] == arr[2][2] and arr[1][3] == arr[3][1]):
        return 1
    elif (arr[1][3] == computer_value and arr[1][3] == arr[2][2] and arr[1][3] == arr[3][1]):
        return 0
    else: return 2

def check_cell(x):
    u, v = pos(x)
    if (bol[u][v] != 0 or u < 1 or u > 3 or v < 0 or v > 3):
        return False
    else: return True

def check_arr():
    if (bol[1][1] == 1 and bol[1][2] == 1 and bol[1][3] == 1 and bol[2][1] == 1 and bol[2][2] == 1 and bol[2][3] == 1 and bol[3][1] == 1 and bol[3][2] == 1 and bol[3][3] == 1):
            return True
    else: return False

def xuli():
   import random
   b = False
   hoa = True

   while(b == False):
       s_cell = int(input("Chon o can dien: "))
       while (check_cell(s_cell) == False):
           print("O da duoc dien hoac o khong ton tai")
           s_cell = int(input("Chon o can dien: "))
       xx, yy = pos(s_cell)
       arr[xx][yy] = value
       bol[xx][yy] = 1
       u = 0
       v = 0

       while (bol[u][v] != 1 and check_arr() == False):
            u = random.randint(1, 3)
            v = random.randint(1, 3)
           
            while (bol[u][v] == 1):
                u = random.randint(1, 3)
                v = random.randint(1, 3)
            arr[u][v] = computer_value
            bol[u][v] = 1
            print("May danh o ", computer_cell(u, v))    
                         
       ghi()

       if (check() == 0 or check() == 1):
           if (check() == 1):
               print("Player wins")
               b = True
               hoa = False
           else: 
               print("Computer wins")
               b = True
               hoa = False

       if (bol[1][1] == 1 and bol[1][2] == 1 and bol[1][3] == 1 and bol[2][1] == 1 and bol[2][2] == 1 and bol[2][3] == 1 and bol[3][1] == 1 and bol[3][2] == 1 and bol[3][3] == 1):
            b = True 

   if (hoa == True):
       print("HOA")
        

arr = [[0, 0, 0, 0],
       [0, 1, 2, 3],
       [0, 4, 5, 6],
       [0, 7, 8, 9]]
bol = [[0, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
val = int(input("Chon X/O nhan 0/1: "))

if (val == 0): 
    value = "X"
    computer_value = "O"
else: 
    value = "O"
    computer_value = "X"

ghi()

xuli()