import predict
import nltk
import re
nltk.download('words')
from nltk.corpus import words
import difflib


def answer(imagepath):
    sp = '[@_!#$%^&*()<>?.,/\|}{~:]'
    d = '0123456789'
    answer = predict.predict(imagepath)
    print(answer)
    #word_list = words.words()
    #arr = difflib.get_close_matches(answer[1:], word_list)
    # if(len(arr) > 0):
    #     return arr[0]
    # else:
    #     if(answer in sp or answer[1:] in sp):
    #         return ""
    #     return answer[1:]
    if(answer in sp):
        return ""
    if (answer[1:2] in sp):
        return answer[2:]
    if ((answer[0:1] in d and answer[1:2] in sp)  or (answer[0:1] in sp and answer[1:2] in d)):
        return answer[2:]
    return answer[1:]
    