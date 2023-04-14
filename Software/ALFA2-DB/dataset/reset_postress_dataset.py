from ScriptsPostgreSQL import ScriptsPostgreSQL

sql_scripts = ScriptsPostgreSQL()

sql_scripts.set_tables_in_db('modelo_aluno_professor.sql')
sql_scripts.set_tables_in_db('modelo_escola_infraestrutura.sql')

sql_scripts.delete_all_data()
sql_scripts.close_connection()