a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]
def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    for i in arr:
        if type(i) == str:
            x = int(i)
            if(x<0):
                print("'" + str(0-x) +"'", end=" ")
            else:
                print("'" + str(x) +"'", end=" ")
        else:
            if(i<0):
                print(0-i,end=" ")
            else:
                print(i,end=" ")
    # TODO add new code here to print the desired result
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
