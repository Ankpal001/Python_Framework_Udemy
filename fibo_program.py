#Python program to display all integers within the range 100-200 whose sum of digits is
#1+0+1, 1+2+3
# an even number
#1*2*3*4*5
#i*i+1*i+2*i+3*i+4(i+0)*(i+1)*(i+2)*(i+3))
sum = 1
x = int(input('Please ent the num: '))
for i in range(1,x+1):
    sum = sum*(i)#1*(2), 2*(4)#(5-1)*(5-2)
    print(sum)





