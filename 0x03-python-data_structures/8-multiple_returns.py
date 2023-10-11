#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if not sentence:
        r = (leng, None)
    else:
        r = (leng, sentence[0])
    return r
