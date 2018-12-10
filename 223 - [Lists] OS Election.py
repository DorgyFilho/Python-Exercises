#227 - OS Election


OS = ['Win 10', 'Ubuntu', 'Mac OS']
OSVotes = [0]*3
print(OSVotes)
total = 0
print("In your opinion, what is the best OS?\n1-Win 10\n2-Ubuntu\n3-Mac OS\n0-Exit")

vote = ''
while vote != 0:
    vote = int(input('Vote: '))
    if not (1 <= vote <= 3):
        print('Options: 1-Win 10, 2-Ubuntu, 3-Mac OS')
    if vote == 0:
        print('End of Elections')
        break
    OSVotes[vote-1] += 1
    total += 1

i = 0
mostVoted = 0
for sys in range(len(OS)):
    print('{} ---- {} votes ---- {:.2f}%'.format(OS[i], OSVotes[i], (OSVotes[i]/float(total)*100)))
    print()
    if OSVotes[i] > OSVotes[mostVoted]:
        mostVoted = i
    i += 1
print('Total of Votes: {}'.format(total))

print('The Winner is {}'.format(OS[mostVoted]))






