# Instrumentation Database
 
 The **Instrumentation Database** is a Python-based project using **SQLAlchemy** to manage instrumentation records. It allows users to store, update, retrieve, and delete instrument data, including **device names, manufacturers, models, and part numbers**.

 ## Features
 **Create a database** for storing instrumentation details
 **Insert new records** into the database
 **Fetch and display** instrument data
 **Update records** ( single update & bulk update)
 **Delete records** from the database
 Uses **SQLite** for data storage

 ## Installation

 ### 1 Clone the Repository
 '''sh
 git clone https://github.com/sardaromrani1/Instrumentation_Database.git
 cd Instrumentation_Database

 2 Install Dependencies
 sh
 pip install sqlalchemy

 3 Set Up the Database
 Run the following script to create the database:
 sh
 python database_setup.py

 Usage
 Insert Data
 To add a new instrument record:
 sh
 python insert_data.py

 Fetch Data
 To retrieve and display all stored instrument records:
 sh
 python fetch_data.py

 Update Data
 To update a single record:
 sh
 python update_data.py

 Bulk Update Data
 To update multiple records in one session
 sh
 python update_data_session.py

 Delete Data
 To delete a specific record from the database:
 sh
 python delete_data.py


 License
 This project is licensed under the MIT License.

 Author
 * Sardar Omrani
 * sardaromrani1
