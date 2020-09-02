
def merge(a,p,q,r):
    n1 = q - p + 1
    n2 = r - q
#    print(n1,n2)
    Left_array = [0] * (n1+1)
    Right_array = [0] * (n2+1)
    
    for i in range(n1):
        Left_array[i] = a[p+i]
    for j in range(n2):
        Right_array[j] = a[q+j+1]
        
    Left_array[n1] = float("infinity")
    Right_array[n2] = float("infinity")
    i = 0
    j = 0
    for k in range(p,r+1):
        if(Left_array[i] < Right_array[j] ):
            a[k] = Left_array[i]
            i += 1
        else:
            a[k] = Right_array[j]
            j += 1
    
    
def merge_sort(a,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)
        
        
if __name__ == "__main__":
    a = [5,4,3,2,1,5]
    merge_sort(a,0,5)
    print(a)
    
        
    
    
     