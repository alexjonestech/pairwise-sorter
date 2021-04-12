# Pairwise Sorter
Sorts (or gets top K items) from a list of items by pairwise comparison. Operates within the best (known) upper bound for necessary comparisons.

# How to use
Replace "list_of_values.txt" with any list of items you would like to sort or get the top K items from, where each item is on it's own line. Running the python script "pairwise_sorter.py" will use the selected K, comparator, and selector implementation to get the top K items from your list. By default, K = 5, the comparator gets user choice (you choose which one of two options is better), and uses the tournament selector.

There are no command line options or gui for this application currently, so if you want to change parameters you will need to do so in code. Most of the other options are for testing purposes, as user choice comparator is the main focus of the app and tournament selector is the best implementation for that use case. However, I should at least add K as a choice in the (command line) interface.

# Tournament selector
## Why this algorithm?
The tournament selector (called "tourneytop" in the code) operates within the best known upper bound for necessary comparisons for N (length of list) and K. Note that this does not necessarily make it more efficient in clock-time (for a fast comparator), especially for large N, nor is it optimized for space or computational complexity in general. The motivation behind this decision was that the main feature of this sorter -- the user choice comparator -- is a highly expensive operation, in that it's much slower than any comparisons done by the computer and also costs the effort and attention of the user. User choice also guarantees that input sizes will not be obscenely large, so space complexity is mostly a non-issue for this use case. The upshot of all of this is that the highest priority is minimizing the number of comparisons needed to complete the task.

## How does it work?
The idea behind the tournament selector is quite simple actually. We set up a tournament bracket, which is a binary tree whose values are empty at initializion, besides the leaves, whose values are the items to be selected from. Then the values in the leaves are propogated upwards by pairwise comparisons (matches) and the value of the root is our "winner", the top element of list. Then, we simply remove the winner and run the tournament again, repeating until we have our top K items. Naively, we could rebuild the bracket without the winner and run the full tournament, but we will likely be taking unnecessary and repeated comparisons if we do that. Instead, we reuse the bracket from the previous tournament which is filled out with the winners from each round. Then we take those winners to still be the winner as long as they weren't removed, thus replaying only the matches that involved the previous winner.

The assumption being made here is that if some item A is better then another item B in one match, then A will be better than B in any match. Further, we are assuming that the order is transitive, i.e. if A is better than B, and B is better than C, then A must be better than C. Lastly, this implementation doesn't currently allow for ties, but that is a limitation of the existing code and not the model, which easily handles this case.

## How many comparisons are made?
The best known upper bound for the number of necessary comparisons to get the top K items from a list of N items is

![equation](https://latex.codecogs.com/svg.latex?C%28N%2CK%29%20%5Cleq%20N%20-%20K%20&plus;%20%5Csum%5Climits_%7Bj%20%3D%20N%20&plus;%202%20-%20K%7D%5E%7BN%7D%20%5Clceil%20%5Clg%28j%29%5Crceil)

For the provided list, N = 141 and K = 5, and so this evaluates to C ≤ 168. In my various tests, the number of comparisons were always between 163 and 165. The fact that this algorithm operates within the known bound in wholly unsurprising when considering that the proof for this bound is done by constructing (a mathematical model of) the exact algorithm implemented here.

## Is there anything better?
There is definitely no better worst-case algorithm for this task, as the existence of such an algorithm would itself be a proof of a better lower bound. However, there may be improvements that could be made to reduce best- and average- cases. The shape of the initial bracket and the order of the populated data are both factors to the actual number of comparisons, neither or which were actually considered in this implementation. If given a nearly-sorted list (or a heuristic to get an approximation of one), I believe average case could actually be brought down somewhat for higher values of K (and especially K = N).

It is also worth noting that a variant of this problem exists where the top K elements are not ranked among themselves, and in this case the best upper bound is

![equation](https://latex.codecogs.com/svg.latex?C%28N%2CK%29%20%5Cleq%20N%20-%20K%20&plus;%20%28K-1%29%5Clceil%5Clg%28N&plus;2-K%29%29%5Crceil)

which you may recognize as identical to the one above, but with each element of the sum replaced with the smallest one. The algorithm/proof for this one is more complicated, but is a bit more efficient for the cases it covers. It's actually an algorithm for getting the Kth top item from the list, and the unsorted (K-1)st to 1st top items pop out for free. This difference is negligible to none for the case where K is small (no difference for (N,K) = (141,5)). This is not implemented here since it's not exactly the case I wanted to consider, but I may add it in later anyways just as a challenge.

## Where can I read more about these kinds of algorithms?
Donald Knuth's "The Art of Computer Programming" is the go-to resource for all your algorithm needs. This particular class of problems is covered in Volume 3, Chapter 5.3.3, aptly named "Minimum-Comparison Selection" (at least in the 1998 2nd edition printing). I highly recommend anyone interested in algorithm design to flip through these texts. They are absolutely massive (just Volume 3 is nearly 800 pages!), and reading them front to back is a daunting task to say the least. However, it's not too hard to jump in to any section that sounds interesting and learn (and implement!) a new algorithm or two.
