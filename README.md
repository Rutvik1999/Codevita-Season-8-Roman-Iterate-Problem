# Codevita-Season-8-Roman-Iterate-Problem
 
Roman Iteration
Problem Description:

We know about number systems: The Roman numerals and the alternative "place value system" with a given base. For the purposes of this problem, we limit ourselves to
Roman numerals with values up to 3999 (MMMCMXCIX)
'Place value system" numbers having bases from 2 (with possible symbols 0,1) through 36 (with possible symbols 0, 1, ..., 9, A, ... ,Z) Consider the following procedure:
Accept a natural number N (in base 10).
If N lies in the closed interval [1,3999], i.e. between 1 and 3999 (both inclusive), convert N to R, its Roman numeral representation; else output N as the result and stop.
Identify the base in which the value of R, now considered to be in 'place value system', is least and calculate its value in base 10, replacing N with this value.
Repeat from step 2.
— Constraints
1 <= N <= 3999.
— Input Format
A single Integer N.
Output
Converted N.
— Test Case
Explanation
Example 1 Input
1
Output
45338950 
Explanation:
The procedure goes as follows in this case:
Accept N = 1.
Since 1 lies in [1,3999], covert it to Roman R = I.
The least value of I (in bases 19 and above) is 18 in base 10. Hence N = 18.
4, 2': Repeating step 2, since 18 lies in [1,3999], convert it to R =
3': The least value of XVIII (in base 34) is 33*34^4+31*34"3+18*34"2+18*34+18 or N = 45338950.
4', 2": Repeating step 2, since 45338950 lies outside [1,3999], output 45338950 and stop.
Here's how the conversions go: Input = 1 => I => 18 => XVIII => 45338950 = Output.
