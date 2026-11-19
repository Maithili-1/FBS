# 1st way :- 
# Merge two sorted parts of the list: start..mid and mid+1..end
def merge(li, start, mid, end):
    left = start
    right = mid + 1
    result = []

    # Compare the front items of both parts and take the smaller one
    while left <= mid and right <= end:
        if li[left] <= li[right]:
            result.append(li[left])
            left += 1
        else:
            result.append(li[right])
            right += 1

    # Copy whatever is left in the left part
    while left <= mid:
        result.append(li[left])
        left += 1

    # Copy whatever is left in the right part
    while right <= end:
        result.append(li[right])
        right += 1

    # Copy the merged result back into the original list
    for k in range(len(result)):
        li[start + k] = result[k]


# Divide the list into halves, sort each half, then merge them
def merge_sort(li, start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    merge_sort(li, start, mid)
    merge_sort(li, mid + 1, end)

    merge(li, start, mid, end)

li = [3, 1, 12, 9, 2]
print("Before:", li)
merge_sort(li, 0, len(li) - 1)
print("After:", li)



# 2nd way :-
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


li = [38, 27, 43, 3, 9, 82, 10]
print("Before:", li)
print("After: ", merge_sort(li))