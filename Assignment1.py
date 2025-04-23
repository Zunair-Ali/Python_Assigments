# 1 Assignment of Python class
import math

# Calculate the final amount with compound interest (for 1 year, compounded annually)
P = 5000
R = 8
T = 1
A = P * (1 + R/100) ** T
print("Final Amount after 1 year:", A)

# Find the total surface area of a cylinder
radius = 7
height = 10
tsa = 2* math.pi* radius**2 + 2* math.pi*radius*height
print("Total Surface Area of a Cylinder",round(tsa,3))

# Convert time into total seconds
hours = 2  
minutes = 46 
seconds = 40 
total_second = (hours*3600 + minutes*60 + 40)
print("Time into Total Seconds is",total_second)

# Split a restaurant bill including tip
bill = 2750
tip = 10
Number_of_people = 5
total_tip = bill* tip/100
total_amount = (bill+total_tip)/Number_of_people
print("Each Person Pays",total_amount)


# Calculate weighted average marks
math_score = 80
math_weight = 3
physics_score = 75
physics_weight = 4
chemistry_score = 70
chemistry_weight = 3

total_weighted_score = (math_score * math_weight) + (physics_score * physics_weight) + (chemistry_score * chemistry_weight)
total_weights = math_weight + physics_weight + chemistry_weight
weighted_average = int(total_weighted_score / total_weights)
print("Weighted Average Marks:", weighted_average)

# Convert speed from km/hr to m/sec and then calculate time to cover a certain distance
Speed = 72
distance = 500
total_speed = Speed*1000/3600
speed_mps = Speed * 5 / 18
time = int(distance // total_speed)
print("Speed in m/s:", speed_mps)
print("Cover a certain distance",time, "seconds")

# Calculate effective discount after two successive discounts
price = 1000
first_discount = 10 
second_discount = 5 
price_after_first = price * (1 - first_discount // 100)
final_price = price_after_first * (1 - second_discount // 100)
total_discount = int(price - final_price)
print("Final Price after successive discounts:", final_price)
print("Total Discount:", total_discount)


# Calculate the average of 5 numbers after increasing each by 10%
num_1 = 100
num_2 = 200
num_3 = 300
num_4 = 400
num_5 = 500
average_number = (100*10//100)+100, (200*10//100)+200, (300*10//100)+300, (400*10//100)+400, (500*10//100)+500
print("Average of 5 Numbers After Increasing Each by 10%  is",average_number)



# Convert a total number of seconds into hours, minutes, and seconds
# (Use integer division and modulus)
total_seconds = 10000
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


# Calculate the monthly EMI (Simple version)
P = 100000   
annual_rate = 12
T = 1            
N = T * 12  
R = annual_rate / 12 / 100
EMI = P * R * (1 + R)**N / ((1 + R)**N - 1)
print("Monthly EMI:", round(EMI,2))


# ---------------------------------------------------------------------------

# Class Questions

# Find the area of a rectangle
length = 15
breadth = 10
area = length * breadth
print("Area of Rectangle:", area)

# Convert Fahrenheit to Celsius
F = 98.6
C = (F - 32) * 5 / 9
print("Celsius Temperature:", round(C, 2))


# Calculate the total marks and average of 3 subjects
math = 87
science = 92
english = 78

total = math + science + english
average = total / 3

print("Total Marks:", total)
print("Average Marks:", round(average, 2))

# Find the perimeter of a square
side = 12
perimeter = 4 * side
print("Perimeter of Square:", perimeter)

# Calculate simple interest
P = 10000
R = 5
T = 2

SI = (P * R * T) / 100
print("Simple Interest:", SI)

# Convert height from feet to inches
feet = 5.5
inches = feet * 12
print("Height in inches:", inches)

# Calculate the area of a circle
radius = 7
pi = 3.14
area = pi * radius * radius
print("Area of Circle:", area)

# Convert days into hours and minutes
days = 3
hours = days * 24
minutes = hours * 60
print("Hours:", hours)
print("Minutes:", minutes)

# Find the volume of a cube
side = 9
volume = side ** 3
print("Volume of Cube:", volume)

# Calculate BMI (Body Mass Index)
weight = 70
height = 1.75
BMI = weight / (height ** 2)
print("BMI:", round(BMI, 2))