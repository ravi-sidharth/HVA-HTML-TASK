Longest Subarray with Increasing Numbers
You are given an integer array. Print the length of the longest subarray with increasing numbers.

A subarray is defined as a contiguous portion of an array.

Try not to use nested loop.

Sample Input
5 4 4 7 6 3 2 4 6 8 6 3 6 8 5

Sample Output
4

Explanation: The given array has many subarrays with increasing numbers.
4 4 7 -> 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
2 4 6 8 -> 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
3 6 8 -> 5 4 4 7 6 3 2 4 6 8 6 3 6 8 5
Out of all these, the subarray with 4 increasing numbers is the longest.


array =list(map(int,input().split()))

count=1
max_count=0
i=0
end=0

while i<len(array)-1:
    if array[i]<=array[i+1]:
      count+=1

      if count >= max_count:
        end=i+1
        print(end)
        max_count=count
    else:
      count=1
    i+=1
# print(max_count)

start=end-max_count+1
# print(start)
while max_count>0:
  print(array[start],end=" ")
  start+=1
  max_count-=1

