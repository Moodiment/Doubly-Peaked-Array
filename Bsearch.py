from random import randrange, choice

def binarySearch(array, min, max):
    mid = int(min + ((max - min) / 2))
    if array[mid-1] <= array[mid] and array[mid] >= array[mid+1]:
        return array[mid]
    elif array[mid-1] > array[mid]:
        return binarySearch(array, min, mid - 1)
    else:
        return binarySearch(array, mid + 1, max)


def findValley(array,min,max):
    print(str(min)+" "+str(max))
    input()
    if (min > max): raise IndexError
    mid = int(min + ((max - min) / 2))
    try:
        if array[mid-1] >= array[mid] and array[mid] <= array[mid+1]:
            x = binarySearch(array,mid + 1,len(array)-1)
            z = binarySearch(array,0,mid-1)
            if (x>z):
                return x
            else:
                return z
        elif array[mid-1] < array[mid]:
            return findValley(array, min, mid - 1)
        else:
            return findValley(array, mid + 1, max)

    except IndexError:
        print("Out of range.")
        return findValley(arr,0,choice(arr))
        return -1

if __name__ == "__main__":
    arr = [1,2,4,5,6,7,8,9,10,6,5,4,2,4,5,7,8,12,3,2,1]
    if((print(findValley(arr,0,len(arr)-1)) is not -1)):
        print("OK.")
