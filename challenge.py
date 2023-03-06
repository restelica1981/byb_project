

def add_prefix(word):
    return "un" + word

def add_prefix_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    return prefix + ": " + ": ".join([prefix + word for word in words])

def remove_suffix(word):
    if word.endswith("ness"):
        word_ = word[:-4]
        if word_[-1] == "i":
            return word_[:-1] + "y"
        return word_
    return word


def extract_transform(sentence, index):

    words = sentence.split()
    adjective = words[index]
    return adjective + "en"

while True:

    print('1. Add Prefix *un*')
    print('2. Make Word groups')
    print('3. Remove Suffix *ness*')
    print('4. Adjective to Verb')

    choice = input('Pick an option: ')

    if choice not in ('1', '2', '3', '4'):
        print('Please enter valid option')
        continue
        
    elif choice == '1':
        
        word = input('Please enter a word: ')
        prefixed_word = add_prefix(word)
        print(prefixed_word)

    elif choice == '2':
        vocab_words = input('Enter the prefix followed by a list of words, separated by a comma: ').split(',')
        word_group = add_prefix_word_groups(vocab_words)
        print(word_group)

    elif choice == '3':
        word = input('Enter word to remove suffix: ')
        word_ = remove_suffix(word)
        print(word_)

    elif choice == '4':
        sentence = input('Enter a sentence: ')
        index = int(input('Enter index of adjective to change: '))
        verb = extract_transform(sentence, index)
        print(verb)
    
    else:
        break

