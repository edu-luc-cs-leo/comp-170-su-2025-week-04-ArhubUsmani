def longest_word(words: list[str]) -> str:
  # Start with the first word as the longest so we can compare to others
  longest = words[0]
  # Loop through list to find a longer word
  for word in words:
    if len(word) > len(longest):
      longest = word
  return longest

def shortest_word(words: list[str]) -> str:
  # Start with the first word as the shortest
  shortest = words[0]
  # Loop through the list to find a shorter word
  for word in words: 
    if len(word) < len(shortest):
      shortest = word
  return shortest

def odd_words(words: list[str]) -> list[str]:
  # Create a new list to store words with odd length
  result = []
  # Check each word and add it to the result list if its length is odd
  for word in words:
    if len(word) % 2 == 1:
        result.append(word)
  return result

def average_words(words: list[str]) -> list[str]:
    # First calculate the total length of all words
    total_length = 0
    for word in words:
        total_length += len(word)
    # Calculate the average length and round it to the nearest whole number
    average = round(total_length / len(words))
     # Make a list to store words close to average length (want words with length within ±1 of average)
    result = []
    for word in words:
        if abs(len(word) - average) <= 1:
            result.append(word)
    return result

def intersect(foo: list[str], bar: list[str]) -> bool:
    # Loop through each element in the first list
    for item in foo:
        # If the item is also in the second list (return true)
        if item in bar:
            return True
    # If we did not find any matches (return false) 
    return False

# Basic testing
words = ["apple", "banana", "kiwi", "mango", "pear"]

print("Longest word:", longest_word(words))       # Expected: "banana"
print("Shortest word:", shortest_word(words))     # Expected: "kiwi"
print("Odd-length words:", odd_words(words))      # Expected: ['apple', 'banana', 'kiwi']
print("Average-length words:", average_words(words))  # Expected: ['apple', 'banana', 'kiwi', 'mango', 'pear']

foo = ["cat", "dog", "bird"]
bar = ["fish", "lion", "cat"]
print("Do they intersect?", intersect(foo, bar))  # Expected: True

  
"""
Reflection

I noticed a few differences in the solutions to my code that helped me understand what I can improve on.

Comments 
I did comment in my original code

Output and Testing
I did test my code and make sure it produced the right output. In solutions the testing was more structred, will begin to do that too.

Logic 
I did not use anything too advanced or complicated. I can simplify things more, like in draw_diamond, I had a few extra steps that could have been made cleaner.

Overall i did not have much to fix or too many differences. I am working towards more concise and cleaner code.

"""

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
