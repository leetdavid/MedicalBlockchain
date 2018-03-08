#!/usr/bin/python
#  The program is used for illustrating how to connect MongoDB in Python (using PyMongo)
#
#  Remember to start the MongoDB server before you run this Python script
#
from pymongo import MongoClient

# Creating Collection
def createCollection(db):
	print("Creating Collection...")
	print("    In MongoDB, there is no need to create a collection explicitly (e.g., \'db.createCollection(\"patients\")\').")
	print("    When we insert the first document into a collection, the collection will be created automatically.")

# Inserting Documents
def insertDocument(db):
	try:
		print("Inserting Documents...")
		print("   Inserting Document 1")
		db.patients.insert(
		{
            "id" : "12345678",
            "dateTimeOfExamination" : "2006-03-19 14:00",
            "patientName" : "PRT",
            "institutionName" : "P.R.T.",
            "requestDateTime" : "2018-03-09 12:00",
            "status" : "single",
            "country" : "U.S.A",
            "city" : "New York",
            "recentHistoryOfIllness" : "Patient is a 24‐year old single Caucasion woman, currently a full time student attending college of the Mainland, self referred to E.D. for evaluation of anxiety and low mood.",
            "pastHistoryOfIllness" : 
            "Illnesses: Patient has occasional migraine headaches for which she takes Excedrin Migraine Hospitalizations: none \n Surgeries: none \n Allergies: no known drug allergies \n Current medications: Venlafaxine 75mg po qd \n Current physician: Sees Dr. R. McDonald for psychiatric meds \n PCP is Ob/gyn physician, Dr. Sam Curry in Texas City‐ last visit was in 11/04",
            "familyHistory" : 
            "Paternal grandfather abused etoh \n Paternal grandmother suffered from depression \n She doesn’t believe there is any psychiatric problems in mother’s family, but she is unsure \n Sister also has anxiety, takes paroxetine \n Reports both parents are generally healthy, although mother is overweight and was recently told she was “pre‐diabetic” \n Siblings (1 sister, age 28, 2 brothers, ages 26 and 22, are all healthy)",
            "chiefComplaint" : 
            "I just feel overwhelmed and can’t take it anymore",
            "review" : 
            "Gen: Positive for 15lb weight loss over 9 months. Denies weakness, fatigue, fever, chills, night sweats, heat intolerance. \n Skin: Denies changes, pruritis, rash, or changes in hair. \n Head: Positive for occ migraine headaches. \n ENT: Denies visual changes, eye pain, hearing loss, tinnitus, vertigo, ear pain, ear discharge, epistaxis, nasal discharge, sinusitis, teeth problems, abnormal taste, sore throat, or speech difficulty \n Neck: Denies neck swelling, pain, stiff neck, goiter, or masses, nodes. Cardiopulmonary: Denies cough, dyspnea, wheezing, hemoptysis, chestpain, palpitations, orthopnea, P.N.D., murmurs, edema, claudication, syncope, hypertension GI: Positive for decreased appetite. Neg for n/v, hematemesis, melena, dysphagia, heartburn, flatulence, abdominal pain, jaundice, change in bowel habits, diarrhea, constipation, hematochezia, or rectal pain. \n GU: Age menarche: 12. regular menses. G0,P0. Currently on no contraceptives. Has used condoms in the past. Denies dysmenorrhea, menorrhagia, metrorrhagia, dyspareunia, pelvic pain, sexual dysfunction (although currently has no sexual partner), discharge, STD, breast masses, pain, or tenderness, No dysuria, frequency, nocturia, hematuria, urgency incontinence or polyuria. \n MS: Denies backache, joint pain, stiffness, \n Heme: Denies lympadenopathy, bleeding, bruising, anemia. \n Neuro: Denies seizures, paralysis, muscle weakness, parasthesia, sensation changes. Reports occasional tremors (when anxious), and problems with headache. \n Psych: Note HPI.",
            "physicalExamination" : [
                {"age" : 24},
                {"ethnicity" : "Caucasian"},
                {"nationality" : "German"},
                {"height" : "63 inches"},
                {"weight" : "115lbs"},                
                {"gender" : "F"},
                {"temperature" : "37 C."},
                {"bloodPressure" : "110/62"},
                {"pulse" : "82 BPM"},
                {"others" : "N/A"}           
            ],
            "assessmentAndDiagnosis" :             "Patient is a 24 year old SWF with a long history of social anxiety disorder which appears to have impacted her life in a significant way, leading to a curtailment in her development educationally, socially and occupationally. This led eventually to depression which was successfully treated with sertraline for some time, until she was overcome by the grief of losing a significant relationship in her life, that of her first real boyfriend. The degree of her social anxiety is so profound is possible she may even meet criteria for avoidant personality disorder. Currently her most significant problem is a major depressive episode of 9 months duration, which is not responding to a change of medications. To date she has only had one decent trial of an alternate medication (escitalopram) in terms of length, but since the medication was not increased to its       \n    Axis I: Major Depressive Disorder, Recurrent, Severe Social Anxiety Disorder    \n Rule out generalized anxiety disorder   \n Axis II: R/O Avoidant Personality Disorder  \n Axis III: Migraine Headaches    \n Axis IV: Mild: Having difficulty going to school and considering dropping out Axis V: GAF=55  ", 
            "plan" : "Since the patient is not acutely suicidal at present, and she is not psychotic, she does not currently meet criteria for hospitalization. Therefore will attempt to treat her as an outpatient.",
            "comments" :  
            "1.Will recommend that she increase her Venlafaxine to 150mg qd for 7 days, then go up again to 225mg qd for 7 day, and then to 300mg qd. For the noradrenergic reuptake properties of venlafaxine to take effect, the dosage must be increased to at least 225mg per day, and preferably 300mg per day. The patient should be warned about the potential side effects of going up including nausea, insomnia, and increased blood pressure. \n 2. For sleep problems, will prescribe rozerem 8mg po qd. This medication has the advantage that it is a melatonin receptor agonist, and has no addictive potential. \n 3. Will refer to a psychotherapist for cognitive behavioral therapy to help augment the somatic therapies, to assist with her grieving over her ended relationship, and to assist her with anxiety so that she might be better able to cope and achieve the attainment of future goals, \n 4. Will recommend that she follow up with her psychiatrist within a week to discuss these plans, but that if she feels worse, or becomes suicidal, that she should return to the E.D. to reevaluate her situation or be considered for hospitalization. \n"          
		}
		)

		print("   Inserting Document 2")
		db.patients.insert( 
		{
            "id" : "12345678",
            "dateTimeOfExamination" : "October 1, 2007",
            "patientName" : "Mr. H",
            "institutionName" : "MD Hospital",
            "requestDateTime" : "2018-03-09 12:00",
            "status" : "divorced",
            "country" : "Japan",
            "city" : "Osaka",
            "recentHistoryOfIllness" :"Mr. H is a 65 year old white male with a past medical history significant for an MI and depression who presents today complaining of sharp, epigastric abdominal pain of 3-4 months duration. The abdominal pain has been gradually worsening over the past 3-4 months. The pain has not changed or worsened acutely; Mr. H seeks care for the pain at this time because he is now covered by Medicare. The pain is located in the epigastric region and left upper quadrant of the abdomen. It does not radiate. The pain is relatively constant throughout the day and night but does vary in severity. Mr. H rates the pain as 6/10 at its worst. Mr. H describes the pain as a “sharp, burning” pain. He has not tried taking any medicines to relieve the pain. The pain is not alleviated with rest. Mr. H thinks the pain may be aggravated by throwing the football, but he has also experienced the pain independent of playing football or exerting himself. The pain is not associated with food or eating, although Mr. H does endorse occasional heartburn. Mr. H thinks the pain may at times be worse on laying down, and it does wake him up at night. Mr. H denies any abdominal trauma or injury. He endorses a 5lb weight loss over the past 3-4 months, decreased appetite, and fatigue. He has experienced some drenching night sweats, requiring him to change his shirt but not his sheets. He describes a “lump in his throat” with associated dysphagia. He has experienced some nausea with the abdominal pain but has not vomited. He endorses constipation. He endorses bloody stools with some bowel movements. The blood is dark red in color and is not bright red. There is a sufficient amount of blood to turn the toilet water red. Mr. H does not know how many times per week he experiences this bleeding. He has not seen a bloody bowel movement in the past week."      ,
            "pastHistoryOfIllness" : "Other active problems: \n • Hypertension, diagnosed “years ago,” well-controlled with Metoprolol \n • Depression, poorly controlled; started Prozac 6 months ago but still feels depressed \n Hospitalizations: MI, 2004 \n Surgeries/procedures: Cardiac catheterization, post-MI, 2004 Medications \n Aspirin 81mg po qd since his MI 3 years ago \n Metoprolol 100mg po qd for years",
            "chiefComplaint" : "Abdominal pain",
            "review" : "Mr. H is a retired factory worker. He is divorced and has six children and one grandchild, whom he sees almost daily. Despite this, Mr. H says he still often feels alone, isolated, and depressed. He denies past or present tobacco and illicit drug use. He denies alcohol use. Mr. H does not have health insurance but is now covered by Medicare.",
                        "physicalExamination" : [
                {"age" : 65},
                {"ethnicity" : "Caucasian"},
                {"height" : "5’10”"},
                {"weight" : "160lbs"},                
                {"gender" : "M"},
                {"temperature" : "Not measured"},
                {"bloodPressure" : "126/78"},
                {"disability" : },
                {"others" : "No Known Drug Allergies, no food or insect allergies"}           
            ],
            "assessmentAndDiagnosis" :     "Diagnostic plan: Colonoscopy to evaluate the colon for presence of polyps or tumors Therapeutic plan: \n • If colon cancer is detected on colonoscopy, refer Mr. H to a GI oncologist. \n • Restart Protonix therapy \n • Treat constipation with laxative as needed or daily Metamucil \n Patient Education: The importance of colonoscopy screening for colon cancer was discussed with the patient. \n Problem #2: Depression \n Therapeutic plan: Continue Prozac 20mg po qd for now. Consider switching to a different anti-depressant. Discuss counseling and therapy options. \n Problem #3: Hypertension \n Therapeutic plan: Continue metoprolol 100mg po qd \n Patient education: The importance of dietary salt and fat restriction and exercise were discussed with the patient."        ,
            "comments" : "HR 72 RR 16"
		}  
		)
        
		print("   Inserting Document 3")
		db.patients.insert( 
		{
            "id" : "98764321",
            "dateTimeOfExamination" : "2004-02-06",
            "patientName" : "Rogers, Pamela",
            "institutionName" : "Emergency Department",
            "requestDateTime" : "2018-03-09 12:00",
            "status" : "married",
            "country" : "U.K.",
            "city" : "London",
            "recentHistoryOfIllness" : 
            "This is the first admission for this 56 year old woman, \n who states she was in her usual state of good health until one week prior to admission. At that time she noticed the abrupt onset (over a few seconds to a minute) of chest pain which she describes as dull and aching in character. The pain began in the left para-sternal area and radiated up to her neck. The first episode of pain one week ago occurred when she was working in her garden in the middle of the day. She states she had been working for approximately 45 minutes and began to feel tired before the onset of the pain. Her discomfort was accompanied by shortness of breath, but no sweating, nausea, or vomiting. The pain lasted approximately 5 to 10 minutes and resolved when she went inside and rested in a cool area. \n Since that initial pain one week ago she has had 2 additional episodes of pain, similar in quality and location to the first episode. Three days ago she had a 15 minute episode of pain while walking her dog, which resolved with rest. This evening she had an episode of pain awaken her from sleep, lasting 30 minutes, which prompted her visit to the Emergency Department. At no time has she attempted any specific measures to relieve her pain, other than rest. She describes no other associated symptoms during these episodes of pain, including dizziness, or palpitations. She becomes short of breath during these \n episodes but describes no other exertional dyspnea, \n orthopnea, or paroxysmal nocturnal dyspnea. No change in the pain with movement, no association with food, no GERD sx, no palpable pain. She has never been told she has heart problems, never had any \n chest pains before, does not have claudication. She was diagnosed with HTN 3 years ago, \n She does not smoke nor does she have diabetes. \n She was diagnosed with hypertension 3 years ago and had a TAH with BSO 6 years ago. She is not on hormone replacement therapy. There is a family history of premature CAD. \n She does not know her cholesterol level.",
            "pastHistoryOfIllness" :
 "Surgical – \n 1994: Total abdominal hysterectomy and bilateral \n oophorectomy for uterine fibroids. 1998: Bunionectomy \n Medical History – \n 1998: 1990: \n Allergy: \n Diagnosed with hypertension and began on unknown medication. Stopped after 6 months because of drowsiness. \n Diagnosed with peptic ulcer disease, which resolved after three months on cimetidine. She describes no history of cancer, lung disease \n or previous heart disease. \n Penicillin; experienced rash and hives in 1985."  ,
            "familyHistory" : 
            " Mother: 79, alive and well. \n Father: 54, deceased, heart attack. No brothers or sisters. There is a positive family history of hypertension, but no diabetes, or cancer.",
            "chiefComplaint" : "Ms. Rogers is a 56 y/o WF having chest pains for the last week.",
            "review" : ,
                        "physicalExamination" : [
                {"age" : 56},
                {"ethnicity" : "Caucasian"},
                {"nationality" : "German"},               
                {"gender" : "F"},
                {"temperature" : "37 C"},
                {"bloodPressure" : "168/98"},
                {"pulse" : "90"}
                            ],
            "assessmentAndDiagnosis" :    
            " 1. Chest pain with features of angina pectoris \n This patient’s description of dull, aching, exertion related substernal chest pain is suggestive of ischemic cardiac origin. Her findings of a FH of early ASCVD, hypertension, and early surgical menopause are pertinent risk factors for development of coronary artery disease. Therefore, the combination of this patient’s presentation, and the multiple risk factors make angina pectoris the most likely diagnosis. The pain symptoms appear to be increasing, and the occurrence of pain at rest suggests this \n fits the presentation of unstable angina, and hospitalization is indicated. \n Other processes may explain her chest pain, but are less likely. Gastro-esophageal reflux disease (GERD) may occur at night with recumbency, but usually is not associated with exertion. The pain of GERD is usually burning, and the patient describes no associated gastrointestinal symptoms such as nausea, vomiting or abdominal pain which might suggest peptic ulcer disease. The presence of dyspnea might suggest a pulmonary component to this patient’s disease process, but \n the absence of fever, cough or abnormal pulmonary examination findings make a pulmonary infection less likely, and the association of the dyspnea with the chest pain supports the theory that both symptoms may be from ischemic heart disease. \n 2. Dyspnea \n Her dyspnea may correlate with findings on physical exam of a third heart sound and pulmonary crackles, \n suggesting left ventricular dysfunction. In that case, she may be manifesting symptoms and findings of congestive heart failure from myocardial ischemia. \n 3. Recent onset hypertension and abdominal bruit \n This combination raises the possibility of a secondary cause of hypertension, specifically ASCVD of the renal artery leading to renovascular hypertension. The lack of hypertensive retinopathy and left ventricular hypertrophy on physical examination further support a recent onset of her BP elevation. \n 4. Systolic murmur \n The possibility of important valvular heart disease is raised by the murmur, specifically, aortic stenosis. The murmur radiates to the neck as an aortic valvular murmur \n often does, but a normal carotid upstroke may mean this murmur is not significant. \n 5. Epigastric discomfort, NSAID use with a history of peptic ulcer disease. \n 6. Lumbo-sacral back pain \n 7. Fibrocystic breast disease \n 8. Penicillin allergy" ,
            "plan" : 
            "1. Carefully monitor the patient for any increased chest pain that might be indicative of impending myocardial infarction by admitting the patient to the telemetry floor. \n 2. Start platelet inhibitors, such as aspirin to decrease the risk of myocardial infarction; start nitrates to decrease the risk of occlusion and to treat her symptoms of pain. For prolonged pain un- responsive to nitrates, she may need an analgesic such as morphine. The nitrates will also help to lower her BP. \n 3. Patient should have her cholesterol monitored and when discharged she should be started on an appropriate exercise and weight loss program, including a low-fat diet. If her cholesterol \n is elevated, she may need cholesterol-lowering medication such as HMG Co-reductases. \n 4. Schedule a cardiac catheterization since non-invasive \n tests have a high pretest probability for being positive and regard- less of the result, negative or positive, she will need a cath \n 5. Begin diuretics for her dyspnea which is most likely secondary to volume overload – this will treat her high BP as well. She should have a ventriculogram with the cath that will assess cardiac size and presence of wall motion abnormalities. \n 6. Appropriate lab work would include BUN/Creatinine to assess kidney function, electrolytes and baseline EKG."
		}  
		)

		
	except pymongo.errors.ConnectionFailure as error: 
		print("Document Insertion Failed! Error Message: \"{}\"".format(error))

	
# Updating Documents
def updateDocument(db):
	try:
		print("Updating Documents...")
		print("    Updating the request datetime of the patient with requestDateTime = "2006-03-19 14:00" to "2006-03-19 15:00".")
		db.patients.update_many({"requestDateTime": "2006-03-19 14:00"}, {"$set":{"requestDateTime": "2006-03-19 15:00"}})
	except pymongo.errors.ConnectionFailure as error: 
		print("Document Update Failed! Error Message: \"{}\"".format(error))

# Querying Documents
def queryDocument(db):
	try:
		print("Querying Documents...")
		
		print("    Finding a list of medical records of patients whose dateTime of examination is on 19th March, 2006 at 2PM (using \'find\')....")
		listOfPatients = db.patients.find({"dateTimeOfExamination":"2006-03-19 14:00"})
		recordNo = 0;
        for p in listOfPatients:
            recordNo = recordNo + 1
			print("        Record of recordNo {:s}: (id={:s}, dateTimeOfExamination={:s}, patientName={:s}, institutionName={:s})".format(p["id"], p["dateTimeOfExamination"], p["patientName"], p["institutionName"]))
			
		print("   Finding a list of medical records of patients recorded in P.R.T. hospital (using \'aggregate\')....")	
		listOfpatients = db.patients.aggregate([{"$match": {"institutionName": "P.R.T."}}])
		recordNo = 0;
		for p in listOfPatients:
			recordNo = recordNo + 1
			print("        Record of recordNo {:s}:  (id={:s}, dateTimeOfExamination={:s}, patientName={:s}, institutionName={:s})".format(recordNo, p["id"], p["dateTimeOfExamination"], p["patientName"], p["institutionName"]))
			
		print("    Finding a list of medical records of patients who are single at the time of physical examination recorded (using \'distinct\')....")	
		listOfpatients = db.patients.distinct("id", {"status":"single"})
		recordNo = 0;
		for p in listOfPatients:
			recordNo = recordNo + 1
			print("        Record {:d}: (status={:s})".format(recordNo, p))	
	except pymongo.errors.ConnectionFailure as error: 
		print("Document Querying Failed! Error Message: \"{}\"".format(error))
		
# Removing Documents
def removeDocument(db):
	try:
		print("Removing Documents...")
		print("    Removing patientss whose birth years are 1998...")
		db.patients.remove({"byear":1998})
	except pymongo.errors.ConnectionFailure as error: 
		print("Document Removal Failed! Error Message: \"{}\"".format(error))	

# Dropping Collection
def dropCollection(db):
	try:
		print("Dropping Collection...")
		print("    Dropping collection \'patients\'...")
		db.patients.drop()
	except pymongo.errors.ConnectionFailure as error: 
		print("Collection Dropping Failed! Error Message: \"{}\"".format(error))

def main():

	try:
		# Making a DB connection
		print("Making a MongoDB connection...")
		client = MongoClient("mongodb://localhost:27017")   #Please connect this to Azure Cloud or mongod
		
		# Getting a Database named "university"
		print("Getting a database named \"university\"")
		db = client["MedicalRecords"]

		choice = "0"
		while (choice != "7"):
			print(" ")
			print("Please select one of the following.")
			print("-----------------------------------")
			print("  1. Creating Collection")
			print("  2. Inserting Documents")
			print("  3. Updating Documents")
			print("  4. Querying Documents")
			print("  5. Removing Documents")
			print("  6. Dropping Collection")
			print("  7. Exit")
			print("-----------------------------------")
			print(" ")
			
			choice = input("Your Input: ")
			
			print("\n")
			
			if (choice == "1"):
				createCollection(db)
			elif (choice == "2"):
				insertDocument(db)
			elif (choice == "3"):
				updateDocument(db)
			elif (choice == "4"):
				queryDocument(db)
			elif (choice == "5"):
				removeDocument(db)
			elif (choice == "6"):
				dropCollection(db)
			elif (choice == "7"):
				print("")
			else:
				print("Invalid Input!")
			
		# Closing a DB connection
		print("Closing a DB connection...")	
		client.close()
		
	except pymongo.errors.ConnectionFailure as error: 
		print("DB Connection Failed! Error Message: \"{}\"".format(error))	


main()


