from flask import Flask, jsonify
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, CHAR, ForeignKey, PrimaryKeyConstraint
import logging
import random

app = Flask(__name__)

metadata = MetaData()

current_object = Table('current_object', metadata,
                       Column('zoid', Integer, primary_key=True),
                       Column('tid', Integer))

object_state = Table('object_state', metadata,
                     Column('zoid', Integer, ForeignKey('current_object.zoid')),
                     Column('tid', Integer),
                     Column('state', CHAR),
                     PrimaryKeyConstraint('zoid', 'tid'))

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)


@app.route('/fetch')
def continuously_execute():
    db_url = "postgresql+psycopg2://postgres:example@db/example"
    engine = create_engine(db_url)
    connection = engine.connect()

    output = []
    try:
        log.info('Fetching all zoid values')
        all_zoids = connection.execute(select(current_object)).all()

        i = 0
        if all_zoids:
            for _ in range(10000):  # Simulate the loop for a fixed number of iterations
                random_zoid = random.choice(all_zoids)[0]
                query = select(current_object.c.zoid).where(current_object.c.zoid == random_zoid)

                info = connection.execute(query).fetchone()
                i += 1
                if i % 10000 == 0:
                    output.append(f'Fetched information for zoid: {random_zoid}: {info}')
        else:
            log.info('No zoids found in current_object')
    except Exception as e:
        log.error(f"Failed to connect to the database: {e}")
    finally:
        connection.close()

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)