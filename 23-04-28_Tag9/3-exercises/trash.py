
# a = input("Type Numbers (seperated by ,): ")                       
# li = a.split(",")
# if ',' not in a:
#     raise ValueError("You forgot the damn ,")
# for i in range(len(li)):
#     li[i] = int(li[i])    # li ist liste vonm integern
# m = sum(li)/len(li)
# print(m)




while True:
    try:
        nums = input("Enter a list of integers, separated by commas: ").split(',')
        nums = [int(num) for num in nums]  #use for loop instead
        avg = sum(nums) / len(nums)
        print(f"Average: {avg}")
    except ValueError:
        print("Error: Invalid input. Please enter a list of integers, separated by commas.")
    else:
        break

