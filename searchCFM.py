from searchCFMFunctions import getListaMedicos
from searchCFMFunctions import getDoctorInfos
import math
import json
import pandas as pd

doctors = []
errors = []  # List to store error messages
# Parse the JSON string
data = json.loads(getListaMedicos().text)
# Extract the first "COUNT" value
count = int(data["dados"][0]["COUNT"])

count = math.ceil(count / 10)

# Loop through the pages
for page in range(1, count + 1):  # substitute 3 by count + 1
    data = json.loads(getListaMedicos(page).text)
    for medico in range(0, len(data["dados"])):
        crm = data["dados"][medico]["NU_CRM"]
        hash = data["dados"][medico]["SECURITYHASH"]
        try:
            doctor = json.loads(getDoctorInfos(crm, hash).text)
            nome = doctor["dados"][0]["NOME"]
            telefone = doctor["dados"][0]["TELEFONE"]
            print(nome)
            print(telefone)
            doctors.append({"Nome": nome, "Telefone": telefone})
        except json.decoder.JSONDecodeError as e:
            error_msg = f"Error decoding JSON for CRM {crm}: {e}"
            print(error_msg)
            errors.append(error_msg)


# Create a DataFrame from the list
df = pd.DataFrame(doctors)

# Drop rows where 'Telefone' is None
df = df.dropna(subset=["Telefone"])

# Save the DataFrame to an Excel file
df.to_excel("medicosInfo.xlsx", index=False)

# Save errors to a text file
with open("errors.txt", "w") as f:
    f.write("\n".join(errors))
