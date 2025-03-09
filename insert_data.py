from database_setup import Session, Instrument

session = Session()

def insert_data(device_name, manufacturer, model, part_number):
    instrument = Instrument(device_name=device_name, manufacturer=manufacturer, model=model, part_number=part_number)

    session.add(instrument)
    session.commit()
    print("Data inserted successfully!")

if __name__ == "__main__":
    insert_data("Oscilloscope", "Tektronix", "TDS2000", "12345")
    