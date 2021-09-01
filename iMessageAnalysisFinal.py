#Import Statements
import csv

#Variables
moodCount = 0 
pleasureCount = 0 
insomniaCount = 0 
fatigueCount = 0 
guiltCount = 0 
concentrationCount = 0 
personalCount = 0 
groupCount = 0 
wordCount = 0
suicideCount = 0 
total = 0 
endUser = False
percent = 0.0
simCount = 0 
missedList = []
caseNum = 0 
row = 0 
col = 0 

#---------------------------------------------------------------------------- Code ----------------------------------------------------------------------------
#Opening Data
with open("analysisMessages.txt", "r", encoding="utf-8") as file:
    
    #Splitting the File into Lines of Text
    for tLine in file:
        
        #Examining Each Line of Text 
        line = tLine.lower()
        
        #Depressed Mood: 
        if ("depression" in line and "began" in line) or ("depression" in line and "begins" in line):
            moodCount+=1
        if " im " in line and " sad" in line:
            moodCount+=1
        if " i " in line and " sad" in line:
            moodCount+=1
        if " myself" in line and " sad" in line:
            moodCount+=1
        if " im " in line and "worthless" in line:
            moodCount+=1
        if " i " in line and "worthless" in line:
            moodCount+=1
        if " myself" in line and "worthless" in line:
            moodCount+=1
        if "i " in line and "lonely" in line:
            moodCount+=1
        if " im " in line and "lonely" in line:
            moodCount+=1
        if " myself" in line and "lonely" in line:
            moodCount+=1
        if " i " in line and "depressed" in line:
            moodCount+=1
        if " me " in line and "depressed" in line:
            moodCount+=1
        if " i " in line and "depression" in line:
            moodCount+=1
        if " myself" in line and "depressed" in line:
            moodCount+=1
        if "depressed" in line and "me " in line:
            moodCount+=1   
        if " i " in line and " alone" in line:
            if "home" or "house" in line:
                moodCount+=0
            else:
                moodCount+=1
        if " im " in line and " alone" in line:
            if "home" or "house" in line:
                moodCount+=0
            else:
                moodCount+=1
        if " myself" in line and " alone" in line:
            if "home" or "house" in line:
                moodCount+=0
            else:
                moodCount+=1
            
        #Loss of Interest and/or Pleasure
        if " i " in line and "disinterested" in line:
            pleasureCount+=1
        if " im " in line and "disinterested" in line:
            pleasureCount+=1
        if " myself" in line and "disinterested" in line:
            pleasureCount+=1
        if " i " in line and "misery" in line:
            pleasureCount+=1
        if " im " in line and "misery" in line:
            pleasureCount+=1
        if " myself" in line and "misery" in line:
            pleasureCount+=1  
        if " i " in line and "sorrow" in line:
            pleasureCount+=1
        if " im " in line and "sorrow" in line:
            pleasureCount+=1
        if " myself" in line and "sorrow" in line:
            pleasureCount+=1 
        if " i " in line and "unhappiness" in line:
            pleasureCount+=1
        if " im " in line and "unhappiness" in line:
            pleasureCount+=1
        if " myself" in line and "unhappiness" in line:
            pleasureCount+=1 
        
        #Insomnia
        if " i " in line and "sleep all the time" in line:
            insomniaCount+=1
        if " i " in line and "stayed in bed" in line:
            insomniaCount+=1
        if " myself" in line and "stayed in bed" in line:
            insomniaCount+=1
        if " me " in line and "stayed in bed" in line:
            insomniaCount+=1
            
        #Fatigue
        if "im always tired" in line:
            fatigueCount+=1
        if "i always want to sleep" in line:
            fatigueCount+=1
        if "im always exhausted" in line:
            fatigueCount+=1
        if "i am always tired" in line:
            fatigueCount+=1
            
        #Feelings of Guilt and Worthlessness
        if " i " in line and "helpless" in line:
            guiltCount+=1
        if " im " in line and "helpless" in line:
            guiltCount+=1      
        if " myself" in line and "helpless" in line:
            guiltCount+=1 
        if " i " in line and "regret" in line:
            guiltCount+=1
        if " im " in line and "regret" in line:
            guiltCount+=1      
        if " myself" in line and "regret" in line:
            guiltCount+=1 
        if " i " in line and "guilt" in line:
            guiltCount+=1
        if " im " in line and "guilt" in line:
            guiltCount+=1      
        if " myself" in line and "guilt" in line:
            guiltCount+=1 
        if " i " in line and "worthless" in line:
            guiltCount+=1
        if " im " in line and "worthless" in line:
            guiltCount+=1      
        if " myself" in line and "worthless" in line:
            guiltCount+=1 
            
        #Concentration Problems
        if " i " in line and "cant concentrate" in line:
            concentrationCount+=1
        if " im " in line and "cant concentrate" in line:
            concentrationCount+=1      
        if " myself" in line and "cant concentrate" in line:
            concentrationCount+=1   
        if " i " in line and "difficulty concentrating" in line:
            concentrationCount+=1
        if " im " in line and "difficulty concentrating" in line:
            concentrationCount+=1      
        if " myself" in line and "difficulty concentrating" in line:
            concentrationCount+=1
                
        #Suicide Count:
        if " kill me" in line:
            suicideCount+=1
        if " kill myself " in line:
            suicideCount+=1
        if " i want " in line and " die " in line:
            suicideCount+=1
        if " me " in line and " die " in line:
            suicideCount+=1
        if " i " in line and " suicide " in line:
            suicideCount+=1
        if " me " in line and " suicide " in line:
            suicideCount+=1
        if "contemplated" in line and "death" in line:
            suicideCount+=1        
        
        #Searching Individual Words:
        for word in line.split():
            wordCount+=1
            if word.lower()=="me" or word.lower()=="i" or word.lower()=="im" or word.lower()=="myself" or word.lower()=="my" or word.lower()=="me." or word.lower()=="me," or word.lower()=="i." or word.lower()=="i," or word.lower()=="myself.":
                personalCount+=1
            elif word.lower()=="we" or word.lower()=="us" or word.lower()=="together":
                groupCount+=1       
                
        
        #Checking whether Personal Pronouns Outweight Group Pronouns
        if personalCount > groupCount:
            total += (personalCount-groupCount)*0.01
        
        #Calculating User's Total Depression Score
        total += (moodCount*3.4) + (pleasureCount*1.9) + (insomniaCount*2) + (fatigueCount*2) + (guiltCount*1.62) + (concentrationCount*1.95) + (suicideCount*7) 
        percent = (total/(wordCount*1.0))*100
    
#Print Statements
print("Your total score is "+percent+"% and "+total+" points.")

        
        