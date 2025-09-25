first_sentence = input("Please enter first sentence: ")
second_sentence = input("Now, enter the second sentence: ")

print(f"Thank you! Summary:\n\nFirst Sentence: '{first_sentence}'\n** Character count: {len(first_sentence)} **\n\nSecond sentence: '{second_sentence}'\n** Character count: {len(second_sentence)} **\n")

if len(first_sentence) > len(second_sentence):
    print(f"The first sentence is the longest with {len(first_sentence)} characters!")
elif len(first_sentence) < len(second_sentence):
    print(f"The second sentence is the longest with {len(second_sentence)} characters!")
else:
    print(f"The two sentences are the same length, with {len(first_sentence)} characters!")