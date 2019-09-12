# ========== Introduction to programming Task 9 =====================
# ========== JOHNSON TEMILOLA ===== [13TH MARCH 2019] ===============

''' =================== Program description ============================
  
 Designing a program for a courier company to calculate the cost of sending a parcel.
 Ask the user to enter the price of the package they would like to purchase.
 Ask the user to enter the total distance of the delivery in km’s.
 Now add on the delivery costs to get the final cost of the product.
 There are four categories to factor in when determining a parcel’s final cost each with two options based on their delivery preferences. (Use an if else statement based on the choice they make)
       - Air R0.36 per Km or freight R0.25 per Km
       - Full insurance R50 or limited insurance R25
       - Gift R15.00 or no gift R0.00
       - Priority R100 or standard delivery R20
 Work out the total cost of the package based on the selection in each category.
'''

# assign the cost value to each variable
total_cost = 0
full_insurance = 50
limited_insurance = 25
userGift = 15
noGift = 0.00
standard_del = 20
priority_del = 100

# request user input to choose their prefered delivery 'Air or Freight'
# request user to enter the distance in kms
user_choice = input("Would you like Air or Freight delivery? ").lower()
total_distance = int(input("Enter the total distance of delivery in (km's): "))

# If the user choice equals 'air'
#    total_cost is  equal to  total_cost multiply by air cost per km's
#    print total cost

if user_choice == "air":
    total_cost = total_distance * 0.36
    print (round(total_cost, 2))

# If user choice is Freight
#   total_cost is  equal to  total_cost multiply by freight cost per km's
#   print total cost of freight
else:
    total_cost = total_distance * 0.25
    print (round(total_cost, 2))

# Request the user if they want the Full or Limited insurance
# if insurance cover is equal to 'full'
#      total cost is equal to total cost plus full insurance cost
#      print total cost added with the full insurance
# else
#    total cost is equal to total cost plus limited insurance cost


insurance_cover = input("Would you like the Full or Limited insurance? ").lower()
if insurance_cover == "full":
    total_cost += full_insurance
    print ("Total cost of sending percel on full insurance = R", round(total_cost, 2))
else:
    
    total_cost += limited_insurance
    print ("Total cost of sending percel on limited insurance = R", round(total_cost, 2))

# Request the user if they want to include gift or not
# if user gift is equal to 'gift'
#      total cost is equal to total cost plus 'gift' cost
#      print total cost added with the gift cost
# else
#    total cost is equal to total cost plus 'no gift' cost

user_gift = input("Would you like to include the of Gift or No-Gift? ").lower()
if user_gift == "gift":
    total_cost += userGift
    print (round(total_cost, 2))
else:
    
    total_cost += noGift
    print ("The Total cost of sending your percel = R", round(total_cost, 2))


# Request the user if they want 'Priority' or 'Standard' delivery
# if user prior is equal to 'priority'
#      total cost is equal to total cost plus 'priority' cost
#      print total cost added with the gift cost
# else
#    total cost is equal to total cost plus 'standard' cost

user_prior = input("Would you like the Priority or standard delivery? ").lower()
if user_prior == "priority":
    total_cost += priority_del
    print ("The Total cost of sending your percel = R", round(total_cost, 2))

else:
    total_cost += standard_del
    print ("The Total cost of sending your percel = R", round(total_cost, 2))

    
