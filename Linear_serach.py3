def linear(a,key):
    for i in range(len(a)):
        if (a[i] == key):
            print("Found at index ",i)
            flag = 1
    if(flag == 0):
        print("Record not present")
        
if __name__ == "__main__":
    a = [1,2,3,4,5]
    linear(a,4)
    