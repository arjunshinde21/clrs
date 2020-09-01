def insertion(a):
    for j in range(1,len(a)):
        i = j - 1
        key = a[j]
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
if __name__ == "__main__":
    a = [ 5,6,3,6,8]
    print("Before sorting")
    print(a)
    insertion(a)
    print("After sorting")
    print(a)
            
        