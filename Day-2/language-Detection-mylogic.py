def detectLanguage(language):
  while True:
   
   if language == "HELLO":
       
    return "ENGLISH"

   elif language=="HOLA":
    return "SPANISH"

   elif language =="HALLO":
    return "GERMAN"

   elif language == "BONJOUR":
    return "FRENCH"

   elif language== "CIAO":
    return "ITALIAN"

   elif language == "ZDRAVSTVUJTE":
     return "RUSSIAN"
 
   else:
    return "UNKNOWN"

while True:
    language=input("Say HI in your language:").upper()
    if language == "#": 
        break

    result=detectLanguage(language)
    print(result)