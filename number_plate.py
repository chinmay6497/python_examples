plate=input("Enter  number plate here:")

# if len(plate)==6 and plate[0]>='A' and plate[0]<='Z' and plate[1]>='A' and plate[1]<='Z' and plate[2]>='A' and plate[2]<='Z' and plate[3]>=0 and plate[3]<=9 and plate[4]>=0 and plate[4]<=9 and plate[5]>=0 and plate[5]<=9:
#     print("Number plate is older")

# elif len(plate)==7 and plate[0]>=0 and plate[0]<=9 and plate[1]>=0 and plate[1]<=9 and plate[2]>=0 and plate[2]<=9 and plate[3]>=0 and plate[3]<=9 and plate[4]>='A' and plate[4]<='Z' and plate[5]>='A' and plate[5]<='Z' and plate[6]>='A' and plate[6]<='Z':
#     print("Number plate is Newer")

# else:
#     print("Enter valid Number")

# if plate[0].isalpha and plate[0].isupper and plate[1].isalpha and plate[1].isupper plate[2].isalpha and plate[2].isupper:
#     print('Valid')


# if plate[0].isalpha and plate[0].isupper:
#     print('Valid')

# else:
#     print('Invalid')

for i in plate[:3]:
    if i.isupper() and i.isalpha():
        print('Valid')

    else:
        print('Invalid')