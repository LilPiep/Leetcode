roots = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

def replaceWords(roots,sentence):
    sentence = sentence.split()
    for root in roots:
        pos = 0
        for word in sentence:
            if word.startswith(root) :
                sentence[pos] = root
            pos += 1
    oe = " "
    sentence = oe.join(sentence)
    return(sentence)

print(replaceWords(roots,sentence))