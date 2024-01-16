Bubble Sort.
We have 2 loops: i and j. The I increases as usual but j right bound
is decreasing every time with the destructing the i. 
In the internal j loop we start from start everytime and compare
the current value (arr(j)) with the next (arr(j) + 1) and swap - move
to the right until current value is bugger then next.

Insertion Sort.
We divide array from start on sorted part and unsorted part. 
Initially sorted part has just single the most left element. Then
we go to the next element, compare it with previous, swap, do it again
and again. And left array (sorted array) is getting bigger and bigger.

Merge Sort.
Arrays is divided into the set of single element arrays which then
are compared and merged into bigger arrays back.