"""
EXAMPLE DICTIONARIES:
Analyzing Song Lyrics in 3 steps:
+ Create a dictionary that  counts the amount of times a word shows up in the lyrics of a song
+ Create a function that finds the most common word and tells us how many times it occured
+ Create a function that collects all the words that appear at least X times in the song
"""

def main():
    lyrics = ["this", "is", "a", "test","this", "this", "is", "a", "a", "a", "a", "test", "test", "test", "test", "test", "wouter", "is", "a", "test", "wouter"]
    min_count = 2
    aDict = lyrics_to_frequencies(lyrics)
    result = word_count(aDict, min_count)
    print(print_result(result))

def lyrics_to_frequencies(lyrics):
    aDict = {}
    for word in lyrics:
        if word in aDict:
            aDict[word] += 1
        else :
            aDict[word] = 1
    return aDict

def most_common_words(aDict):
    count = aDict.values()
    highest_count = max(count)
    list_words = []
    for word in aDict:
        if aDict[word] == highest_count:
            list_words.append(word)
    return (list_words, highest_count)

def word_count(aDict, min_count):
    result = []
    done = False
    while not done:
        common_words = most_common_words(aDict)
        if common_words[1] >= min_count:
            result.append(common_words)
            for words in common_words[0]:
                del(aDict[words])
        else :
            done = True
    return result

def print_result(result):
    for i in range (len(result)):
        print(result[i][0], "appears", result[i][1], "times")


if __name__ == '__main__':
    main()