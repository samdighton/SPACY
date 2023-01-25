import spacy 
nlp = spacy.load('en_core_web_sm')
word1 = nlp("car")
word2 = nlp("bicycle")
word3 = nlp("petrol")
#similarities were all statistics or probablities
#hence they were between 0 and 1 
#the cat and monkey were relatively related
#most probably due to them both being animals 
#monkey and bannana were also relatively similar due to the association 
#between the two words although cat and bannana were pretty unrelated 
#changed to car bicycle and petrol 
#bicycle and car were both strongly related 
#bicycle and petrol were loosely related 
#car and petrol were also loosely related but more so than bicycle and petrol 
#all a probabilistic model based off some formulaes
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
#when changed to 'en_core_sm' similarity based method does not load word vectors so is therefore unable to compare 
#the words together based on the context sensitive tensors. As the taggers are not loaded only the context sensitive 
#tensors are returned. This is because the context sensitive tensors are loaded in 'en_core_sm' and 'en_core_md'. 
#However, the tool in en_core_md for these sentence similarity appears to be more powerful in detecting consistency
#across sentences. 