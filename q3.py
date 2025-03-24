# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

#### YOUR CODE HERE 
with open("romeo_and_juliet.txt","r") as f:
    text = f.read()

# Count how many times the word "Juliet" appears

#### YOUR CODE HERE 

word_count = {}
text = text.split()
for word in text:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)