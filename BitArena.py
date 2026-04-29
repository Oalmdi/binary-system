Teams = ["Al Hilal","Al Nassr","Al Ittihad","Al Ahli","Al Shabab","Al Ettifaq","Al Fateh",
         "Al Fayha","Al Raed","Al Taawoun","Abha Club","Al Tai","Al Hazem","Al Okhdood",
         "Al Khaleej","Damac FC","Al Wehda","Al Riyadh"]
result = ["Win","Loss","Draw","Cansel"]
Stadium = ["Team 1","Team 2"]
Tournament = ["Roshen league","Kings cup","Super cup","cup"]
Referee = ["referee Saudi","referee foreign"]


x =int(input("Enter Match number :"), 16)





Team1_mask = 0b0000_0000_0001_1111
Team2_mask = 0b0000_0011_1110_0000
result_mask = 0b0000_1100_0000_0000
Stadium_mask =0b0001_0000_0000_0000
Tournament_mask =0b0110_0000_0000_0000
Referee_mask = 0b1000_0000_0000_0000



Team_1 = x & Team1_mask
Team_2 = (x & Team2_mask) >> 5
result1 = (x & result_mask) >> 10
Stadium1 = (x & Stadium_mask) >> 12
Tournament1 = (x & Tournament_mask) >> 13
Referee1 = (x & Referee_mask) >> 15


if Team_1 >= len(Teams) or Team_2 >= len(Teams) or  Team_1 == Team_2:
    print("UNABILBLE TEAM")
else:
    print("Team 1 : ", Teams[Team_1])
    print("Team 2 : ", Teams[Team_2])
    print("Result : ", result[result1])
    print("Stadium:", Stadium[Stadium1])
    print("Tournament:", Tournament[Tournament1])
    print("Referee :", Referee[Referee1])





