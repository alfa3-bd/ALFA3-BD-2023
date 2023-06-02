### Fake (PT BR) DOC: https://faker.readthedocs.io/en/master/locales/pt_BR.html ###
from faker import Faker
from dataset.ScriptsPostgreSQL import ScriptsPostgreSQL
from utils.CryptoHelper import CryptoHelper
import json


def main(*args, **kwargs):
    locate = "pt_BR" if "locate" not in kwargs else kwargs["locate"]
    number_of_range = (
        10 if "number_of_examples" not in kwargs else kwargs["number_of_examples"]
    )
    crypto = CryptoHelper()

    fake = Faker(locale=locate)

    scripts_postgre = ScriptsPostgreSQL()

    ### Fake Cidades ###
    if scripts_postgre.get_table_data_count(table_name="CIDADE") == 0:
        city_data = []

        for i in range(number_of_range):
            city = {
                "cid_nome": fake.city(),
                "cid_uf": fake.state_abbr(),
                "cid_pais": fake.country(),
            }
            city_data.append(city)

        json_data = json.dumps(city_data)
        scripts_postgre.save_data(table_name="CIDADE", data=json_data)

    ### Fake Enderecos ###
    if scripts_postgre.get_table_data_count(table_name="Endereco") == 0:
        endereco_data = []
        for i in range(number_of_range):
            endereco = {
                "end_rua": fake.random_element(
                    ["Centro", "Vila Nova", "Jardim", "Bela Vista"]
                ),
                "end_numero": fake.building_number(),
                "end_cep": fake.zipcode(),
                "cid_id": fake.random_int(min=1, max=10),
            }
            endereco_data.append(endereco)
        json_data = json.dumps(endereco_data)
        scripts_postgre.save_data(table_name="Endereco", data=json_data)
        print("Dados inseridos na tabela Endereco com sucesso!")

    ### Fake Gestor Admin ###
    if scripts_postgre.get_table_data_count(table_name="GESTOR_ADMIN") == 0:
        gestor_admin_data = []
        for i in range(number_of_range):
            gestor_admin = {
                "ges_adm_primeiro_nome": fake.first_name(),
                "ges_adm_segundo_nome": fake.last_name(),
                "ges_adm_senha": crypto.encrypt_message("1234"),
            }
            gestor_admin_data.append(gestor_admin)
        json_data = json.dumps(gestor_admin_data)
        scripts_postgre.save_data(table_name="GESTOR_ADMIN", data=json_data)
        print("Dados inseridos na tabela GESTOR_ADMIN com sucesso!")

    ### Fake Gestor Escola ###
    if scripts_postgre.get_table_data_count(table_name="GESTOR_ESCOLA") == 0:
        gestor_escola_data = []
        for i in range(number_of_range):
            gestor_escola = {
                "ges_identificador": fake.cpf(),
                "ges_primeiro_nome": fake.first_name(),
                "ges_segundo_nome": fake.last_name(),
                "ges_senha": crypto.encrypt_message("1234"),
                "ges_ges_id": fake.random_int(min=1, max=10),
            }
            gestor_escola_data.append(gestor_escola)
        json_data = json.dumps(gestor_escola_data)
        scripts_postgre.save_data(table_name="GESTOR_ESCOLA", data=json_data)
        print("Dados inseridos na tabela GESTOR_ESCOLA com sucesso!")

    ### Fake Unidade Escolar ###
    if scripts_postgre.get_table_data_count(table_name="UNIDADE_ESCOLAR") == 0:
        unidade_escolar_data = []
        for i in range(number_of_range):
            unidade_escolar = {
                "uni_codigo_inep": fake.random_number(digits=8),
                "uni_nome": fake.company(),
                "uni_categ_admin": fake.random_int(min=1, max=5),
                "uni_depen_admin": fake.random_int(min=1, max=5),
                "ges_id": fake.random_int(min=1, max=10),
                "end_id": fake.random_int(min=1, max=10),
            }
            unidade_escolar_data.append(unidade_escolar)
        json_data = json.dumps(unidade_escolar_data)
        scripts_postgre.save_data(table_name="UNIDADE_ESCOLAR", data=json_data)
        print("Dados inseridos na tabela UNIDADE_ESCOLAR com sucesso!")

    ### Fake Professor ###
    if scripts_postgre.get_table_data_count(table_name="PROFESSOR") == 0:
        professor_data = []
        for i in range(number_of_range):
            professor = {
                "pro_identificador": fake.cpf(),
                "pro_primeiro_nome": fake.first_name(),
                "pro_segundo_nome": fake.last_name(),
                "pro_senha": crypto.encrypt_message("1234"),
            }
            professor_data.append(professor)
        json_data = json.dumps(professor_data)
        scripts_postgre.save_data(table_name="PROFESSOR", data=json_data)
        print("Dados inseridos na tabela PROFESSOR com sucesso!")

    ### Fake Turma ###
    if scripts_postgre.get_table_data_count(table_name="TURMA") == 0:
        turma_data = []
        for i in range(number_of_range):
            turma = {
                "tur_ano": fake.random_int(min=2010, max=2023),
                "tur_ano_escolar": fake.random_int(min=1, max=12),
                "uni_id": fake.random_int(min=1, max=10),
                "pro_id": fake.random_int(min=1, max=10),
            }
            turma_data.append(turma)
        json_data = json.dumps(turma_data)
        scripts_postgre.save_data(table_name="TURMA", data=json_data)
        print("Dados inseridos na tabela TURMA com sucesso!")

    ### Fake Aluno ###
    if scripts_postgre.get_table_data_count(table_name="ALUNO") == 0:
        aluno_data = []
        for i in range(number_of_range):
            aluno = {
                "alu_primeiro_nome": fake.first_name(),
                "alu_segundo_nome": fake.last_name(),
                "alu_tipo": fake.word(),
                "tur_id": fake.random_int(min=1, max=10),
            }
            aluno_data.append(aluno)
        json_data = json.dumps(aluno_data)
        scripts_postgre.save_data(table_name="ALUNO", data=json_data)
        print("Dados inseridos na tabela ALUNO com sucesso!")

    ### Fake Frase ###
    if scripts_postgre.get_table_data_count(table_name="FRASE") == 0:
        frase_data = []
        for i in range(number_of_range):
            frase = {
                "fra_frase": fake.sentence(),
                "fra_tipo": fake.random_int(min=1, max=5),
            }
            frase_data.append(frase)
        json_data = json.dumps(frase_data)
        scripts_postgre.save_data(table_name="FRASE", data=json_data)
        print("Dados inseridos na tabela FRASE com sucesso!")

    ### Fake Avaliacao ###
    if scripts_postgre.get_table_data_count(table_name="AVALIACAO") == 0:
        avaliacao_data = []
        for i in range(number_of_range):
            avaliacao = {
                "ava_tipo": fake.word(),
                "ava_data": fake.date_time(),
                "alu_id": fake.random_int(min=1, max=10),
                "pro_id": fake.random_int(min=1, max=10),
            }
            avaliacao_data.append(avaliacao)
        json_data = json.dumps(avaliacao_data)
        scripts_postgre.save_data(table_name="AVALIACAO", data=json_data)
        print("Dados inseridos na tabela AVALIACAO com sucesso!")

    ### Fake Coleta ###
    if scripts_postgre.get_table_data_count(table_name="COLETA") == 0:
        coleta_data = []
        for i in range(number_of_range):
            coleta = {
                "col_audio": fake.file_name(),
                "col_metrica": fake.random_float(),
                "fra_id": fake.random_int(min=1, max=10),
                "ava_id": fake.random_int(min=1, max=10),
            }
            coleta_data.append(coleta)
        json_data = json.dumps(coleta_data)
        scripts_postgre.save_data(table_name="COLETA", data=json_data)
        print("Dados inseridos na tabela COLETA com sucesso!")

    ### Fake Contrato ###
    if scripts_postgre.get_table_data_count(table_name="CONTRATO") == 0:
        contrato_data = []
        for i in range(number_of_range):
            contrato = {
                "con_data_ini": fake.date_between(start_date="-1y", end_date="today"),
                "con_data_fim": fake.date_between(start_date="today", end_date="+1y"),
                "con_tipo": fake.random_int(min=1, max=5),
                "uni_id": fake.random_int(min=1, max=10),
            }
            contrato_data.append(contrato)
        json_data = json.dumps(contrato_data)
        scripts_postgre.save_data(table_name="CONTRATO", data=json_data)
        print("Dados inseridos na tabela CONTRATO com sucesso!")


if __name__ == "__main__":
    config = {
        "number_of_examples": 10,
        "locate": "pt_BR",
        "delete_elements_before": True,
    }

    main(**config)
