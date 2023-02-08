# we use this operator when we have multiple conditions

has_high_income = True
has_good_credit = True

# this is AND operator always print if both conditions are true
if has_high_income and has_good_credit:
    print("Eligible for loan")

# here is the OR operator which prints if one of the condition is true
has_high_income =False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")
has_good_credit = True
has_criminal_record = False

# not operate negate the false statement to be true
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
