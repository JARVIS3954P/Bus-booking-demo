import sqlite3

#_______________________________________________________________________________________________________
def check_journey_details_with_seats(db_path, origin,destination, date):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
		SELECT
		    B.id AS bus_id,
		    O.name AS operator_name,
		    B.type AS bus_type,
		    J.avalable_seats,
		    B.capacity,
		    B.fare
		FROM
		    BUSES B
		    JOIN OPERATOR O ON B.op_id = O.operator_id
		    JOIN JOURNEY J ON B.id = J.bus_id
		    JOIN ROUTES R ON B.r_id = R.route_id
		    JOIN STATION S1 ON R.origin = S1.id
		    JOIN STATION S2 ON R.destination = S2.id
		WHERE
		    J.journey_date = ? 
		    AND S1.name = ?  
		    AND S2.name = ?; 
    ''', (date,origin, destination))

    bus_details = cursor.fetchall()

    connection.close()

    return bus_details
def add_new_booking_with_seat_update(db_path, date,bus_id, passenger_name, sex, seats, mobile_number, age, total_fare):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Check if enough seats are available in the bus
    cursor.execute('SELECT avalable_seats FROM JOURNEY WHERE bus_id = ? AND avalable_seats >= ?', (bus_id, seats))
    available_seats_result = cursor.fetchone()
    if not available_seats_result:
        connection.close()
        return 1  # Not enough available seats in the journey
    # Insert new booking details
    cursor.execute('''
        INSERT INTO BOOKING (journey, name, sex, seats, mob_no, age, total_fare)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (bus_id, passenger_name, sex, seats, mobile_number, age, total_fare))
    # Update available seats in the journey
    updated_available_seats = available_seats_result[0] - seats
    cursor.execute('UPDATE JOURNEY SET avalable_seats = ? WHERE bus_id = ? AND journey_date = ?', (updated_available_seats, bus_id, date))
    connection.commit()
    connection.close()
    return 2 

def check_booked_seat(number):
    cursor.execute('''SELECT
        B.name AS passenger_name,
        R.origin AS journey_origin,
        R.destination AS journey_destination,
        J.journey_date AS journey_date,
        J.total_fare AS fare,
        B.seats AS seats,
        B.sex AS gender
        FROM
            BOOKING B
        JOIN
            JOURNEY J ON B.journey = J.journey_id
        JOIN
            ROUTES R ON J.bus_id = R.route_id
        WHERE
            B.mob_no = ?;
        ''',(number))

def insert_station_data(db_path, station_id, station_name):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Insert station data
    cursor.execute('''
        INSERT INTO STATION (id, name)
        VALUES (?, ?);
    ''', (station_id, station_name))

    connection.commit()
    connection.close()
    return 1
def add_new_route(db_path,route_id, origin, destination):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Check if origin and destination exist in the STATION table
    cursor.execute('SELECT id FROM STATION WHERE name = ? OR name = ?', (origin, destination))
    station_ids = cursor.fetchall()
    if len(station_ids) == 2:
        origin_station_id, destination_station_id = station_ids[0][0], station_ids[1][0]
        # Insert new route details
        cursor.execute('''
            INSERT INTO ROUTES (route_id, origin, destination)
            VALUES (?, ?, ?)
        ''', (route_id,origin_station_id, destination_station_id))
        connection.commit()
        connection.close()

        return 1  # Success
    else:
        connection.close()
        return 0  # Origin or destination not found in STATION table
def delete_route_by_id(db_path, route_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Check if the route_id exists in the ROUTES table
    cursor.execute('SELECT route_id FROM ROUTES WHERE route_id = ?', (route_id,))
    existing_route = cursor.fetchone()

    if existing_route:
        # Delete the route record
        cursor.execute('DELETE FROM ROUTES WHERE route_id = ?', (route_id,))
        connection.commit()
        connection.close()

        return 1  # Success
    else:
        connection.close()
        return 0  # Route with given route_id not found in ROUTES table    
def add_new_operator(db_path,operator_id, name, address, phone_number, email):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Insert new operator details
    cursor.execute('''
        INSERT INTO OPERATOR (operator_id, name, address, ph_no, email)
        VALUES (?, ?, ?, ?, ?)
    ''', (operator_id,name, address, phone_number, email))
    connection.commit()
    connection.close()
    return 1  # Success
def update_operator(db_path, operator_id, name, address, phone_number, email):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Update existing operator details
    cursor.execute('''
        UPDATE OPERATOR
        SET name=?, address=?, ph_no=?, email=?
        WHERE operator_id=?
    ''', (name, address, phone_number, email, operator_id))
    
    connection.commit()
    connection.close()
    return 1         
def add_new_bus(db_path,bus_id, bus_type, capacity, fare, o_id, route_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Check if the operator exists in the OPERATOR table
    cursor.execute('SELECT operator_id FROM OPERATOR WHERE operator_id = ?', (o_id,))
    operator_result = cursor.fetchone()
    if operator_result:
        operator_id = operator_result[0]
        # Insert new bus details
        cursor.execute('''
            INSERT INTO BUSES (id, type, capacity, fare, op_id, r_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (bus_id,bus_type, capacity, fare, operator_id, route_id))
        connection.commit()
        connection.close()
        return 1  # Success
    else:
        connection.close()
        return 0 
def update_bus(db_path, bus_id, bus_type, capacity, fare, o_id, route_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Check if the operator exists in the OPERATOR table
    cursor.execute('SELECT operator_id FROM OPERATOR WHERE operator_id = ?', (o_id,))
    operator_result = cursor.fetchone()

    if operator_result:
        operator_id = operator_result[0]

        # Check if the bus exists in the BUSES table
        cursor.execute('SELECT id FROM BUSES WHERE id = ?', (bus_id,))
        bus_result = cursor.fetchone()

        if bus_result:
            # Update existing bus details
            cursor.execute('''
                UPDATE BUSES
                SET type=?, capacity=?, fare=?, op_id=?, r_id=?
                WHERE id=?
            ''', (bus_type, capacity, fare, operator_id, route_id, bus_id))

            connection.commit()
            connection.close()
            return 1  # Success
        else:
            connection.close()
            return 0  # Bus not found, return 0 indicating failure
    else:
        connection.close()
        return 0
        
def add_new_journey(db_path, journey_date, bus_id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        # Check if the bus is already on a journey
        cursor.execute('SELECT journey_id FROM JOURNEY WHERE bus_id = ? AND journey_date = ?', (bus_id, journey_date))
        existing_journey_result = cursor.fetchone()

        if existing_journey_result:
            return -1  # Bus is already on a journey

        # Retrieve the bus capacity
        cursor.execute('SELECT capacity FROM BUSES WHERE id = ?', (bus_id,))
        bus_capacity_result = cursor.fetchone()

        if not bus_capacity_result:
            return 0  # Bus not found

        bus_capacity = bus_capacity_result[0]
        # Insert new journey details
        cursor.execute('''
            INSERT INTO JOURNEY (journey_id, journey_date, bus_id, avalable_seats)
            VALUES ((SELECT COALESCE(MAX(journey_id), 0) + 1 FROM JOURNEY), ?, ?, ?)
        ''', (journey_date, bus_id, bus_capacity))

        connection.commit()
        return 1  # Success

    finally:
        connection.close()