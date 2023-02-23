def letter_counter(word):
    letter_counter = {} #with dictionary works but letter_counter = set() doesnt work cuz
    for letter in word:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    print(letter_counter)


letter_counter('hello')
