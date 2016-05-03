#!/usr/bin/python3
from sys import argv
from string import whitespace
import string

myPunctuation = ".?!:"

def getPrefix(i):
	global paragraph
	i = i - 1
	prefix = ""
	while(i >= 0 and paragraph[i] not in whitespace):
		prefix = paragraph[i] + prefix
		i -= 1
	return prefix
def getSuffix(i):
	global paragraph
	i = i + 1
	suffix = ""
	while (i < len(paragraph) and paragraph[i] not in whitespace):
		suffix += paragraph[i]
		i += 1
	return suffix
def getNext(i):
	global paragraph
	while(i < len(paragraph) and paragraph[i] not in whitespace):
		i+= 1
	while(i < len(paragraph) and paragraph[i] in whitespace):
		i+= 1
	nextWord = ""
	while (i < len(paragraph) and paragraph[i] not in whitespace):
		nextWord += paragraph[i]
		i += 1
	return nextWord
def getPrevious(i):
	global paragraph
	while(i >= 0 and paragraph[i] not in whitespace):
		i -= 1
	while(i >= 0 and paragraph[i] and paragraph[i] in whitespace):
		i -= 1
	previousWord = ""
	while (i >= 0 and paragraph[i] not in whitespace):
		previousWord = paragraph[i] + previousWord
		i -= 1
	return previousWord
def getType(str):
	if len(str) == 0:
		return 'empty'
	elif str.isupper():
		return 'upper'
	elif str.islower():
		return 'lower'
	elif str.isdigit():
		return 'numeric'
	elif str == string.capwords(str):
		return 'capword'
	else:
		return 'misc'
# for i, char in enumerate(paragraph):
# 	if char in myPunctuation:
# 		print(getPrefix(i), getSuffix(i), getPrevious(i), getNext(i))


def getcharname(char):
	if char == '.':
		return 'dot'
	if char == '?':
		return 'quest'
	if char == '!':
		return 'exclam'
	if char == ':':
		return 'colon'
	return None

index = 0
def getattribute(i):
	global paragraph
	prefix = getPrefix(i)
	suffix = getSuffix(i)
	previousWord = getPrevious(i)
	nextWord = getNext(i)

	attribute = list()
	attribute.append(getcharname(char))
	attribute.append(getType(prefix))
	attribute.append(getType(suffix))
	attribute.append(getType(previousWord))
	attribute.append(getType(nextWord))
	attribute.append(str(len(prefix)))
	attribute.append(tagList[index])
	index += 1
	return ','.join(attribute) + '\n'

if __name__ == "__main__":
	prepFile = argv[1]
	tagFile = argv[2]
	fprep = open(prepFile, 'r')
	ftag = open(tagFile, 'r')
	outputFile = prepFile.replace('.prep', '.arff')
	fout = open(outputFile, 'w')
	paragraphs = fprep.read().split('\n')
	tagList = ftag.read().split('\n')


	print(paragraphs[:5])
	print(tagList[:10])

	for paragraph in paragraphs:
		# fout.write(paragraph + '\n')
		for i, char in enumerate(paragraph):
			if char in myPunctuation:
				attribute = getattribute(i)
				fout.write(attribute)
