from database_setup import Session, Instrument

session = Session()

def update_data(record_id, field, new_value):
    instrument = session.query(Instrument).filter_by(id= record_id).first()
    if instrument:
        setattr(instrument, field, new_value)
        session.commit()
        print("Record updated successfully!")
    else: 
        print("Record not found.")


if __name__ ==  "__main__":
    record_id = int(input("Enter Instrument ID: "))
    field = input("Enter field name to update (device_name, manufacturer, model, part_number): ")
    new_value = input("Enter new value: ")


update_data(record_id, field, new_value)