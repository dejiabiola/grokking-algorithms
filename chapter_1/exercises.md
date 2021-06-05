1. Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?

Solution

Binary search is logarithmic which is the inverse of exponential. To calculate this, you have to calulate how many times
do you have to multiply the number 2 by itself to get the total number of values in the sorted list. 

`O log n` Worst case scenario

For 128 names, 2 x 2 x 2 x 2 x 2 x 2 x 2 = 128

So you need 2 in 7 places all multiplied together to round up to 128 names.

So to answer the question, the maximum number of steps it would take is 7 steps. 

2. 2 Suppose you double the size of the list. What’s the maximum
number of steps now?

If you double the size of the list, meaning 128 names becomes 256 names, you will need to simply add one more step which brings it to 8 steps. The fact than you only need one extra step after doubling the number of values in the list shows you the 
efficiency of the binary search especially in comparison to linear search.

Proof of answer => 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 = 256

