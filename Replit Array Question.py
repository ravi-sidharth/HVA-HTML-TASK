Answer to the question number 1:

Square - Each Array Element
You are given an integer array. Traverse through the array and print the square for each element.

Sample Input
5 3 4 7 2 9

Sample Output
25 9 16 49 4 81


array = list (map(int,input().split()))

i=0

while i<len(array):
	print(array[i]*array[i],end=" ")
	i+=1




Answer to the question number 2:

Odd or Even - Each Array Element
You are given an integer array. Traverse through the array and for each element, if the element is odd print "Odd", else print "Even".

Sample Input
4 7 9 10 13 17
Sample Output
Even
Odd
Odd
Even
Odd
Odd



array = list(map(int,input().split()))

i=0
while i<len(array):
	if array[i]%2==0:
		print("Even")
	else:
		print("Odd")	
	i+=1



Answer to the question number 3:

Odd Count in an Array
You are given an integer array. Print the number of odd numbers in the array.

Sample Input
4 7 9 10 13 17
Sample Output
4
Explanation: There are 4 odd numbers in the given numbers: 7, 9, 13, 17.


array =list(map(int,input().split()))

i=0
count=0
while i<len(array):
	if (array[i]%2!=0):
		count+=1
	i+=1

print(count)


Answer to the question number 4:

Number Count in an Array
You are given an integer array. You are also given a number. Print the number of times the number appears in the array.

Sample Input
4 7 9 10 7 14 12 4 7 27
7
Sample Output
3
Explanation: The given number 7 appears 3 times in the given array.

array =list(map(int,input().split()))
target=int(input())

i=0
count=0
while i<len(array):
	if target==array[i]:
		count+=1
	i+=1
print(count)



Answer to the question number 5:

Sum of Elements in an Array
You are given an integer array. Add all the numbers present in the array and print the sum.

Sample Input
10 5 6 3 4 3 5 6
Sample Output
42
Explanation: 10+5+6+3+4+3+5+6 = 42

	array = list(map(int,input().split()))
	array_sum=0

	i=0
	while i<len(array):
		array_sum+=array[i]
		i+=1
	print(array_sum) 


Answer to the question number 6:

Average of Elements in an Array
You are given an integer array. Find the average of all the numbers present in the array.

Sample Input
10 5 6 3 4 3 5 6
Sample Output
5.25
Explanation: There are 8 elements in the given array. Sum = 10+5+6+3+4+3+5+6 = 42. Average = 42/8 = 5.25

array =list(map(int,input().split()))

n=len(array)
sum=0

i=0 
while i<len(array):
	sum+=array[i]
	i+=1

average=sum/n

print(average)



Answer to the question number 7:


array = list(map(int, input().split()))

i=0 
min=2**63-1

while i<len(array):
  if min>array[i]:
    min=array[i]
  i+=1


j=0

while j<len(array):
  if min==array[j]:
    print(j+1)
    break
  j+=1


Answer to the question number 8:

You are given an integer array. Print the maximum sum of two consecutive integers in the given array.
Sample Input
3 6 2 1 7 2 5 6 1
Sample Output
11
Explanation: 5+6 = 11 is the maximum sum of two consecutive integers in the given array.

array =list(map(int,input().split()))
max=0
i=0
max_sum=False
while i<len(array):
	if max<array[i]:
		max=array[i]
	i+=1
	

sum= max
k=1
while True:
	j=0
	while j <len(array):
		if array[j]==max-k:
			sum+=array[k]
			max_sum=True
			break
		j+=1
		k+=1
			
	if max_sum==True:
		break
print(sum)
		
		
Answer to the question number 9:
Count Elements until Negative
You are given an integer array. Count all the numbers present in the array till you encounter a negative number and print the count. If no negative number is present, count till the end.

Sample Input
10 5 6 3 -1 4 -3 5 6
Sample Output
4
Explanation: There are 4 elements before the first negative number appears.

array =list(map(int,input().split())) 

count=1
while count<=len(array):
	if array[count]<0:
		break
	count+=1

print(count)



Answer to the question number 10:
You are given an integer array. Add all the numbers present in the array till you encounter a 0 and print the sum. If no 0 is present, add till the end.

Sample Input
10 5 6 3 0 4 3 5 6
Sample Output
24
Explanation: 10+5+6+3 = 24


array =list(map(int,input().split())) 
sum=0
i=0
while i<len(array):
	if array[i]==0:
		break
	sum+=array[i]	
	i+=1

print(sum)



Answer to the question number 11:
You are given an integer array. Take another number as input and search if the number is present in the given array. If the number is present, print "Yes", else print "No".

Sample Input 1
11 1 13 21 3 7
3
Sample Output 1
Yes
Sample Input 2
11 1 13 21 3 7
5
Sample Output 2
No

array =list(map(int,input().split()))
target_number = int(input())

i=0 
while i<len(array):
	if array[i]==target_number:
		print("Yes")
		break
	i+=1
else:
	print("No")
	
	
	
Answer to the question number 12:

Check Array for Negative Numbers
You are given an array of integers. Check if the array has any negative numbers. If the array has any negative number, print yes. Else, print no.

Sample Input 1
11 1 13 21 3 7
Sample Output 1
No
Explanation: The given array has no negative number.

Sample Input 2
6 8 9 -1 14 8 -3 6
Sample Output 2
Yes
Explanation: The given array has negative numbers, -1 and -3.


array =list(map(int,input().split()))
i=0
while i <len(array):
	if array[i]<0:
		print("Yes")
		break
	i+=1
else:
	print("No")
	
	
	
Answer to the question number 13:

Check Array for Ascending Order
You are given an array of integers. Check if the array is in Ascending Order. If yes, print "Yes", else print "No.

Sample Input 1
3 5 10 13 16 12 14
Sample Output 1
No
Explanation: The given array is not in ascending order.

Sample Input 2
3 5 10 13 16 25 33
Sample Output 2
Yes
Explanation: The given array is in ascending order.

array = list (map(int,input().split()))
i =0 
while i<len(array)-1:
	if array[i]<array[i+1]:
		i+=1
	else:
		print("No")
		break
print("Yes")



Answer to the question number 14:


First Perfect Square
You are given an array of integers. Print the first element of the array that is a perfect square. If there are no perfect squares, print No.

Sample Input 1
3 6 7 4 6 9 1 23
Sample Output 1
4
Explanation: In the given array, the first perfect square to appear is 4.


Sample Input 2
10 8 14 11 6 15
Sample Output 2
No
Explanation: In the given array, there are no perfect squares.

array =list(map(int,input().split()))
i =0 
perfect_square =False
while i < len(array):
	j=1
	while j<=array[i]:
		if  j*j==array[i]:
			print(array[i])
			perfect_square=True
			break
		j+=1
	if perfect_square is True:
		break
else: 
	print("No")




Answer to the question number 15:
First Element Greater Than K
You are given an array of integers and another integer K. Print the first element of the array that is greater than K. If there are no elements greater than K, print No.

Sample Input 1
3 5 10 25 16 12 14
11
Sample Output 1
25
Explanation: In the given array, the first element greater than 11 is 25.


Sample Input 2
3 5 10 13 16 12 14
19
Sample Output 2
No
Explanation: In the given array, there are no elements greater than 19.



array =list(map(int,input().split()))

count=1
max_count=0
start=0
i=0

while i<len(array)-1:

    
    if array[i]<=array[i+1]:
      count+=1
     
        
    else:
      count=1
      
    if count >= max_count:
        max_count=count
        start=i
    i+=1
print(max_count)



Answer to the question number 16:

Reverse an Array
You are given an array of integers. Create a new array with elements in reverse order. Print the new array.

Sample Input
11 1 13 21 3 7

Sample Output
7 3 21 13 1 11


array = list(map(int, input().split()))

new_array = [0]*len(array) 

i=len(array)-1
j=0
while i>=0 :
  new_array[j]=array[i]
  j+=1
  i-=1


j=0
while j<len(new_array): 
  print(new_array[j],end=" ")
  j+=1
  
  
  
  
Answer to the question number 17:

Check Array for Palimdrome
You are given an array of integers. Check if the given array is a Palindrome. If it is a Palindrome array, print yes, else print no.

Note: A Palindrome Array is when the reverse of the array is the same as the original array.

Sample Input 1
11 1 13 21 3 7
Sample Output 1
No
Sample Input 2
17 1 13 1 17
Sample Output 2
Yes
Explanation: The reverse of the array reads same as the original array.

array = list(map(int, input().split()))

i=0
n=len(array)-1
palindrome =True
while i<=n/2:
  if array[i]==array[n]:
    i+=1
    n-=1
    continue 
  else:
    print("No")
    palindrome=False
    break

if palindrome is True:
 print("Yes")
 
 
 Answer to the question number 18:
 
Maximum Frequency in an Array
You are given an array of integers. Find the element that appears the maximum number of times in an array. If multiple elements appear maximum number of times, you have to print the element which occurs first.

Sample Input
5 4 7 11 8 4 6 11 9
Sample Output
4
Explanation: Both 4 and 11 appear 2 times. We can print any of 4 and 11, so we print 4.


array =list(map(int,input().split()))

i=0
count=0
max=0
frequency=0
while i < len(array):
	j=i 
	while j < len(array):
	
		if array[i]==0:
			break
		if array[i] == array[j]:
			array[j]=0
			count=+1
		j+=1
	print(array)
	if max > count:
		max=count
		frequency=array[i]
	print(max)
	print(frequency)
	i+=1
	
			
			

































































































	




	



