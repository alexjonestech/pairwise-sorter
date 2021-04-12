import random
import math


def quicktop(unsorted, k, better_of):
    def quicksort(unsorted):
        if not unsorted: 
            return unsorted 
    
        pivot = random.choice(unsorted)
        unsorted = [item for item in unsorted if item != pivot]
        unsortedTop = [item for item in unsorted if item == better_of(item, pivot)]
        unsortedBottom = [item for item in unsorted if item not in set(unsortedTop)]
    
        top = quicksort(unsortedTop)
        bottom = quicksort(unsortedBottom)
        return top + [pivot] + bottom

    return quicksort(unsorted)[:k]


def mergetop(unsorted, k, better_of):
    def mergesort(unsorted):
        def merge(list1, list2):
            merged = []
        
            while list1 and list2:
                better = better_of(list1[0], list2[0])
                merged.append(better)
        
                if list1[0] == better:
                    list1 = list1[1:]
                else:
                    list2 = list2[1:]
        
            return merged + list1 + list2
    
    
        if len(unsorted) <= 1:
            return unsorted
        
        (unsortedTop, unsortedBottom) = (
            unsorted[:len(unsorted)//2], 
            unsorted[len(unsorted)//2:]
            )
        (top, bottom) = (
            mergesort(unsortedTop), 
            mergesort(unsortedBottom)
            )
        return merge(top,bottom)


    return mergesort(unsorted)[:k]


def bubbletop(unsorted, k, better_of):
    for _ in range(k):
        for i in reversed(range(len(unsorted)-1)):
            if unsorted[i+1] == better_of(unsorted[i], unsorted[i+1]):
                (unsorted[i], unsorted[i+1]) = (unsorted[i+1], unsorted[i])
                swapped_top = (i < k)

    return unsorted[:k]


def tourneytop(unsorted, k, better_of):
    class tournament_tree:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right


        def build_tree_with_leaves(leaves):
            if not leaves:
                return None

            if len(leaves) == 1:
                return tournament_tree(leaves[0], None, None)

            (leftLeaves, rightLeaves) = (
                leaves[:(1+len(leaves))//2], 
                leaves[(1+len(leaves))//2:]
                )

            return tournament_tree(
                None, 
                tournament_tree.build_tree_with_leaves(leftLeaves), 
                tournament_tree.build_tree_with_leaves(rightLeaves)
                )


        def isLeaf(self):
            return not self.left and not self.right


        def isValid(self):
            return self and self.value and self.value not in removed


        def get_winner(self, removed={}):
            if self.isValid():
                return self.value

            if self.isLeaf():
                return None

            leftWinner = self.left.get_winner(removed=removed)
            rightWinner = self.right.get_winner(removed=removed)

            if not leftWinner:
                self.value = rightWinner
            elif not rightWinner:
                self.value = leftWinner
            else:
                self.value = better_of(leftWinner, rightWinner)

            return self.value


    tournament = tournament_tree.build_tree_with_leaves(unsorted)
    removed = set()
    winners = [tournament.get_winner()]
    while len(winners) < k:
        removed.add(winners[-1])
        winners.append(tournament.get_winner(removed=removed))    
    return winners

