ed_scores = [1, 3, 5, 4, 5, 2]
jay_scores = [2, 3, 1, 1, 5, 1] 
print(ed_scores)
# sorted(ed_scores) doesnt do anything
# ed_scores.sort() 
print(sorted(ed_scores)) # This one works though
print(sorted(jay_scores, reverse=True))


# print(ed_scores)
# for scores in ed_scores:
#     for scores in jay_scores:
#         print(f"Ed's scores {ed_scores[:3]}")
#     print(f"Jays scores {jay_scores[0:3]}")