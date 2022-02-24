for _ in range(int(input())):
  s = input()
  sefr = s.count('0')
  yek  = s.count('1')
  if sefr > yek :
    print (yek)
  elif sefr < yek:
      print(sefr)
  else:
      print("0")