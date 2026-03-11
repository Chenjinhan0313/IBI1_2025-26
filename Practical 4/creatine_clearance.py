age=int(input("Age(years):" ))
if age>=100:#if age is not in the correct range,remind the user
    print("Age must be less than 100")
else:
    weight=float(input("Weight(kg):"))
    if weight<=20 or weight>=80:#if weight is not in the correct range,remind the user
        print("Weight must be between 20 kg and 80 kg")
    else:
        gender=input("Gender(male/female):")
        if gender!="male" and gender!="female":#if gender is not typed in correct form,remind the user
            print("Gender must be either ‘male’ or ‘female’")
        else:
            Cr=float(input("Creatine concentration(umol/l):"))
            if Cr <=0 or Cr >=100:#if Cr concentration is not in the correct range,remind the user
                print("Creatine concentration must be between 0 and 100 umol/l")
            else:
                CrCl=((140-age)*weight)/(72*Cr)
                if gender=="female":#if gender is female,adjust the CrCl concentration
                    CrCl=CrCl*0.85
                print("Age:"+str(age)+"years")
                print("Weight:"+str(weight)+"kg")
                print("Gender:"+gender)
                print("Creatine Concentration:"+str(CrCl)+"umol/l")