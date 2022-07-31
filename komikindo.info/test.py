from cgitb import text
import re

a = "the girl from random chatting    !"
b = "not a friend’s"

new = ''.join(filter(str.isalnum,a))
print(new)

new2 = re.sub(r'[^a-zA-Z0-9 ]', "", b)
new2 = "-".join(new2.split())
print(new2)
