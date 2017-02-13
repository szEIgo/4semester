# Name generator

import nouns
import adjectives
import random


# Random name


articles = ['a', 'an', 'the']
adjz = adjectives.adjective
nounz = nouns.noun
grammatical = []


print "Not grammatical correct"
#print random.choice(articles) +' '+adjz + " " + nounz

vowel = ['a', 'e', 'u', 'o', 'i']


for art in articles:
	for adj in adjz:
		for n in nounz:
			if art == 'a' and adj[0] not in vowel:
				grammatical.append(art + " " + adj + " " + n)
			if art == 'an' and adj[0] in vowel:
				grammatical.append(art + " " + adj + " " + n)
			#if art == 'the' and n[-3:-1] == 've':
			#	grammatical.append(art + "  " + adj + " " + n[0:-2] + 'fs')
			if art == 'the' and n[-1] == 'y' or n[-2:-1] == 'es':
				grammatical.append(art + " " + adj + " " + n[0:-1] + 'ies')
			if art == 'the' and n[-1] != 'y' and n[-1] != 'ies' and n[-1] != 's':
				grammatical.append(art + " " + adj + " " + n + 's')
				

for g in grammatical:
	print g
	
					 
			
