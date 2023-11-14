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
    
def healthScore(bmi,bfp,dbp,sbp,dbs):
    nbmi = (bmi - 18.5)/11.5
    nbfp = (bfp - 1.0)/25.0
    ndbp = (dbp - 60.0)/20.0
    nsbp = (sbp - 90.0)/30.0
    ndbs = dbs
    score = (nbmi * 0.3) + (nbfp * 0.25) + (nsbp * 0.175) + (ndbp * 0.175) + (ndbs * 0.2)
    return score



bmi = BMI(172.0,81.0)


print(round(bmi,1))
print(BMIRange(bmi))
print(healthScore(21,12,80.0,120.0,1))
