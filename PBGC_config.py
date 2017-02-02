nsURL = "https://MyNightscoutURL.herokuapp.com/" # or perhaps like "https://MyNightscoutURL.azurewebsites.net/"
glucoseUnit = "mg/dL" # selected unit
carbRatio = 12 # grams of carbohydrate per unit of fast-acting insulin
ISF = 40 # mg/dL or mmol/L per unit fast-acting insulin
CSF = ISF / carbRatio # mg/dL or mmol/L per gram of carbohydrate
carbsPerSkittle = 0.88 # grams of carbohydrate per Skittle
lowGlucoseThreshold = 70 # mg/dL or mmol/L, below which the user requires Skittles
treatmentTarget = 90 # mg/dL or mmol/L, the target glucose to treat to