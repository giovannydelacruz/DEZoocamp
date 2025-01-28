#!/usr/bin/env python
# coding: utf-8

import argparse # Para poder pasar argumentos por consola
import pandas as pd
import os
from sqlalchemy import create_engine
from time import time

def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url=params.url

    csv_name = 'output.csv'

    os.system(f"wget -O {csv_name} {url}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    df_iter = pd.read_csv(f"{url}", iterator=True, chunksize=10, low_memory=False)

    # Si vamos dandole next al iterador, nos va a devolver un dataframe de 
    # 100000 filas y asi sucesivamente.
    df = next(df_iter)

    df.head(n=0).to_sql(f"{table_name}", con=engine, if_exists="replace")
    df.to_sql(f"{table_name}", con=engine, if_exists="append")

    while True:
        t_start = time()

        df = next(df_iter)
        

        df.to_sql(f"{table_name}", con=engine, if_exists="append")

        t_end = time()

        print(f"Chunk loaded in {t_end - t_start} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='Ingest_data',
                    description='Ingest data from csv to postgresql',
                    epilog='Enjoy the program! :)',)

    # user, password, host, port, database, table, url
    
    parser.add_argument('--user', help='User of the database')     
    parser.add_argument('--password', help='Password of the database')      
    parser.add_argument('--host', help='Host of the database')
    parser.add_argument('--port', help='Port of the database')
    parser.add_argument('--db', help='Database name')
    parser.add_argument('--table_name', help='Table name')
    parser.add_argument('--url', help='URL of the csv file')

    args = parser.parse_args()
    
    main(args)

