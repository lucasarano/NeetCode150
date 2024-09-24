class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        myDict = {}
        output = []
        for s in strs:
            sortedString = ''.join(sorted(s))
            if sortedString not in myDict:
                myDict[sortedString] = [s]
            else:
                myDict[sortedString].append(s)
        for i in myDict.values():
            output.append(i)
        return output