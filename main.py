year=int(input('Enter the year'))
if(year%4==0)and(year%100!=0):
  print(f'the given {year} is leap year ')
else:
  print(f'the given {year} is not leap year')
