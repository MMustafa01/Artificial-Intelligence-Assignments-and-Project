import math
import random
from turtle import color 
import matplotlib.pyplot as plt

# Using the Algorithm in the slides. 
# There are two fuctions: 
# 1) Simulated Annealing 
# 2) Plotting 

def simulated_annealing(f, extrema, lim_x, lim_y):

    #Getting random value for x and y for current coordinates. 
    x_min, x_max = lim_x
    y_min, y_max = lim_y
    x_ = random.randint(x_min, x_max)
    y_ = random.randint(y_min, y_max)


    #List of all for x,y and function values to be used later for plotting. 
    x_axis =[]
    y_axis =[]
    func_val =[]
 
    #Add coordinates in the list.
    x_axis.append(x_)
    y_axis.append(y_)


    #Updating the variable names to be used in funtion value calculation.
    x =x_
    y = y_

    #Selecting with-in the three given fuctions from the input.
    # 0 == Sphere Function
    # 1 == Rosenbrock Function
    # 2 == Griewank Funtion 

    if f == 0:
        func = -x**2 -y**2     
    elif f == 1: 
        func =  100 *(x-y)**2 + (1-x)**2                                                
    elif f == 2:
        func = (x**2 + y**2)/(4000)- math.cos(x)*math.cos(y/(2)**(1/2)) +1



    #Add the result of the fuction in the funtion value list     
    func_val.append(func)


    #Initialising some temperture, iteration and factor 
    temp = 100
    iter = 50
    factor = 0.5

 
    #Loop to traverse the values for the temperature.
    for i in range(1, temp):
        
        #Loop to traverse the values for the no of iterations.
        for j in range(1, iter):
            

            # x = random.randint(0,7)
            
            #Choosing a random number for our next state.
            new_x = x + (random.choice([+1,-1]))*random.randint(lim_x[0],lim_x[1]) /(lim_x[0]-lim_x[1])
            new_y = y+ (random.choice([+1,-1]))*random.randint(lim_y[0],lim_y[1]) /(lim_y[0] - lim_y[1])


            # if new_x > lim_x[1] or new_x < lim_x[0]:
            #     new_x = new_x/lim_x[0]-lim_x[1]
            # if new_x > lim_x[1] or new_x < lim_x[0]:
            #     new_x = new_x/lim_x[0]-lim_x[1]


 
            #Replacing the updated values of x and y in the fuction. 
            if f == 0:
                func2 = (-(new_x**2)-(new_y**2))
                
            elif f == 1: 
                func2 =  100 *(new_x-new_y)**2 + (1-new_x)**2
                
            else:
                func2 = (new_x**2 + new_y**2)/(4000)- math.cos(new_x)*math.cos(new_y/(2)**(1/2)) +1


            
            #Change in energy calculated to be compared.
            energy_delta = func -func2
            

            #Comparing values to see if we should go ahead or not. 
            #For Maxima 
            if extrema == 1:
                if energy_delta > 0: 
                    func = func2 
                    func_val.append(func)
                    x= new_x
                    y= new_y 
                    x_axis.append(new_x)
                    y_axis.append(new_y)
                else: 

                    #Comparing with probablity 
                    if random.uniform(0,1) < math.exp(energy_delta/temp): 
                        func = func2
                        func_val.append(func)
                        x= new_x
                        y= new_y  
                        x_axis.append(new_x)
                        y_axis.append(new_y)

            #For Minima 
            elif extrema == 0 : 
                if energy_delta < 0: 
                    func = func2
                    func_val.append(func)
                    x= new_x
                    y= new_y 
                    x_axis.append(new_x)
                    y_axis.append(new_y)
                else: 

                    #Comparing with probablity 
                    if random.uniform(0,1) < math.exp(-energy_delta/temp):
                        func = func2
                        func_val.append(func)
                        x= new_x
                        y= new_y 
                        x_axis.append(new_x)
                        y_axis.append(new_y)
            i =+ 1 
        temp = factor * temp 

    res = [func, func_val,x_axis,y_axis]
    # print(res)
    return res 





def plotting (x_axis, y_axis, func_val):

    #Ploting the graph 
    fig, a = plt.subplots(2)
    a[0].plot(func_val,color='red',label ='Objective ',  **{'marker':'.'})
    a[0].legend()
    a[1].plot(x_axis,color ='blue',label ='X', **{'marker':'.'})
    a[1].plot(y_axis,color='green',label ='Y',linestyle='dashed',  **{'marker':'.'})
    a[1].legend()
    plt.show()



##--------TESTING------------## 
# res = simulated_annealing(0,1, [-5,5], [-5,5])   
res = simulated_annealing(0,0, [-5,5], [-5,5])
# res = simulated_annealing(1,1, [-2, 2], [-1, 3])
# res = simulated_annealing(1,0, [-2, 2], [-1, 3])
# res = simulated_annealing(2,1, [-5,5], [-5,5])
# res = simulated_annealing(2,0, [-2, 2], [-1, 3])
l_val = res[0]
print(l_val)
function = res[1] 
plotting(res[2],res[3],res[1])
##---------------------------##





    




    
        

