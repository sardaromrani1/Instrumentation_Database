from instrumentation_database import Instrumentation, session

# Fetch all records
devices = session.query(Instrumentation).all()

# Display results 
for device in devices:
    print(f"ID: {device.id}, Name: {device.device_name}, Manufacturer: {device.manufacturer}, Model: {device.model}, Part Number: {device.part_number}")