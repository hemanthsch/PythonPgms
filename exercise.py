'''Yahtzee Score Calculator'''

def yahtzee_score_calc(lst):
	combinations = {
		0: lambda x: x.count(1),
		1: lambda x: x.count(2)*2,
		2: lambda x: x.count(3)*3,
		3: lambda x: x.count(4)*4,
		4: lambda x: x.count(5)*5,
		5: lambda x: x.count(6)*6,
		6: lambda x: sum(x) if any(x.count(i)>=3 for i in set(x)) else 0,
		7: lambda x: sum(x) if any(x.count(i)>=4 for i in set(x)) else 0,
		8: lambda x: 25 if len(set(x))==2 and any(x.count(i)==2 for i in set(x)) else 0,
		9: lambda x: 30 if any(i.issubset(x) for i in [{1,2,3,4},{2,3,4,5},{3,4,5,6}]) else 0,
		10: lambda x: 40 if set(x) in ({1,2,3,4,5},{2,3,4,5,6}) else 0,
		11: lambda x: 50 if len(set(x))==1 else 0,
		12: lambda x: sum(x)}

	score = 0
	for i in range(len(lst)):
		if i == 7:
			if score >= 63:
				score += 35
		score += combinations[i](lst[i])
	return score

out=yahtzee_score_calc([
	[1, 3, 1, 1, 2], # Aces
	[1, 2, 4, 5, 6], # Twos
	[6, 3, 4, 3, 4], # Threes
	[3, 1, 1, 4, 4], # Fours
	[5, 5, 5, 5, 3], # Fives
	[6, 2, 6, 6, 6], # Sixes
	[1, 4, 4, 2, 1], # Three of a Kind
	[3, 3, 3, 3, 3], # Four of a Kind
	[2, 2, 1, 1, 2], # Full House
	[6, 1, 2, 3, 4], # Lower Straight
	[2, 3, 5, 4, 1], # Higher Straight
	[4, 4, 4, 4, 4], # Yahtzee
	[3, 3, 4, 5, 6], # Chance
])
print(out)