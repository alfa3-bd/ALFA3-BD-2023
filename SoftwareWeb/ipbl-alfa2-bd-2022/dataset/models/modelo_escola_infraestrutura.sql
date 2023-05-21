-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-04-22 18:52:52.241

-- tables
-- Table: CONTRATO
CREATE TABLE CONTRATO (
    con_id serial  NOT NULL,
    uni_id serial  NOT NULL,
    inf_id serial  NOT NULL,
    con_data_ini date  NOT NULL,
    con_data_fim date  NOT NULL,
    con_tipo int  NOT NULL,
    CONSTRAINT CONTRATO_pk PRIMARY KEY (con_id)
);

-- Table: UNIDADE_ESCOLAR
CREATE TABLE UNIDADE_ESCOLAR (
    uni_id serial  NOT NULL,
    uni_codigo_inep int  NOT NULL,
    uni_nome varchar(255)  NOT NULL,
    uni_uf char(2)  NOT NULL,
    uni_cep char(9)  NOT NULL,
    uni_endereco varchar(255)  NOT NULL,
    uni_municipio varchar(50)  NOT NULL,
    uni_categ_admin int  NOT NULL,
    uni_depen_admin int  NOT NULL,
    CONSTRAINT UNIDADE_ESCOLAR_pk PRIMARY KEY (uni_id)
);

-- Reference: CONTRATO_UNIDADE_ESCOLAR (table: CONTRATO)
ALTER TABLE CONTRATO ADD CONSTRAINT CONTRATO_UNIDADE_ESCOLAR
    FOREIGN KEY (uni_id)
    REFERENCES UNIDADE_ESCOLAR (uni_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

