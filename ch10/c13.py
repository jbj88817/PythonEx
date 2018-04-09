import re

s = "Hey there,\tthis is a very \"good\" example! Some say it's \"great.\""

r = re.findall("\w+'\w+|\w+", s)
print(r)
