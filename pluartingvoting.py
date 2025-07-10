candidates = int(input("How many candidates? ").strip())
votes = {}

for i in range(candidates):
    name = input(f"Enter the name of candidate {i + 1}: ").strip()
    votes[name] = 0
    
no_of_voters = int(input("Enter the number of voters: ").strip())
    
for voter in range(no_of_voters):
    vote = input(f"Voter {voter + 1}, Enter the name of candidate you vote for: ")
        
    if vote in votes:
        votes[vote] += 1
    elif vote not in votes:
        print(f"Invalid candidate {vote} , it will not consider!")

print("Votes recieved by each candidate:")
for candidate, count in votes.items():
    print(f"{candidate} : {count} votes")

max_votes = max(votes.values())

winner = []
for name, count in votes.items():
    if count == max_votes:
        winner.append(name)
if len(winner) == 1:
    print(f"Winner(s): {winner[0]}")
elif len(winner) > 1:
    print(f"Tie between:")
    for winner in winner:
        print(winner)