print('this is calorie and mantainence calorie calculator  ')
a = input('do you want to calculate your maintanence calorie (answer y for yes and n for no) ')
if(a=='y'):
    age = int(input('enter your age '))
    h = float(input('enter your height in cm '))
    w = float(input('enter your weight in kg '))
    g = input('enter m for male and f for female ')
    print('enter your activity level')
    print('press (s) for Sedentary: Little to no exercise')
    print('press (m) for Moderately active: Moderate exercise/sports 3–5 days per week  ')
    print('press(va) for  Very active: Hard exercise/sports 6–7 day; ')
    print('press(sa) Super active: Very hard exercise/sports and a physical job ')
    
    ex = input('enter your input')
    if(g=='m'):
        mc = (10*w)+(6.25*h)-(5*age)+5
        
    elif(g=='f'):
        mc = (10*w)+(6.25*h)-(5*age)-161
        
    else:
        print('invalid input')
        

    if(ex=='s'):
        mc = mc*1.2
    elif(ex=='l'):
        mc = mc*1.375
    elif(ex=='m'):
        mc = mc*1.55
    elif(ex=='va'):
        mc = mc*1.725
    elif(ex=='sa'):
        mc = mc*1.9
    else:
        print('invalid input')
        

    print('your maintainence calories is',mc)

elif(a=='n'):
    print('ok ')
else:
    print('invalid input')

    
        

t = 0
tm = int(input('how many meals you had today '))
meal = 1
while meal<=tm:
    m = (f'what did you have for meal {meal} ')
    m1 = input(str(m))
    c1 = int(input('how many calories was it '))
    with open('calorie.txt','a') as q1:
        q1.write(m1)
        q1.write(' : ')
        q1.write(str(c1))
        q1.write('\n')
    meal+=1
    t  =t+c1
    


r = open('calorie.txt','r')
re = r.read()
print(re)
  
if(a=='y'):
    if(t<mc):
        print('you are in a deficeit you will lose weight')
        defi = mc-t
        lw = defi/7.7
        print('you will loss ',lw,'grams in one day',(lw/1000),'kg in one day')
        print('and ',(lw/1000)*7,'kg in 1 week')
    else:
        print('you are in a calorie surplus you will gain weight')
        defi = t-mc
        lw = defi/7.7
        print('you will gain ',lw,'grams in one day or',(lw/1000),'kg in one day') 
        print('and ',(lw/1000)*7,'kg in 1 week')

r.close()


