from searchCFMFunctions import getListaMedicos
from searchCFMFunctions import getDoctorInfos
import math
import json

# Take number of doctors from on the response "COUNT":"5984"
# Parse the JSON string
data = json.loads(getListaMedicos().text)

# Extract the first "COUNT" value
count = int(data["dados"][0]["COUNT"])

count = math.ceil(count / 10)

# Loop through the pages
for page in range(1, 3):  # substitute 3 by count + 1
    data = json.loads(getListaMedicos(page).text)
    for medico in range(0, 10):
        crm = data["dados"][medico]["NU_CRM"]
        hash = data["dados"][medico]["SECURITYHASH"]
        doctor = json.loads(getDoctorInfos(crm, hash).text)
        nome = doctor["dados"][0]["NOME"]
        telefone = doctor["dados"][0]["TELEFONE"]
