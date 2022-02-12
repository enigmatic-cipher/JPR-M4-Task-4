"""
Given a string as input, print the index of the first and second occurrence of T in the string.
Input-> "MATTERS"
Output-> First:2 Second:3
"""

st = "MATTERS"
ln = len(st)
ls = ['first', 'second']
ln1 = len(ls)
for i in range(0,ln):
  ch = st[i]
  if (ch=="T"):
    for j in range(ln1):
      ch2 = ls[j]
      print(f"{ch2} = {i}")
