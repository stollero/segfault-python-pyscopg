import psycopg2
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)


def continuously_execute():
    conn_params = {
        "dbname": "example",
        "user": "postgres",
        "password": "example",
        "host": "db"
    }

    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        log.info('Fetching all zoid values')
        cursor.execute("SELECT zoid FROM current_object")
        all_zoids = cursor.fetchall() 

        i = 0
        while True:
            if all_zoids:
                random_zoid = random.choice(all_zoids)[0] 
                cursor.execute("""
                    SELECT co.zoid, co.tid, os.state 
                    FROM current_object co
                    JOIN object_state os ON co.zoid = os.zoid
                    WHERE co.zoid = %s
                """, (random_zoid,))
                info = cursor.fetchone()
                i += 1
                if i % 10000 == 0:
                    i = 0
                    log.info(f'Fetched information for zoid: {random_zoid}: {info}')
            else:
                log.info('No zoids found in current_object')
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    continuously_execute()