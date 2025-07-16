def func(strs):
    anagram = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagram:
            anagram[sorted_s] = []
        anagram[sorted_s].append(s)
    return list(anagram.values())



print(func(["act","pots","tops","cat","stop","hat"]))