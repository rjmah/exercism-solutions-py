def detect_anagrams(word, anas):
    return [ana for ana in anas if word.lower() != ana.lower() and sorted(word.lower()) == sorted(ana.lower())]