# Scorekeeper for all sports/games

T1 = 0
T2 = 0
t1_diff = T1 - T2
t2_diff = T2 - T1

T1n = input("What is the first team's name?")
T2n = input("What is the second team's name?")

for n in range[5]:
  score = input("Who scored? (T1 or T2)")
  if score == 'T1':
    T1 = T1 + 1
    if T1 > T2:
      print(T1n,'leads with', T1,'.', T2n,'follows with',T2)
    if T2 > T1:
      print(T2n,'leads by',t2_diff,'.', T1n,'follows with',T1)
      
  if score == 'T1':
    T2 = T2 + 1
    if T1 > T2:
      print(T1n,'leads with', T1,'.', T2n,'follows with',T2)
    if T2 > T1:
      print(T2n,'leads by',t2_diff,'.', T1n,'follows with',T1)
      
