from deepface import DeepFace


print("----------------------------------------------------\n")

programname= "Depression Detection"
print(programname)

print("----------------------------------------------------\n")

print("Welcome to Depression Detection Software")

#database is folder data model face emotion
an_emot = DeepFace.stream("database", model_name='DeepFace') #Analyze Emotion from face with using library DeepFace
print(an_emot)
