# Cricket Match Analysis Tool

target = int(input("Target score: "))
score = int(input("Current score: "))
overs = float(input("Overs bowled: "))
wickets_lost = int(input("Wickets lost: "))

full_overs = int(overs)
extra_balls = round((overs - full_overs) * 10)

balls_bowled = full_overs * 6 + extra_balls
balls_remaining = 300 - balls_bowled

overs_remaining = str(balls_remaining // 6) + "." + str(balls_remaining % 6)

runs_required = target - score
crr = score / (balls_bowled / 6)
rrr = runs_required / (balls_remaining / 6)
wickets_remaining = 10 - wickets_lost

chase_feasible = runs_required <= balls_remaining * 6
chase_comfortable = (rrr <= crr) and (wickets_lost < 7)

print("Balls bowled:", balls_bowled)
print("Balls remaining:", balls_remaining)
print("Overs remaining:", overs_remaining)
print("Runs required:", runs_required)
print("Current run rate:", round(crr, 2))
print("Required run rate:", round(rrr, 2))
print("Wickets remaining:", wickets_remaining)
print("Chase feasible:", chase_feasible)
print("Chase comfortable:", chase_comfortable)