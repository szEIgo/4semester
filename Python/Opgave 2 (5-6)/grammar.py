# Name generator

import nouns
import adjectives
import random
import verbs


# Random name


articles = ['a', 'an', 'the']
adjz = adjectives.adjective
nounz = nouns.noun
verbz = verbs.verb
grammatical = []

count = 0;



vowel = ['a', 'e', 'u', 'o', 'i']
for article in articles:
	for noun in nounz:
		for verb in verbz:
			if article == 'a' and noun[0] not in vowel:
				grammatical.append(articles[0] + " " + noun + " " + verb)
			elif  article == 'an' and noun[0] in vowel:
				grammatical.append(article[1] + " " + noun + " " + verb)
			else:
				grammatical.append(articles[2] + " " + noun + " " + verb)


for g in grammatical:
	

#print "Not grammatical correct"
#print random.choice(articles) +' '+adjz + " " + nounz
#for art in articles:
#	for adj in adjz:
#		for n in nounz:
#			if art == 'a' and adj[0] not in vowel:
#				grammatical.append(art + " " + adj + " " + n)
#			if art == 'an' and adj[0] in vowel:
#				grammatical.append(art + " " + adj + " " + n)
#			if art == 'the' and n[-3:-1] == 've':
#				grammatical.append(art + "  " + adj + " " + n[0:-2] + 'fs')
#			if art == 'the' and n[-1] == 'y' or n[-2:-1] == 'es':
#				grammatical.append(art + " " + adj + " " + n[0:-1] + 'ies')
#			if art == 'the' and n[-1] != 'y' and n[-1] != 'ies' and n[-1] != 's':
#				grammatical.append(art + " " + adj + " " + n + 's')
				

#for g in grammatical:
	
#	count = count+1
#	print count
#	print g

# Correct article



				
			
				
					 
			
