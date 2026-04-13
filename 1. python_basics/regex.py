
import re

# get numbers using regex
text = "contact me at 123-456-789"
nums1 = re.findall(r"\d",text)
nums2 = re.findall(r"\d+",text)
print(nums1)
print(nums2)

# Substitute
replaced= re.sub(r"\d","X",text)
print(replaced)