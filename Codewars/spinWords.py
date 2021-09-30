def spin_words(sentence):
    sentenceArr = sentence.split()
    y = 0
    for x in sentenceArr:
        if len(x) >= 5:
            x = x[::-1]
            sentenceArr[y] = x
        y += 1
    spinText = ''.join(sentenceArr)

    return spinText

#DONE
