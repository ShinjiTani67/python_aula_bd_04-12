# create table petshop (
#     id_pk number,
#     pet varchar(30),
#     nome_pet varchar (30),
#     idade number
# ); --> tabela

import json
import oracledb
import pandas as pd

margem = '\t'

with open("credenciais.json") as f:
    credenciais = json.load(f)

USER = credenciais["user"]
PASS = credenciais["pass"]

dsnString = oracledb.makedsn("oracle.fiap.com.br",1521,"ORCL")
conn = oracledb.connect(user = USER, password = PASS, dsn = dsnString)

cursor = conn.cursor()

pet = "cachorro"
nome_pet = "ricardo"
idade = "10"

cadastro = f"""Insert into petshop (pet,nome_pet,idade)Values('{pet}','{nome_pet}','{idade}')"""
cursor.execute(cadastro)
conn.commit()

query_leitura = "SELECT * FROM petshop"
result = cursor.execute(query_leitura)

data = result.fetchall()
df = pd.DataFrame(data=data, columns=["ID_PK","PET","NOME_PET","IDADE"])
print(df.set_index("ID_PK").sort_index())