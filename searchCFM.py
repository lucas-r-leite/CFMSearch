from searchCFMFunctions import getListaMedicos
import math
import json

#Take number of doctors from on the response "COUNT":"5984"
# Parse the JSON string
data = json.loads(getListaMedicos().text)

# Extract the first "COUNT" value
count = int(data["dados"][0]["COUNT"])

count = math.ceil(count / 10)

# Loop through the pages
for page in range(1, 3):
    data = json.loads(getListaMedicos(page).text)
    for medico in range(0, 10):
        crm = data["dados"][medico]["NU_CRM"]
        hash = data["dados"][medico]["SECURITYHASH"]
        print(crm)
        print(hash)
    