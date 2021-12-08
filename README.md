My solutions to Advent of Code 2021 (https://adventofcode.com/2021), in Python3.


### Day 3, part 2

The challenges in the first two days are pretty straightforward, nothing surprising. Day 3 part 2 is when it starts getting interesting.

The approach I decided to take was to sort each string on each character we're considering, but since there are only two possible values (0 and 1), this is really just a simple bucket sort, which I did in place to avoid unnecessary memory usage. At first I was thought this was overkill, and I was sure there was some one-liner that could take care of it (which always happens on leetcode). Luckily, other people's implementations are equally verbose, if not more so.

I then used recursion on each subsequent smaller list since it was easier than iterating and keeping track of a new slice of the list.

In the previous challenges, I was able to just do one pass through the input without reading it all into memory, but unfortunately I don't think that was possible on this one, since you have to potentially look over every item n times, where n is the length of the binary strings.

The time complexity of this solution is O(nm^2), where n is the number of binary strings and m is the length of each binary string. To see why, consider the worst case scenario, where we have to iterate over and swap every single element in the list m times.

Space complexity is O(nm), from reading the entire input into memory.
