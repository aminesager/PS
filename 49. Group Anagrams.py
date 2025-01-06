from collections import defaultdict


def groupAnagrams( strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        key = "".join(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))