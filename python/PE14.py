i = 2
supIndex = 0
sup = 0
while(i < 1000000):
	j = i
	k = 1
	while(j != 1):
		if(j % 2 == 0):
			j = j/2
			k = k + 1
		else:
			j = 3*j + 1
			k = k + 1
		k = k + 1
	if(supIndex < k):
		supIndex = k
		sup = i
	i = i + 1
print sup