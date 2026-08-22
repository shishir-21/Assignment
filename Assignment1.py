import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.movies = []   # (title, rating)


class MovieIndex:
    
    # in this we create the root and insert every movie into the trie
    def __init__(self, movies):
        self.root = TrieNode()

        for title, rating in movies:
            self._insert(title, rating)

    def _insert(self, title, rating):
        node = self.root

        for char in title.lower():   # convert title into lowercase
            if char not in node.children:  # If character does not exist then create a new node
                node.children[char] = TrieNode()

            node = node.children[char]

        node.movies.append((title, rating))  # store original title and rating

    def search(self, prefix, n):
        
        if n <= 0:
            return []

        node = self.root

        for char in prefix.lower():
            if char not in node.children: #if prefix does not exist then return empty
                return []

            node = node.children[char]

        # min-heap containing of size n
        heap = []

        self._collect_top_n(node, heap, n)

        return heap

    def _collect_top_n(self, node, heap, n):

        for title, rating in node.movies: #check every matching movie.

            heapq.heappush(heap, (rating, title))   # added movie to the heap.

            if len(heap) > n:  #if the heap bigger than n
                heapq.heappop(heap) # then removes the smallest rating.


        for child in node.children.values():     # This is for DFS
            self._collect_top_n(child, heap, n)


# Example
movies = [
    ("Toy Story", 8.1),
    ("Top Gun", 7.5),
    ("Tomorrowland", 6.4),
    ("Titanic", 7.9),
    ("Harry Potter", 8.3),
    ("Friends", 6.8)
]

index = MovieIndex(movies)

print(index.search("to", 3))
