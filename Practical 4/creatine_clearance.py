# Pseudocode:
# 1. Ask user for age (years)
# 2. IF age >= 100 THEN display error and stop
# 3. Ask user for weight (kg)
# 4. IF weight <= 20 OR weight >= 80 THEN display error and stop
# 5. Ask user for gender (male/female)
# 6. IF gender is NOT "male" AND NOT "female" THEN display error and stop
# 7. Ask user for creatinine concentration (umol/L)
# 8. IF Cr <= 0 OR Cr >= 100 THEN display error and stop
# 9. Calculate CrCl using formula: ((140 - age) * weight) / (72 * Cr)
# 10. IF gender is "female" THEN multiply CrCl by 0.85
# 11. Display the calculated CrCl value with appropriate units
# Input age
age = int(input("Age (years): "))
if age >= 100:
    print("Error: Age must be less than 100 years.")
else:
    # Input weight
    weight = float(input("Weight (kg): "))
    if weight <= 20 or weight >= 80:
        print("Error: Weight must be between 20 kg and 80 kg (excluding 20 and 80).")
    else:
        # Input gender
        gender = input("Gender (male/female): ").lower()
        if gender != "male" and gender != "female":
            print("Error: Gender must be 'male' or 'female'.")
        else:
            # Input creatinine concentration
            Cr = float(input("Creatinine concentration (umol/L): "))
            if Cr <= 0 or Cr >= 100:
                print("Error: Creatinine concentration must be between 0 and 100 umol/L (excluding 0 and 100).")
            else:
                # Calculate CrCl using Cockcroft-Gault equation
                CrCl = ((140 - age) * weight) / (72 * Cr)
                # Adjust for female
                if gender == "female":
                    CrCl = CrCl * 0.85
                # Display results
                print("\n--- Results ---")
                print("Age: " + str(age) + " years")
                print("Weight: " + str(weight) + " kg")
                print("Gender: " + gender)
                print("Creatinine Concentration: " + str(Cr) + " umol/L")
                print("Creatinine Clearance (CrCl): " + str(round(CrCl, 2)) + " ml/min")#verify the age,weight,gender,Cr concentration,and then calculate the CrCl()
