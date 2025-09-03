# Sum of Multiples Problem

## Problem
Find the sum of all natural numbers below N that are multiples of 3 or 5.

## Input
First line: number of test cases `t`  
Next `t` lines: each line contains integer `N`

## Output
For each test case, print the sum of multiples.

## Approach
We use the formula for sum of multiples and inclusion-exclusion principle:
sum = sum(3) + sum(5) - sum(15)
