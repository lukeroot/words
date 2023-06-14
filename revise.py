import re
old = open('words.txt', 'r')
new = open('words-revised.txt', 'w')
while w:=old.readline():
	w1=w.lower()
	if not re.match(r'^[a-z]{3,8}$', w1):
		continue
	dupe = 0
	prev = ''
	skip = 0
	for i in range(0, len(w1) - 1):
		if prev and prev == w1[i]:
			dupe+=1
		else:
			dupe=0
		prev = w1[i]
		if dupe == (len(w1) - 2) % 3:
			skip = 1
			continue
	if skip:
		continue
	new.write(w1.capitalize())
