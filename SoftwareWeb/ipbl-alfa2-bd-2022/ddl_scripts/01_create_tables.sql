-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-05-18 03:58:01.645

-- tables
-- Table: ALUNO
CREATE TABLE ALUNO (
    alu_id serial  NOT NULL,
    alu_primeiro_nome varchar(255)  NOT NULL,
    alu_segundo_nome varchar(255)  NOT NULL,
    alu_data_nascimento date NOT NULL,
    tip_alu serial NOT NULL,
    tur_id serial  NOT NULL,
    CONSTRAINT ALUNO_pk PRIMARY KEY (alu_id)
);

-- Table: TIPO_ALUNO
CREATE TABLE TIPO_ALUNO (
    "tip_alu_id" INTEGER NOT NULL DEFAULT nextval('tipo_aluno_tip_alu_id_seq'),
    "tip_alu_desc" VARCHAR NOT NULL,
    PRIMARY KEY ("tip_alu_id")
);

-- Table: AVALIACAO
CREATE TABLE AVALIACAO (
    ava_id serial  NOT NULL,
    ava_tipo varchar(256)  NOT NULL,
    ava_data timestamp  NOT NULL,
    ava_nota numeric(10, 2),
    alu_id serial  NOT NULL,
    pro_id serial  NOT NULL,
    CONSTRAINT AVALIACAO_pk PRIMARY KEY (ava_id)
);

-- Table: COLETA
CREATE TABLE COLETA (
    col_id serial  NOT NULL,
    col_audio varchar(256)  NOT NULL,
    col_metrica real  NOT NULL,
    fra_id serial  NOT NULL,
    ava_id serial  NOT NULL,
    CONSTRAINT COLETA_pk PRIMARY KEY (col_id)
);

-- Table: CONTRATO
CREATE TABLE CONTRATO (
    con_id serial  NOT NULL,
    con_data_ini date  NOT NULL,
    con_data_fim date  NOT NULL,
    con_tipo int  NOT NULL,
    uni_id serial  NOT NULL,
    CONSTRAINT CONTRATO_pk PRIMARY KEY (con_id)
);

-- Table: FRASE
CREATE TABLE FRASE (
    fra_id serial  NOT NULL,
    fra_frase varchar(256)  NOT NULL,
    fra_tipo int  NOT NULL,
    CONSTRAINT FRASE_pk PRIMARY KEY (fra_id)
);

-- Table: GESTOR_ADMIN
CREATE TABLE GESTOR_ADMIN (
    ges_adm_id serial  NOT NULL,
    ges_adm_primeiro_nome varchar(256)  NOT NULL,
    ges_adm_segundo_nome varchar(256)  NOT NULL,
    ges_adm_senha varchar(256)  NOT NULL,
    CONSTRAINT GESTOR_ADMIN_pk PRIMARY KEY (ges_adm_id)
);

-- Table: GESTOR_ESCOLA
CREATE TABLE GESTOR_ESCOLA (
    ges_id serial  NOT NULL,
    ges_identificador varchar(256)  NOT NULL,
    ges_primeiro_nome varchar(256)  NOT NULL,
    ges_segundo_nome varchar(256)  NOT NULL,
    ges_senha varchar(256)  NOT NULL,
    ges_ges_id int  NOT NULL,
    CONSTRAINT GESTOR_ESCOLA_pk PRIMARY KEY (ges_id)
);

-- Table: PROFESSOR
CREATE TABLE PROFESSOR (
    pro_id serial  NOT NULL,
    pro_identificador varchar(256)  NOT NULL,
    pro_primeiro_nome varchar(255)  NOT NULL,
    pro_segundo_nome varchar(255)  NOT NULL,
    pro_senha varchar(256)  NOT NULL,
    CONSTRAINT PROFESSOR_pk PRIMARY KEY (pro_id)
);

-- Table: TURMA
CREATE TABLE TURMA (
    tur_id serial  NOT NULL,
    tur_ano int  NOT NULL,
    tur_ano_escolar int  NOT NULL,
    uni_id serial  NOT NULL,
    pro_id serial  NOT NULL,
    CONSTRAINT TURMA_pk PRIMARY KEY (tur_id)
);

-- Table: UNIDADE_ESCOLAR
CREATE TABLE UNIDADE_ESCOLAR (
    uni_id serial  NOT NULL,
    uni_codigo_inep int  NOT NULL,
    uni_nome varchar(255)  NOT NULL,
    uni_categ_admin int  NOT NULL,
    uni_depen_admin int  NOT NULL,
    ges_id int  NOT NULL,
    end_id int  NOT NULL,
    CONSTRAINT UNIDADE_ESCOLAR_pk PRIMARY KEY (uni_id)
);

-- Table: ENDERECO
CREATE TABLE ENDERECO (
    end_id serial  NOT NULL,
    end_rua varchar(255)  NOT NULL,
    end_numero int  NOT NULL,
    end_cep varchar(9)  NOT NULL,
    cid_id int  NOT NULL,
    CONSTRAINT ENDERECO_pk PRIMARY KEY (end_id)
);

CREATE TABLE CIDADE (
    cid_id serial  NOT NULL,
    cid_nome varchar(255)  NOT NULL,
    cid_uf varchar(2)  NOT NULL,
    cid_pais varchar(50)  NOT NULL,
    CONSTRAINT CIDADE_pk PRIMARY KEY (cid_id)
);

-- foreign keys
-- Reference: ALUNO_Turma (table: ALUNO)
ALTER TABLE ALUNO ADD CONSTRAINT ALUNO_Turma
    FOREIGN KEY (tur_id)
    REFERENCES tipo_aluno (tur_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

ALTER TABLE ALUNO ADD CONSTRAINT ALUNO_Tipo
    FOREIGN KEY (tip_alu)
    REFERENCES TIPO_ALUNO (tip_alu_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: AVALIACAO_ALUNO (table: AVALIACAO)
ALTER TABLE AVALIACAO ADD CONSTRAINT AVALIACAO_ALUNO
    FOREIGN KEY (alu_id)
    REFERENCES ALUNO (alu_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: AVALIACAO_PROFESSOR (table: AVALIACAO)
ALTER TABLE AVALIACAO ADD CONSTRAINT AVALIACAO_PROFESSOR
    FOREIGN KEY (pro_id)
    REFERENCES PROFESSOR (pro_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: COLETA_AVALIACAO (table: COLETA)
ALTER TABLE COLETA ADD CONSTRAINT COLETA_AVALIACAO
    FOREIGN KEY (ava_id)
    REFERENCES AVALIACAO (ava_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: COLETA_FRASES (table: COLETA)
ALTER TABLE COLETA ADD CONSTRAINT COLETA_FRASES
    FOREIGN KEY (fra_id)
    REFERENCES FRASE (fra_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: CONTRATO_UNIDADE_ESCOLAR (table: CONTRATO)
ALTER TABLE CONTRATO ADD CONSTRAINT CONTRATO_UNIDADE_ESCOLAR
    FOREIGN KEY (uni_id)
    REFERENCES UNIDADE_ESCOLAR (uni_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: GESTOR_ESCOLA_GESTOR_GESTOR (table: GESTOR_ESCOLA)
ALTER TABLE GESTOR_ESCOLA ADD CONSTRAINT GESTOR_ESCOLA_GESTOR_GESTOR
    FOREIGN KEY (ges_ges_id)
    REFERENCES GESTOR_ADMIN (ges_adm_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: TURMA_PROFESSOR (table: TURMA)
ALTER TABLE TURMA ADD CONSTRAINT TURMA_PROFESSOR
    FOREIGN KEY (pro_id)
    REFERENCES PROFESSOR (pro_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Turma_UNIDADE_ESCOLAR (table: TURMA)
ALTER TABLE TURMA ADD CONSTRAINT Turma_UNIDADE_ESCOLAR
    FOREIGN KEY (uni_id)
    REFERENCES UNIDADE_ESCOLAR (uni_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: UNIDADE_ESCOLAR_GESTOR_ESCOLA (table: UNIDADE_ESCOLAR)
ALTER TABLE UNIDADE_ESCOLAR ADD CONSTRAINT UNIDADE_ESCOLAR_GESTOR_ESCOLA
    FOREIGN KEY (ges_id)
    REFERENCES GESTOR_ESCOLA (ges_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: UNIDADE_ESCOLAR_ENDERECO (table: UNIDADE_ESCOLAR)
ALTER TABLE UNIDADE_ESCOLAR ADD CONSTRAINT UNIDADE_ESCOLAR_ENDERECO 
    FOREIGN KEY (end_id)
    REFERENCES ENDERECO (end_id)
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

ALTER TABLE ENDERECO ADD CONSTRAINT ENDERECO_CIDADE
    FOREIGN KEY (cid_id)
    REFERENCES CIDADE (cid_id)
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.
