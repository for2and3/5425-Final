import difflib
import pandas as pd
import json

def find_most_similar_word(word_list, target_word):
    highest_ratio = 0
    most_similar_word = ""
    for word in word_list:
        ratio = difflib.SequenceMatcher(None, target_word, word).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            most_similar_word = word
    return most_similar_word

def find_related_keyword(text, keywords):   
    related_scores = {}
    words = text.split()
    for keyword in keywords:
        related_word = find_most_similar_word(words, keyword)
        related_scores[keyword] = difflib.SequenceMatcher(None, keyword, related_word).ratio()
    related_keywords = sorted(related_scores, key=related_scores.get, reverse=True)
    return related_keywords


data = 'R —— o e \\L‘ A e v 10x1x4 Tablets Cabergoline Tablets IP 0.5mg. L Cabergoline 0.5 N w08 N St 4 . T e | i Cabergoline Tablets IP 0.5mg. @i o8y 1 Cabergoline 05 i 1 e /‘_ i'
df = pd.read_excel('Data_Clean.xlsx', sheet_name='Sheet1')
related_keywords = find_related_keyword(data, df['Drug_name'])
result = df.loc[df['Drug_name'] == related_keywords[0]]
json_string = result.to_json(orient='records')
json_data = json.loads(json_string)
print(json_data)