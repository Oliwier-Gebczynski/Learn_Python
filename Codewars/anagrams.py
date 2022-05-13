def anagrams(word, words):
    sorted_list = []
    result = []
    sorted_word = ''.join(sorted(word))

    for item in words:
        sorted_list.append(''.join(sorted(item)))

    for i in range(0, len(sorted_list)):
        if sorted_list[i] == sorted_word:
            result.append(words[i])

    return result

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])

#done