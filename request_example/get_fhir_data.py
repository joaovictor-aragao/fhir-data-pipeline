import requests

# DOCS: https://www.hl7.org/fhir/http.html
# Patient DOCS: https://www.hl7.org/fhir/patient.html

# variables
BASE_URL = "http://localhost:8080/fhir"

# search 5 results in all patients
# resp = requests.get(f"{BASE_URL}/Patient?_count=5&_pretty=true")
# print(resp.json())

# request observations from Patient 2 (they have obs)
# resp = requests.get(f"{BASE_URL}/Observation?subject=Patient/2&_pretty=true")
# print(resp.json())

# patients on total
resp = requests.get(f"{BASE_URL}/Patient?_summary=count&_total=accurate")
data = resp.json()
print("Total de pacientes:", data.get("total", 0))

