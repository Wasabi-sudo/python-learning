coordinates = [0.1235, -75.54664]
latitude, longitude = coordinates
print(f"Latitude: {latitude} and Longitude: {longitude}")


event_data = [
    [101, '2023-01-01 12:00', "LOGIN", "user654", "192.124.144.1"],
    [102, '2023-01-01 12:01', "LOGOUT", "user654"],
    [103, '2023-01-01 12:02', "FILE_UPLOAD", "user654", "report.pdf", 1024]
]

for event_id, timestamp, event_type, *details in event_data:
    print(f"Event ID: {event_id}, Timestamp: {timestamp}, Event Type: {event_type}, Details: {details}")