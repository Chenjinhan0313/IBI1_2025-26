#verify the age,weight,gender,Cr concentration,and then calculate the CrCl()
age=int(input("Age(years):" ))
#if age is not in the correct range,remind the user
if age>=100:
    print("Age must be less than 100")
else:
    #if age is in the correct range,let the user to input weight
    weight=float(input("Weight(kg):"))
    #if weight is not in the correct range,remind the user
    if weight<=20 or weight>=80:
        print("Weight must be between 20 kg and 80 kg")
    else:
        gender=input("Gender(male/female):")
        #if gender is not typed in correct form,remind the user
        if gender!="male" and gender!="female":
            print("Gender muust be 'male' or 'female'")
        else:
            Cr=float(input("Creatine concentration(umol/l):"))
            #if Cr concentration is not in the correct range,remind the user
            if Cr <=0 or Cr >=100:
                print("Creatine concentration must be between 0 and 100 umol/l")
            else:
                #calculate creatine concentration accrodding to the equationc
                CrCl=((140-age)*weight)/(72*Cr)
                #if gender is female,adjust the CrCl concentration
                if gender=="female":
                    CrCl=CrCl*0.85
                print("Age:"+str(age)+"years")
                print("Weight:"+str(weight)+"kg")
                print("Gender:"+gender)
                print("Creatine Concentration:"+str(CrCl)+"umol/l")
