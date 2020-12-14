def eligibility_for_vote(age):
    if age >= 18:
        print("eligible for vote")
    else:
        print("not eligible for voting")
age = int(input("enter age"))
eligibility_for_vote(age)