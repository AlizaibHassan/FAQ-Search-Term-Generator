from bs4 import BeautifulSoup
import random


def FixCase(st):
    return ' '.join(''.join([w[0].upper(), w[1:].lower()]) for w in st.split())


f = open('input.txt')
line = f.readline()


cntr=1

while line:
    
    base_modifiers="""
How to MODIFIER,
What MODIFIER,
Can MODIFIER,
Will MODIFIER,
Which MODIFIER,
How do you MODIFIER,
What is the difference between MODIFIER,
Pros and cons of MODIFIER,
Why does MODIFIER,
How to fix MODIFIER,
Will MODIFIER,
Is MODIFIER,
Are MODIFIER,
Can MODIFIER,
Why do MODIFIER,
Why does MODIFIER,
Why don't MODIFIER,
Why doesn't MODIFIER,
Why isn't MODIFIER,
Where do MODIFIER,
When do MODIFIER,
Why can't MODIFIER,
How do MODIFIER,
How much MODIFIER,
How many MODIFIER,
Isn't MODIFIER,
Aren't MODIFIER,
What if a MODIFIER,
When to use MODIFIER,
Should you MODIFIER,
How to make MODIFIER,
What to do if MODIFIER,
How to use MODIFIER,
Best MODIFIER,
How to fix MODIFIER,
Best way to use MODIFIER,
Prevent MODIFIER,
How often does MODIFIER,
Improve MODIFIER,
Best way to MODIFIER,
Cheapest MODIFIER,
MODIFIER vs,
MODIFIER alternatives,
MODIFIER Ideas for,
MODIFIER Tips for,
MODIFIER can't,
MODIFIER doesn’t,
MODIFIER won't,
MODIFIER problem with,
MODIFIER step by step,
MODIFIER Stopped,
MODIFIER Quit,
MODIFIER Started to,
MODIFIER Sounds,
MODIFIER ideas,
Is MODIFIER worth it,
Best MODIFIER for,
"""
   

    line=line.replace('\n','')
    base_modifiers=base_modifiers.replace("MODIFIER",line)
    name=line

    name=str(cntr)+"_"+name+".csv"
    name="output/"+name

    f2 = open(name,'w+')
    f2.write(base_modifiers)
    f2.close()

    line = f.readline()
    cntr+=1


print("Done!")
f.close()