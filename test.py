import logic
import parser

url = raw_input("enter url: ")
tgt = raw_input("what word don't you want to see?: ")

txt = parser.extract(url)
txt = txt.split()
trigs = logic.trigger(txt, tgt)
print logic.trig_stats(txt, trigs)
