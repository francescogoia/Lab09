from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_flights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from flights f 
                    """

        cursor.execute(query)

        for row in cursor:
            #print(row)
            result.append(Flight(row["ID"],
                                 row["AIRLINE_ID"],
                                 row["FLIGHT_NUMBER"],
                                 row["TAIL_NUMBER"],
                                 row["ORIGIN_AIRPORT_ID"],
                                 row["DESTINATION_AIRPORT_ID"],
                                 row["SCHEDULED_DEPARTURE_DATE"],
                                 row["DEPARTURE_DELAY"],
                                 row["ELAPSED_TIME"],
                                 row["DISTANCE"],
                                 row["ARRIVAL_DATE"],
                                 row["ARRIVAL_DELAY"]
                                 ))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_airport():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from airports a"""

        cursor.execute(query)

        for row in cursor:
            #print(row)
            result.append(Airport(row["ID"],
                                 row["IATA_CODE"],
                                 row["AIRPORT"],
                                 row["CITY"],
                                 row["STATE"],
                                 row["COUNTRY"],
                                 row["LATITUDE"],
                                 row["LONGITUDE"],
                                 row["TIMEZONE_OFFSET"],
                                 ))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_medie_aereoporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select avg(f.DISTANCE) , f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID 
                    from flights f 
                    group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID  """

        cursor.execute(query)

        for row in cursor:
            # print(row)
            result.append((float(row["avg(f.DISTANCE)"]), int(row["ORIGIN_AIRPORT_ID"]), int(row["DESTINATION_AIRPORT_ID"])))
            #result.append(row)
        print(result)
        cursor.close()
        conn.close()
        return result



if __name__=="__main__":
    d = DAO()
    #d.get_all_flights()
    #d.get_all_airport()
    d.get_medie_aereoporti()