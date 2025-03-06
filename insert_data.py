from instrumentation_database import Instrumentation, session

# Sample Data
devices = [
    Instrumentation(device_name= "Multimeter", manufacturer= "Fluke", model= "117", part_number= "FLK-117"),
    Instrumentation(device_name= "Oscilloscope", manufacturer= "Tektronix", model= "TBS1104", part_number= "TEK-1104")
]

# Add data to database
session.add_all(devices)
session.commit()

print("Data inserted successfully!")