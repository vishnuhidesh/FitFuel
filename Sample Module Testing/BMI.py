def BMI(height, weight):             # The problem with bmi is that it cannot distinguish between muscle and fat.
    bmi = weight/((height/100)**2)   # So it is not recommended to rely only on bmi for overall bodyfat summarization.
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
    
def WTHR(height, waist):
    wthr = round(waist/height, 2)
    return wthr


# def WTHRRange(wthr, gender="M"):
#     if gender == "M":
#         if wthr >= 0.63:
#             return "Highly Obese"
#         elif 0.58 <= wthr < 0.63:
#             return "Extremely Overweight"
#         elif 0.53 <= wthr < 0.58:
#             return "Overweight"
#         elif 0.46 <= wthr < 0.53:
#             return "Healthy"
#         elif 0.43 <= wthr < 0.46:
#             return "Slender & Healthy"
#         elif 0.35 <= wthr < 0.43:
#             return "Extremely Slim"
#         else:
#             return "Abnormally Slim"
#     elif gender == "F":
#         if wthr >= 0.58:
#             return "Highly Obese"
#         elif 0.54 <= wthr < 0.58:
#             return "Extremely Overweight"
#         elif 0.49 <= wthr < 0.54:
#             return "Overweight"
#         elif 0.46 <= wthr < 0.49:
#             return "Healthy"
#         elif 0.42 <= wthr < 0.46:
#             return "Slender & Healthy"
#         elif 0.35 <= wthr < 0.42:
#             return "Extremely Slim"
#         else:
#             return "Abnormally Slim"

def WTHRRangeScore(wthr, gender="M"):
    if gender == "M":
        if wthr >= 0.63:
            return -3
        elif 0.58 <= wthr < 0.63:
            return -2
        elif 0.53 <= wthr < 0.58:
            return -1
        elif 0.46 <= wthr < 0.53:
            return 0
        elif 0.43 <= wthr < 0.46:
            return 1
        elif 0.35 <= wthr < 0.43:
            return 2
        else:
            return 3
    elif gender == "F":
        if wthr >= 0.58:
            return -3
        elif 0.54 <= wthr < 0.58:
            return -2
        elif 0.49 <= wthr < 0.54:
            return -1
        elif 0.46 <= wthr < 0.49:
            return 0
        elif 0.42 <= wthr < 0.46:
            return 1
        elif 0.35 <= wthr < 0.42:
            return 2
        else:
            return 3



    
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
print(WTHR(170.0,80.0))
# print(WTHRRange(0.47,"M"))
# print(healthScore(21,12,80.0,120.0,1))
