def BMI(height,weight):
    bmi = weight/((height/100)**2)
    return bmi

def BMIRange(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal Weight"
    elif bmi >= 25.0 and bmi <= 29.9:
        return "Overweight"
    elif bmi >= 30.0 and bmi <= 34.9:
        return "Obesity Class I"
    elif bmi >= 35.0 and bmi <= 39.9:
        return "Obesity Class II"
    elif bmi >= 40.0:
        return "Obesity Class III"



bmi = BMI(172.0,98.0)


print(round(bmi,1))
print(BMIRange(bmi))
