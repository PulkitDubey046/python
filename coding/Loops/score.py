score=[2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]

# total score
total_score=0
for i in score:
    total_score+=i
print(f"total run: {total_score}")

# highest score
high=score[0]
for i in score:
    if(high<i):
        high=i
print(f"Higest score: {high}")

# we can find using max()
print(max(score))


# lowest score
low=score[0]
for i in score:
    if(low>i):
        low=i
print(f"Lowest score: {low}")

# we can find using min()
print(min(score))