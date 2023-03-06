class Solution:
    def __init__(self, arr, k) -> int:
        count_missing_ints = 0 
        missing_number_array = []
        if arr[0] > 1:
            for z in range(1, arr[0]):
                missing_number_array.append(z)
                count_missing_ints = count_missing_ints + 1
        for i in range(0, len(arr)-1):
            current_int = arr[i]
            next_int = arr[i+1]
            if (next_int - current_int) > 1:
                difference = next_int - current_int
                print(difference)
                count_missing_ints  = count_missing_ints + difference
                for j in range(1, difference):
                    missing_number_array.append(current_int+j)
        print(count_missing_ints)
        if count_missing_ints < k:
            last_int = arr[len(arr)-1]
            for i in range(1, k-count_missing_ints+1):
                missing_number_array.append(last_int+i)
        for i in range(0, len(missing_number_array)):
            if i == k - 1:
                print(missing_number_array[i])
        print(missing_number_array)




if __name__ == '__main__':
    Solution([1,13,18], 17)