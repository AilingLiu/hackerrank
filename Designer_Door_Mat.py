# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b= map(int, input().split(' '))

knob='.|.'
middle = a//2
gate = ''
for i in range(middle):
    line = (knob*(2*i+1)).center(b, '-')
    gate = gate + line + '\n'

plague = 'WELCOME'.center(b, '-')+'\n'
final = gate + plague + gate[:-1][::-1]
print(final)

