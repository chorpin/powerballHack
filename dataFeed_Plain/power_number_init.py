import pandas as pd
from sqlalchemy import create_engine
import os


mysql_path = ':/usr/local/mysql/bin'


os.environ['PATH'] += os.pathsep + mysql_path


db_host = "localhost"
db_name = "Powerball"
db_user = "root"
db_password = "zaq753XSW42"
engine = create_engine("mysql://root:zaq753XSW42@127.0.0.1:3306/Powerball")


excel_file = "dataFeed_Plain/powerball.xlsx"
df = pd.read_excel(excel_file)


table_name = "data_table"
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
