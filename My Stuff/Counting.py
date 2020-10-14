import time
skipWhat = int(input('Tell me a number: '))
i = 1
print()
while True:
    a = i % skipWhat
    if a is 0: print('\nShhhh!\n')
    else: print(i,'\n')
    time.sleep(1)
    i += 1