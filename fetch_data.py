from database_setup import Session, Instrument

session = Session()

def fetch_data():
    instruments = session.query(Instrument).all()
    for instrument in instruments:
        print(f"{instrument.id}: {instrument.device_name}: {instrument.manufacturer}: {instrument.model}: {instrument.part_number}")

if __name__ == "__main__":
    fetch_data()