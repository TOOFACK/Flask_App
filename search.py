import random
import pandas as pd
from collections import Counter

class Document:
    def __init__(self, title, text):
        # можете здесь какие-нибудь свои поля подобавлять
        self.title = title
        self.text = text
    
    def format(self, query):
        # возвращает пару тайтл-текст, отформатированную под запрос
        return [self.title, self.text[:50] + ' ...']

index = []

def build_index():
    # считывает сырые данные и строит индекс
    df = pd.read_csv("Music_New.csv")
    for i in range(209522):
    	index.append(Document(df["ALink"][i] + " - " + df["SName"][i],df["Lyric"][i]))
    #index.append(Document('The Beatles — Come Together', 'Here come old flat top\nHe come groovin\' up slowly '))
    #index.append(Document('The Rolling Stones — Brown Sugar', 'Gold Coast slave ship bound for cotton fields\nSold in the market down in New Orleans'))
    #index.append(Document('МС Хованский — Батя в здании', 'Вхожу в игру аккуратно,\nОна еще не готова.'))
    #index.append(Document('Физтех — Я променял девичий смех', 'Я променял девичий смех\nНа голос лектора занудный,'))

def score(query, document):
    # возвращает какой-то скор для пары запрос-документ
    # больше -- релевантнее
    return random.random()

def retrieve(query):
    # возвращает начальный список релевантных документов
    # (желательно, не бесконечный)
	candidates = []
	for doc in index:
		#print(query)
		if str(query).lower() in str(doc.title).lower() or str(query) in str(doc.text).lower():
			#print(doc.text)
			
			candidates.append(doc)
			if len(candidates) > 50:
				break
	freq = {}
	docs = {}
	idx= 0
	X = []
	Y = []
	for i in candidates:
		docs[idx] = i
		X.append(idx)
		idx+=1
		if str(i.title).lower() not in freq:
			freq[str(i.title).lower()] = 0
		else:
    		
			
			count1 = Counter(str(i.title).lower().split())
			count2 = Counter(str(i.text).lower().split())
			for word in str(query).lower().split(" "):
				#print(word)
				freq[str(i.title).lower()] += count1[word]
				freq[str(i.title).lower()] += count2[word]
		Y.append(freq[str(i.title).lower()])
    		 	
    	
	a = [x for _, x in sorted(zip(Y, X))]
	ans = []
	for i in a:
		ans.append(docs[i])
	return ans[::-1]
	
    
	return ans
