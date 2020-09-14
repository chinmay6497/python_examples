# A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional
# text messages cost $0.15 each. All cell phone bills include an additional charge of
# $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
# subject to 5 percent sales tax.
# Write a program that reads the number of minutes and text messages used in a
# month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only
# display the additional minute and text message charges if the user incurred costs in
# these categories. Ensure that all of the charges are displayed using 2 decimal places

m=float(input("Enter total minute of talk time you have in this month:"))
t=float(input("Enter total minute of text message you have in this month:"))

if m<=50.0 and t<=50:
    y=15*1.05

else:
    x1=m-50
    x2=t-50
    y=(15+(x1*0.25)+(x2*0.15))*1.05


#     if m>50.0:
#         q=0.25*(m-50)
#     elif t>50:
#         z=0.15*(m-50)

# v=y+q+z
# s=0.05*(y+q+z)

print(f"The total Bill for {m} minute talk time and {t} text message is {round(y+0.44,2)}  which include tax and 911 sercies ")