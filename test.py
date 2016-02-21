import logic
import parser

url = raw_input("enter url: ")
tgt = raw_input("what word don't you want to see?: ")

txt = parser.extract(url)
trigs,percent = logic.similar_words(tgt, txt)

print trigs
print percent
