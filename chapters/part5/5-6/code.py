# 집합
baseball_teams = {'Dangers', 'Giants', 'Padres', 'Rockies'}
football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}

baseball_teams.add('Yankees')
football_teams.update(['Patriots', 'Jets'])
print(baseball_teams)
print(football_teams)

print(baseball_teams.union({1, 2})) # |
print(baseball_teams.intersection(football_teams)) # &
print(baseball_teams.difference(football_teams)) # -
print({'Padres', 'Yankees'}.issubset(baseball_teams)) # <=
  