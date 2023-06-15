**Today**
- merge sort
- LIFO and FIFO behavior
- Deques


# Merge Sort
- is a **devide and conquer** sorting algorithm
- recursivly dividing an input arraay into smaller subarrays
- sorting those subarrays
- then merging them back together

Works as follows:
- divide the input into 2 halves
- recursivley sort eatch using merge sort
- merge 2 sorted halves into single ouput array
- the merge operation is key step of the algo
- it works comparing 1st element of eatch subarray and selectig the smaller one to add to output array
- this process is repeated untill all elements have been added to the output array

- the time complexity of merge sort is o(n log n) in worst case
- this is because the algo
1. divides input array into halves
