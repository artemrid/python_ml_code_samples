import spacy

nlp = space.load("en_core_web_sm")
doc = nlp("Robots will win")
robots = doc[0]
will = doc[1]
win = doc[2]
print("The word 'robots' is a ", robots.pos_)
print("The word 'will' is a ", will.pos_)
print("The word 'win' is a ", win.pos_)
