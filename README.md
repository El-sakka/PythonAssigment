Problem #1 
Given: A positive integer and an array ​ A ​ [1..​ n ​ ] ​ of integers a positive number ​ k ​ ≤ ​ n
Return: The ​ k ​ -th smallest element of ​ A
Sample Input
11
2 36 5 21 8 13 11 20 5 4 1
8
Sample Output
13


Problem #2 (20 marks) Find Factors of Number
Write a program that get factors of a number and display it.
Input
>> 20
OutputThe factors of 20 are:
1
2
4
5
10
20



Problem #3  Find Armstrong Number in an
Interval
A positive integer is called an Armstrong number of order n if
abcd... = an + bn + cn + dn + ...
For example,
153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.
Your program will take start and end interval as input then print all Armstrong number in
this interval
Input
>> 100 2000
Output
153
370
371
407
1634



Problem #4 (20 marks) Convert Number
Convert number from base a to base b
Your program will take number in base a then convert it to base b
InputEnter number
>> 234
Enter Number base
>> 6
Convert it to base
>> 8
Output
136


Problem#5  Addition Using BCD
Binary Coded Decimal (BCD) is a form of decimal representation represent the 10
decimal digits in terms of binary numbers each number in four bits.
Through Addition calculation for any invalid entry (any BCD digit greater than 1001)
exists, 6 is added to generate a carry bit and cause the sum to become a valid entry.
The reason for adding 6 is that there are 16 possible 4-bit BCD values (since 2​ 4​ = 16),
but only 10 values are valid (0000 through 1001). So adding 6 to the invalid entries
results in the following:
1001 1000 1011 1111
9 8 11 15
+ 0000 0000 0110 0110
0 0 6 6
= 1001 1001 0010 0101
9 9 2 5
ex.
To add 124 + 196 you need to follow these steps
a) Convert number to BCD representation
(124) = (0001 0010 0100)
(195) = (0001 1001 0110)
b) Adding BCD
Carry
1
1
0001 0010 0100+
0001 1001 0111
-----------------------------------
Carry
1 1111 11
0010 1011 1011
+
0000 0110 0110
-----------------------------------
0011 0010 0001
c) Convert result to decimal digit again
(0011 0010 0001) = (321)
Input
Enter First Number
>> 124
Enter Second Number
>> 197
Output
321
