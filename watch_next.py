import spacy

def planetHulk(): 
    with open ('movies.txt', 'r', encoding = "utf-8-sig") as text_read: 
        sentences = text_read.readlines()
        
    nlp = spacy.load('en_core_web_md')#loads module 
    sentence_to_compare =  ("""Will he save
    their world or destroy it? When the Hulk becomes too dangerous for the
    Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
    planet where the Hulk can live in peace. Unfortunately, Hulk land on the
    planet Sakaar where he is sold into slavery and trained as a gladiator.""")
    model_sentence = nlp(sentence_to_compare) 
    similarity_metric = []
    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)#checks similarity against model sentence 
        similarity_metric.append(similarity)#appends similarity metric to list
    most_similar_sentence = ""
    for idx, integer in enumerate(similarity_metric): 
        if max(similarity_metric) == integer: #gets maximum similarity metric off the list 
            new_line = sentences[idx] #gets the index of the sentence 
            new_line = new_line.split(':')#splits with the colon seperator 
            most_similar_sentence += new_line[0] #appemnds to most_similar_sentence 
    return most_similar_sentence 

print(planetHulk())



            
        
        
         
            


