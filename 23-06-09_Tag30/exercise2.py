
print("======= TASK 2 ========")
# change the merge_sort so that you can sort by age.


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["age"] <= right[j]["age"]:   # hier vergleichen wir und zwar mit dem key: age!
            result.append(left[i])              # hier fügenm wir die dicts komplett hinzu 
            i += 1
        else:
            result.append(right[j])
            j += 1


    result += left[i:]
    result += right[j:]

    return result
    



def merge_sort(lst):
    # exit condition: if the length of the list is 1 or less, return the list
    if len(lst) <= 1:
        return lst

    # divide the list into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    #  recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)
    print('left: ', left)
    print('right: ', right)

    return merge(left, right)





dictionaries = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "Houston"},
    {"name": "Emma", "age": 27, "city": "San Francisco"},
    {"name": "Frank", "age": 32, "city": "Seattle"},
    {"name": "Grace", "age": 29, "city": "Boston"},
    {"name": "Henry", "age": 31, "city": "Dallas"},
    {"name": "Ivy", "age": 26, "city": "Miami"},
    {"name": "Jack", "age": 33, "city": "Denver"}
]




print(merge_sort(dictionaries))


