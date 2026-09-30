ambulances = {
    "AMB001": "Available",
    "AMB003": "Available"
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

book_ambulance("Patient 2", "Coimbatore")
track_ambulance("AMB001")
notify_hospital("City Hospital")
# Updated during Git and GitHub workflow demonstration
def calculate_response_analytics():
    """Feature: Admin Analytics Engine for Sprint 1 (Added by Avantika R)"""
    avg_response_time = 6.4
    active_dispatches = 12
    print(f"[ANALYTICS] Avg Response Time: {avg_response_time} mins | Active: {active_dispatches}")
    return {"avg_response_time": avg_response_time, "active_dispatches": active_dispatches}

def delay_alert(ambulance_id, delay_minutes):
    if delay_minutes > 10:
        print(f"Delay alert triggered for {ambulance_id}")
    else:
        print(f"Ambulance {ambulance_id} is on schedule")

delay_alert("AMB001", 15)

# B: Ambulance tracking feature updated
