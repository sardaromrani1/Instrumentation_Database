# update_data_session.py
# Allow multiple updates in one session
from database_setup import Session, Instrument
def update_multiple_records(updates):
    """
    Updates multiple records in the Instrument table.
    param updates: List of tuples (record_id, field, new_value)
    """
    session = Session()

    try:
        for record_id, field, new_value in updates:
            instrument= session.query(Instrument).filter_by(id= record_id).first()
            if instrument:
                setattr(instrument, field, new_value)
                print(f"Updated Record {record_id}: {field}-> {new_value}")
            else:
                print(f"Record {record_id} not found.")
        
        session.commit()    # Commit all changes at once
        print("All updates committed successfully!")

    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print(f"Error updating records: {e}")
    
    finally:
        session.close()

if __name__ == "__main__":
    updates = [
        (1, "device_name", "Updated Device 1"),
        (2, "manufacturer", "Updated Manufacturer 2"),
        (3, "model", "Updated Model 3")
    ]

    update_multiple_records(updates)