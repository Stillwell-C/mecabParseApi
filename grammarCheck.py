from jamo import j2hcj, h2j
from grammar import grammarArray
import re

def grammarCheck(sentence):
    possibleMatches = []

    splitSentence = j2hcj(h2j(sentence))

    for grammar in grammarArray:
        if re.search(grammar["regex"], splitSentence):
            returnFields = {"grammarForm": grammar["grammarForm"], "description": grammar["description"], "link": grammar["link"]}
            possibleMatches.append(returnFields)

    return possibleMatches