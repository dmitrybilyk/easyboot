# Starting empty array of eventIds
event_ids = []

# Initial event ID
initial_id = 2620

# Number of objects to add
num_objects_to_add = 1000

# Generate and append new objects with incremented event IDs
for i in range(num_objects_to_add):
    new_id = initial_id + i
    event_ids.append({"eventId": f"callrec:voicetagid:{new_id}"})

# Print the updated array of eventIds
for event in event_ids:
    print(event)
