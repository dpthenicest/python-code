value = True
count = 0

while value:
  print(count)

  if (count == 5):
    break
  elif count < 5:
    count += 1
  else:
    value = 0
    continue
