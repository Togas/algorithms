class Trie:
  trie={}
  def __init__(self, words):
    for word in words:
      self.insert(word)
    
  def insert(self, word):
    current=self.trie
    for char in word:
      if char not in dict:
        current[char]={}
      current=current[char]
    current["*"]=word
    
