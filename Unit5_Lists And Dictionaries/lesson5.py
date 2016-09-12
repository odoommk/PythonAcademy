suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

"""In the above example, we first create a list called letters.
Then, we take a subsection and store it in the slice list. We start at the index before the colon and continue up to but not including the index after the colon.
Next, we print out ['b', 'c']. Remember that we start counting indices from 0 and that we stopped before index 3.
Finally, we print out ['a', 'b', 'c', 'd', 'e'], just to show that we did not modify the original letters list.
"""
