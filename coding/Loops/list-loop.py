countries=["India", "United State", "Australia", "Ireland", "Sri Lanka", "Iceland", "Cuba", "Iran", "Poland"]

# Count all the countries which are starting with I.
# Also print the list of those countries.
count=0
print("Countries starting with I are: ")
for i in countries:
    if (i[0]=="I"):
        count= count+1
        print(i, end=" ")
print(f"\ncount: {count}")