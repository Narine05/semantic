#importing spacy
import spacy
nlp = spacy.load('en_core_web_md')

#defining the predefined movie
my_film = "Planet Hulk"
my_desc = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

#function returning the most similar movie
def find_similar_movie(description):
    mv_list = []
    new_list = []
    model_sentence = nlp(description)

    #Loops through the file
    for i in open('movies.txt', 'r'):
        mv_list = i.split(':')
        similarity = nlp(mv_list[1]).similarity(model_sentence)
        #appends the movie name and the similarity score to a new list
        new_list.append([mv_list[0].strip(),similarity])

    #Sort the list according to the second element (similarity) in the sublist
    new_list.sort(key=lambda x: x[1], reverse=True)
    #returns the first element with the highest score
    return new_list[0][0]


sim_movie = find_similar_movie(my_desc)
print(f"The most similar movie to '{my_film}' is '{sim_movie}'")