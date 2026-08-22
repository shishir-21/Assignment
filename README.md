
## Problem

Given a list of movies with their ratings, we need to search movies using a prefix.

## Approach
I use two data structures:

1. Trie : Trie use because problem is based on prefix search
2. Min Heap : This is used for return top N highest rated movies

## Why Not use Max Heap?
max heap keeps the largest value at the root.

But i need to remove the smallest movie in our current top N movies whenever a better movie comes.


## How Search Works

Suppose we call:

search("to", 3)

### Step 1: Search the prefix in Trie

First, search `"to"` in the Trie.

### Step 2: Find matching movies

From this node use DFS and collect all movies starting with "to".

### Step 3: Get top rated movies

Now we use a Min Heap.

The value 3 means we need only 3 movies, So we keep the 3 highest rated movies.

If there are more than 3 matching movies, we remove the movie with the lowest rating

Step 4: Return result
Finally return the top 3 movies.

output: 
<img width="1827" height="59" alt="image" src="https://github.com/user-attachments/assets/862ea901-9d8f-4e43-a4be-6431a20ea352" />

The output is not sorted because a heap is not a sorted data structure.
