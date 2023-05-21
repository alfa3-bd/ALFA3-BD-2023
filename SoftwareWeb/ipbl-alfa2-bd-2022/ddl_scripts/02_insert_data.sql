-- Fake Cidades
INSERT INTO CIDADE (cid_nome, cid_uf, cid_pais)
SELECT
    'Fake City ' || ROW_NUMBER() OVER (ORDER BY 1),
    'UF' || (ROW_NUMBER() % 10 + 1),
    'Fake Country'
FROM generate_series(1, 10);

-- Fake Enderecos
INSERT INTO Endereco (end_rua, end_numero, end_cep, cid_id)
SELECT
    CASE (ROW_NUMBER() % 4)
        WHEN 1 THEN 'Centro'
        WHEN 2 THEN 'Vila Nova'
        WHEN 3 THEN 'Jardim'
        WHEN 0 THEN 'Bela Vista'
    END,
    (ROW_NUMBER() % 1000 + 1)::varchar,
    LPAD((ROW_NUMBER() % 99999 + 1)::varchar, 5, '0'),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Gestor Admin
INSERT INTO GESTOR_ADMIN (ges_adm_primeiro_nome, ges_adm_segundo_nome, ges_adm_senha)
SELECT
    'Fake First Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    'Fake Last Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    '1234'
FROM generate_series(1, 10);

-- Fake Gestor Escola
INSERT INTO GESTOR_ESCOLA (ges_identificador, ges_primeiro_nome, ges_segundo_nome, ges_senha, ges_ges_id)
SELECT
    LPAD((ROW_NUMBER() % 999999999 + 1)::varchar, 11, '0'),
    'Fake First Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    'Fake Last Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    '1234',
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Unidade Escolar
INSERT INTO UNIDADE_ESCOLAR (uni_codigo_inep, uni_nome, uni_categ_admin, uni_depen_admin, ges_id, end_id)
SELECT
    (ROW_NUMBER() % 99999999 + 1),
    'Fake Company ' || ROW_NUMBER() OVER (ORDER BY 1),
    (ROW_NUMBER() % 5 + 1),
    (ROW_NUMBER() % 5 + 1),
    (ROW_NUMBER() % 10 + 1),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Professor
INSERT INTO PROFESSOR (pro_identificador, pro_primeiro_nome, pro_segundo_nome, pro_senha)
SELECT
    LPAD((ROW_NUMBER() % 999999999 + 1)::varchar, 11, '0'),
    'Fake First Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    'Fake Last Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    '1234'
FROM generate_series(1, 10);

-- Fake Turma
INSERT INTO TURMA (tur_ano, tur_ano_escolar, uni_id, pro_id)
SELECT
    2010 + (ROW_NUMBER() % 14),
    (ROW_NUMBER() % 12 + 1),
    (ROW_NUMBER() % 10 + 1),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Aluno
INSERT INTO ALUNO (alu_primeiro_nome, alu_segundo_nome, alu_tipo, tur_id)
SELECT
    'Fake First Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    'Fake Last Name ' || ROW_NUMBER() OVER (ORDER BY 1),
    'Fake Type ' || ROW_NUMBER() OVER (ORDER BY 1),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Frase
INSERT INTO FRASE (fra_frase, fra_tipo)
SELECT
    'Fake Sentence ' || ROW_NUMBER() OVER (ORDER BY 1),
    (ROW_NUMBER() % 5 + 1)
FROM generate_series(1, 10);

-- Fake Avaliacao
INSERT INTO AVALIACAO (ava_tipo, ava_data, alu_id, pro_id)
SELECT
    'Fake Type ' || ROW_NUMBER() OVER (ORDER BY 1),
    NOW() - (ROW_NUMBER() || ' days')::INTERVAL,
    (ROW_NUMBER() % 10 + 1),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Coleta
INSERT INTO COLETA (col_audio, col_metrica, fra_id, ava_id)
SELECT
    'Fake Audio ' || ROW_NUMBER() OVER (ORDER BY 1),
    RANDOM(),
    (ROW_NUMBER() % 10 + 1),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);

-- Fake Contrato
INSERT INTO CONTRATO (con_data_ini, con_data_fim, con_tipo, uni_id)
SELECT
    CURRENT_DATE - (ROW_NUMBER() || ' months')::INTERVAL,
    CURRENT_DATE + (ROW_NUMBER() || ' months')::INTERVAL,
    (ROW_NUMBER() % 5 + 1),
    (ROW_NUMBER() % 10 + 1)
FROM generate_series(1, 10);
