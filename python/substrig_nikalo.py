mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"
index = 0
new_mainStr = mainStr.split(subStr)
new_mainStr = new_mainstr.join(replacemenStr)
print new_mainStr
