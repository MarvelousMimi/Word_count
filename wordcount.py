# Ask a user for a sentence
# Remove extra whitespace around the string
# Split the sentence into Words
# Count the number of words
# Print the number of words

user_sentence = input("Enter a sentence:")
no_of_space = user_sentence.strip(" ")
list_of_words = no_of_space.split(" ")
no_of_words = len(list_of_words)
print(no_of_words) 



# bad_sentence = "   as the day    "  #has a lot of spaces
# # print(bad_sentence)
# good_sentence = bad_sentence.strip(" ")
# print(good_sentence)

# list_of_words = good_sentence.split(" ")
# print(list_of_words)

# length_of_words = len(list_of_words)
# print(length_of_words)

# to replace strings
# trial_sentence = good_sentence.replace("a","#")
# print(trial_sentence)