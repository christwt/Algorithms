# LastName: Christie
# FirstName: Will
# Email: william.christie@colorado.edu
# Comments: Most inline comments are for my benefit and understanding of material.

# Sources:
# 1. https://docs.python.org/3.2
# 2. various stack overflow threads regarding tries and prefix trees.
# 3. https://www.youtube.com/watch?v=BXeIu54mUg0 "Let's Try a Trie in Python"
# 4. Algorithms textbook.

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        # The initialization below is just a suggestion.
        # Change it as you will.
        # But do not change the signature of the constructor.
        self.word = None  # Store the word at the end of the node. Useful for AutoComplete
        self.isRoot = isRootNode
        self.isWordEnd = False  # Is this node a word ending node?
        self.isRoot = False  # Is this a root node?
        self.count = 0  # Frequency count
        self.next = {}  # Dictionary mapping each character from a-z to the child node

    def addWord(self, w, string=""):  # string used to accumulate chars to set .word
        char = w[0]  # track current char of word.
        if char in self.next:  # check to see if head w is in dictionary.
            node = self.next[char]  # if yes, then update current node.
        else:
            node = MyTrieNode(False)  # if we didn't find it, then we need to add a new one.
            self.next[char] = node  # update current node.
        if len(w) > 1:
            tail = w[1:]  # if there are more chars left in our string
            node.addWord(tail, string+char)  # recurse on remaining portion.
        else:
            node.count += 1  # update count to reflect new frequency.
            node.isWordEnd = True  # update isWordEnd flag.
            node.word = string+char  # update .word to store original w.

    def lookupWord(self, w):
        # Return frequency of occurrence of the word w in the trie.
        # returns a number for the frequency and 0 if the word w does not occur.
        char = w[0]
        if char in self.next:  # check to see if head of w is in dictionary.
            node = self.next[char]  # if yes, then update current node.
        else:
            return 0  # if not, then return 0
        if len(w) > 1:
            tail = w[1:]  # if there are more chars lef in our string,
            try:
                return node.lookupWord(tail)  # recurse of remaining portion.
            except KeyError:
                return 0  # always return 0 if failure.
        elif node.isWordEnd:  # if we come to the end of the word,
            return node.count  # return our frequency.
        else:
            return 0  # always return 0 if failure.

    def autoComplete(self, w):
        results = list()  # used to store tuples.
        topNode = self
        for char in w:
            if char in topNode.next:  # if char in prefix is in dictionary.
                topNode = topNode.next[char]  # advance node.
            else:
                return results  # prefix is not in the tree, so return empty set.
        if topNode == self:  # BFS to traverse node, storing words in subTrie in results.
            queue = [node for key, node in topNode.next.items()]  # queue to contain our sub-trie nodes to traverse
        else:
            queue = [topNode]
        while queue:
            current = queue.pop()  # Basic BFS
            if current.word is not None:  # wait until we get to an isEnd node w/ saved word.
                results.append((current.word, current.count))  # add tuples to our results.
            queue = [node for key, node in current.next.items()] + queue  # adjust queue
        return results

if (__name__ == '__main__'):
    t = MyTrieNode(True)

    lst1 =['test', 'testament', 'testing', 'ping', 'pin', 'pink', 'pine', 'pint', 'testing', 'pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy')  # should return 0
    print(j)
    j2 = t.lookupWord('telltale')  # should return 0
    print(j2)
    j3 = t.lookupWord('testing')  # should return 2
    print(j3)
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)

