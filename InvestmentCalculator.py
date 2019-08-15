# ========== Introduction to programming Task 12 ==============
# ========== JOHNSON TEMILOLA === [13TH MARCH 2019] ===========
# ========== This program calculates the amount, and years that a user wants to invest with the interest rate 

# ======================= PROGRAM DESCRIPTION ===============================================================================================================
# Ask the user to input:
#   The amount that they are depositing, stored as ‘P’.
#   The interest rate (as a percentage), stored as ‘i’.
#   The number of years of the investment. stored as ‘t’.
#   Then ask the user to input whether they want “simple” or “compound” interest, and store this in a variable called ‘interest’.
# Only the number of the interest rate should be entered - don’t worry about having to deal with the added ‘%’,
# e.g. The user should enter 8 and not 8%.
# Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get after the given period at the interest rate.
# Print out the answer!
# Try enter 20 years and 8 (%) and see what a difference there is depending on the type of interest rate!
# ===========================================================================================================================================================




import math

# Get user's input of the  amount, years, percentage interest an interest type and stores in the variables
p = float(input("Please enter the amount you want to deposit:R "))
i = float(input("The percentage interest: "))
t = int (input("Enter the number of years of investment: "))
interest_type = (input("enter your prefered interest type (simple or compound): ")).lower()

    
# To determines the amount of a user receives after a period of investing based on the type of interest the user chooses
# Simple interest type is calculated as:  a = p *(1 + (i/100) * t)
# Compound interest type is calculated as:  a = p * math.pow((1 + (i/100)), t)

if interest_type == "simple":
    a = p * (1 + (i/100) * t)
    print ("The amount received after a period of {0}-year = R ".format(t), a)
elif interest_type == "compound":
    a = p * math.pow((1 + (i/100)), t)
    print ("The amount received after a period of years of {0}-year = R ".format(t), round(a, 2))

else:
    print ("Invalid Interest type")









