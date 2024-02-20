import re

pattern = re.compile("^(a+)+$")

def check(input):
    return bool(pattern.match(input))
    
check("a" * 3000 + "!")