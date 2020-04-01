import psycopg2



conn = psycopg2.connect(database='postgres',password='',
                        host='localhost',port='')
cursor = conn.cursor()
def data():
    cursor.execute('a query')

    res = cursor.fetchone()[0]
    return res
                        

class DBConnector:
    def data(self):
        cursor.execute('a query')

        res = cursor.fetchone()[0]
        return res
                        
