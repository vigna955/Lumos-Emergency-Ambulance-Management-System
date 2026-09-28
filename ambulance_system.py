ambulances = {
    "AMB001": "Available",
    "AMB002": "Available"
}

hospitals = [
    "City Hospital",
    "Emergency Care Hospital"
]

def book_ambulance(patient, location):
    for ambulance_id, status in ambulances.items():
        if status == "Available":
            ambulances[ambulance_id] = "Assigned"
            print(f"Ambulance {ambulance_id} assigned to {patient} at {location}")
            return ambulance_id

    print("No ambulance currently available")
    return None

def track_ambulance(ambulance_id):
    if ambulance_id in ambulances:
        print(f"Tracking ambulance {ambulance_id}")
    else:
        print("Ambulance not found")

def notify_hospital(hospital):
    if hospital in hospitals:
        print(f"Hospital notified: {hospital}")
    else:
        print("Hospital not found")

book_ambulance("Patient 1", "Coimbatore")
track_ambulance("AMB001")
notify_hospital("City Hospital")