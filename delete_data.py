# delete_data.py
# Remove a record
from database_setup import Session, Instrument
session = Session()

def delete_data(record_id):
    instrument = session.query(Instrument).filter_by(id= record_id).first()
    if instrument:
        session.delete(instrument)
        session.commit()
        print("Record deleted successfully!")
    else:
        print("Record not found.")

if __name__ == "__main__":
    record_id = int(input("Enter Instrument ID to delete: "))
    delete_data(record_id)