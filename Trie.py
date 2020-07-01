class Trie:
  trie={}
  def __init__(self, words):
    for word in words:
      self.insert(word)
    
  def insert(self, word):
    current=self.trie
    for char in word:
      if char not in current:
        current[char]={}
      current=current[char]
    current["*"]=word
  
  def inTrie(self, word):
    current=self.trie
    for char in word:
      if char not in current:
        return False
      current=current[char]
    if "*" in current:
      return True
    return False
