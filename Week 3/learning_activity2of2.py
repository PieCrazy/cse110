
# and statments
 
# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('Well done')
# # can be an and statement.
# if gpa >= .85 and lowest_grade >= .70:
#     print('Well done')


#boolean varibles as flags
#
# on the true and makes ure no "" or '' on those indicate boolean varible
#you can do this so you don't have to ask over and over again on if stements.
# if gpa >= .85 and lowest_grade >= .70:
#     honor_roll = True  # caps is important here on the true and flase
# else:
#     honor_roll = False
# #somewher later in code
# if honor_roll:
#     print('Well done')



# True and False values
# In addition to comparing against other variables, you can also set a variable
# itself to be a True or False. To this point, we have learned about the variable 
# types of int, float, and string. Variables that are either true or false are a
# new data type called Boolean variables (named after a mathematician, George Boole).

# You can set a boolean variable directly, such as is_hot = True or is_hot = False.
# Notice that you must always use a capital T on True and a capital F on False.

# Because these variables are already either true or false, you don't need to 
# compare them against another value.



#  Testing Multiple Similar Conditions
# It is common to want to test the same variable for two conditions, or to test two variables against the same condition. In these cases, you may be tempted to leave part out, but this will not work, anytime you use operators like > or ==, you must provide both a left and a right hand side for it.


# # To check if x is either 5 or 6, you might be tempted to write:
# if x == 5 or 6:
#     # INCORRECT: This does not work!

# # You must write them both out:
# if x == 5 or x == 6:
#     # This is the correct way to check

# # To check if either first_name or last_name is Scott you might be tempted to write:
# if first_name or last_name == "Scott":
#     # INCORRECT: This does not work!

# # You must write them both out:
# if first_name == "Scott" or last_name == "Scott":
#     # This is the correct way to check


# Activity Instructions
# For this activity, you will implement a simplistic system to determine if a user can qualify for a loan.

# The Problem: Qualifying for a loan
# When loaning money to someone, you want to have some level of confidence that they will be able to repay the loan.

# There are different characteristics you might base this decision on,
#   or different questions you might ask someone.
#   And depending on their answers to those questions, you might ask other questions. 
#   For example, consider the following possible questions:

# Does the person have a job, and if so, how long have they worked there,
# and how much money do they make?

# Is there good collateral for the loan? 
# (for example, is the loan against a car or home that is worth 
# at least the amount of the loan?)

# Does the person have a good credit score or history of paying back loans?

# How much other debt does the person have?

# How much money does the person have?

# Will the person have a down payment, and if so, what percentage of the loan 
# does it amount to?

# Program Specification
# Write a program to determine whether to loan money based on the following rules.

# First, ask for a rating from 1–10 on the following:

# How large is the loan?

# How good is your credit history?

# How high is your income?

# How large is your down payment?

# Then, you will create a boolean variable for whether you should loan the 
# money that will be set to either True or False. Set up a series of if 
# statements to decide if your decision to loan is "yes" or "no" according to 
# the following rules:

# First, check if the loan size is at least 5. If it is, use the following rules:

# If the credit history and income are both at least 7, then the decision is "yes"

# If either the credit history or income is at least 7, then check if
# the down payment is at least 5, if it is, the decision is "yes", if not, 
# the decision is "no"

# Otherwise (if neither the credit history nor income is at least 7), 
# the decision is "no"

# Otherwise (if the loan is not 5 or greater), use these rules:

# If the credit is less than 4, then the decision is "no"

# Otherwise, check the following:

# If either the income or the down payment is at least 7, the decision is "yes"

# If both the income and the down payment are at least 4, then the answer is "yes"

# Otherwise, the decision is "no"

# # Finally, display the decision to the user.






#The Problem: Qualifying for a loan

print('To get a loan we need to get some information from you to see if you qualify. ')
print()
print('We are going to ask you to rate the following quesions. \n Rating from 1-10 on the following')
loan_size_r = int(input('How large is the loan? '))
credit_history_r = int(input('How good is your credit history? '))
income_r = int(input('How high is your income? '))
downpayment_r = int(input('How large is your downpayment? '))
give_loan = True
# going to try this in more than one way
if loan_size_r >= 5:
    if credit_history_r >= 7 and income_r >=7:
        give_loan = True
    elif credit_history_r >= 7 or income_r >=7:
        if downpayment_r >= 5:
            give_loan = True
        else:
            give_loan = False
    else:
        give_loan = False
else:
    if credit_history_r < 4:
        give_loan = False
    else:
        if income_r >= 7 or downpayment_r >= 7:
            give_loan = True
        elif income_r >= 4 and downpayment_r>= 4:
            give_loan = False
        else:
            give_loan = True
#what to print

if give_loan:
    print('You qualify for a loan.') 
else:
    print('You do not qualify for a loan')
        

    