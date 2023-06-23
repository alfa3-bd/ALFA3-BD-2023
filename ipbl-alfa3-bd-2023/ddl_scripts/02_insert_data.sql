INSERT INTO CATEGORIA_ESCOLAR (cat_esc_id, cat_esc_desc) VALUES
	(1, 'Pública'),
	(2, 'Privada');

INSERT INTO TIPO_AVALIACAO (tip_aval_id, tip_aval_desc) VALUES
	(1, 'Avaliação Diagnóstica'),
	(2, 'Avaliação Formativa de Processo'),
	(3, 'Avaliação Formativa de Saída');

INSERT INTO TIPO_CONTRATO (tip_con_id, tip_con_desc) VALUES
	(1, 'Anual'),
	(2, 'Mensal'),
	(3, 'Exclusivo');

INSERT INTO TIPO_ESCOLA (tip_esc_id, tip_esc_desc) VALUES
	(1, 'Federal'),
	(2, 'Estadual'),
	(3, 'Municipal');

INSERT INTO TIPO_FRASE (tip_frase_id, tip_frase_desc) VALUES
	(1, 'Palavras Aleatórias'),
	(2, 'Pseudo Palavras'),
	(3, 'Palavras Simples');

INSERT INTO FRASE (fra_id, fra_frase, tip_frase_id) VALUES
	(1, 'A certeza de inovar de maneira eficaz', 1),
	(2, 'O poder de realizar seus sonhos direto da fonte', 2),
	(3, 'A segurança de conseguir antes de tudo', 2),
	(4, 'A certeza de avançar com força total', 3),
	(5, 'O prazer de inovar em estado puro', 1),
	(6, 'A liberdade de avançar em estado puro', 1),
	(7, 'O prazer de concretizar seus projetos sem preocupação', 1),
	(8, 'A arte de evoluir simplesmente', 3),
	(9, 'O poder de ganhar com toda a tranquilidade', 2),
	(10, 'O prazer de concretizar seus projetos de maneira eficaz', 2);

INSERT INTO CIDADE (cid_id, cid_nome, cid_uf, cid_pais) VALUES
	(1, 'São Paulo', 'SP', 'Brasil'),
	(2, 'Rio de Janeiro', 'RJ', 'Brasil'),
	(3, 'Belo Horizonte', 'MG', 'Brasil'),
	(4, 'Salvador', 'BA', 'Brasil'),
	(5, 'Santa Catarina', 'SC', 'Brasil');

INSERT INTO ENDERECO (end_id, end_rua, end_numero, end_cep, cid_id) VALUES
	(1, 'Rua das Flores', 123, '01000-000', 1),
	(2, 'Avenida dos Bandeirantes', 456, '04500-000', 1),
	(3, 'Rua Copacabana', 234, '22000-000', 2),
	(4, 'Rua Maracanã', 890, '20500-000', 2),
	(5, 'Avenida Afonso Pena', 123, '30130-000', 3),
	(6, 'Rua Pelourinho', 234, '40000-000', 4),
	(7, 'Avenida Beira-Mar', 456, '88050-000', 5);

INSERT INTO PROFESSOR (pro_id, pro_identificador, pro_primeiro_nome, pro_segundo_nome, pro_senha) VALUES
	(1, '999.999.999-99', 'Royall', 'Adams', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(2, '321.987.654-99', 'Shawna', 'Parslow', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(3, '876.543.210-99', 'Blanca', 'Shotton', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(4, '321.987.852-99', 'Guillermo', 'Belf', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(5, '321.987.896-99', 'Sayre', 'Wisker', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(6, '789.012.345-99', 'Melodie', 'Keggins', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(7, '234.567.890-99', 'Nicky', 'Ivey', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(8, '012.345.678-99', 'Moria', 'Tilliards', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(9, '987.654.321-99', 'Jake', 'Austing', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(10, '876.548.321-90', 'Joelynn', 'Rodie', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA==');

INSERT INTO GESTOR_ADMIN (ges_adm_id, ges_adm_primeiro_nome, ges_adm_segundo_nome, ges_adm_senha) VALUES
	(1, 'Lucas', 'Silva', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(2, 'Paula', 'Moraes', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(3, 'Cristiano', 'de Paula', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA=='),
	(4, 'Sofia', 'Magalhães', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA==');

INSERT INTO GESTOR_ESCOLA (ges_id, ges_identificador, ges_primeiro_nome, ges_segundo_nome, ges_senha, ges_ges_id) VALUES
	(1, '119.876.543-21', 'João', 'Silva ', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA==', 1),
	(2, '119.876.543-22', 'Pedro', 'Almeida', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA==', 3),
	(3, '119.012.345-67', 'Maria', 'Santos ', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA==', 2),
	(4, '119.012.345-68', 'Ana', 'Oliveira', 'gAAAAABkaPztyZ5W2nWs6hW8U4bozfk-Ah4CsoX5AlzmI5-yjoa6eNmkgXNNd1tJRpd9So5CEm1Oquozvz9eGuQQBvIgBKNJlA==', 1);

INSERT INTO UNIDADE_ESCOLAR (uni_id, uni_codigo_inep, uni_nome, cat_esc_id, tip_esc_id, ges_id, end_id) VALUES
	(1, 68779474, 'Escola Nascimento', 1, 3, 1, 1),
	(3, 89332709, 'Escola Estadual João Silva', 1, 2, 3, 6),
	(4, 94237178, 'Escola Municipal Maria Santos', 1, 3, 1, 5),
	(2, 73225631, 'Instituto Federal de Educação, Ciência e Tecnologia Pedro Almeida', 1, 1, 2, 7),
	(5, 55656452, 'Colégio Anglo', 2, 1, 4, 2),
	(6, 42569985, 'Escola Dom Bosco', 2, 3, 4, 3);

INSERT INTO TURMA (tur_id, tur_ano_escolar, tur_ano, uni_id, pro_id) VALUES
	(1, 1, 2022, 1, 1),
	(4, 2, 2022, 2, 4),
	(2, 2, 2022, 1, 3),
	(3, 1, 2022, 2, 2),
	(5, 1, 2022, 3, 5),
	(6, 2, 2022, 3, 6),
	(7, 1, 2022, 4, 7),
	(8, 2, 2022, 4, 8),
	(9, 1, 2023, 1, 1),
	(10, 2, 2023, 1, 3),
	(11, 1, 2023, 2, 2),
	(12, 2, 2023, 2, 4),
	(13, 1, 2023, 5, 9),
	(14, 1, 2023, 6, 10);

INSERT INTO TIPO_ALUNO (tip_alu_id, tip_alu_desc) VALUES
	(1, 'Normal'),
	(2, 'Especial'),
	(3, 'Superdotado');

INSERT INTO ALUNO (alu_id, alu_primeiro_nome, alu_segundo_nome, alu_data_nascimento, tip_alu, tur_id) VALUES
	(1, 'Hasheem', 'Marzelo', '2017-05-24', 1, 1),
	(2, 'Iosep', 'Breens', '2018-03-15', 1, 5),
	(3, 'Matthias', 'Dan', '2017-06-09', 2, 2),
	(4, 'Annissa', 'McGraw', '2017-09-25', 3, 4),
	(5, 'Earle', 'Kencott', '2015-03-10', 3, 5),
	(6, 'Callean', 'Domerc', '2016-09-13', 2, 5),
	(7, 'Gerald', 'Heaney', '2016-08-19', 2, 4),
	(8, 'Bing', 'Berrecloth', '2017-03-06', 1, 4),
	(9, 'Orton', 'Philippson', '2017-01-18', 1, 1),
	(10, 'Celinda', 'Bachnic', '2015-07-13', 3, 2),
	(11, 'Archy', 'Commucci', '2018-06-08', 2, 1),
	(12, 'Glennis', 'Kierans', '2017-02-27', 1, 1),
	(13, 'Joey', 'Pinks', '2016-04-08', 1, 1),
	(14, 'Sawyer', 'Mathew', '2015-03-02', 1, 3),
	(15, 'Juliette', 'Grancher', '2015-04-30', 1, 5),
	(16, 'Roobbie', 'Keirl', '2018-09-27', 1, 5),
	(18, 'Lexy', 'Burge', '2017-01-19', 2, 3),
	(17, 'Briggs', 'Pocke', '2018-11-16', 1, 2),
	(19, 'Rivkah', 'Nickols', '2016-03-07', 1, 4),
	(20, 'Melisse', 'MacGille', '2016-11-30', 1, 5);

INSERT INTO AVALIACAO (ava_id, tip_aval_id, ava_data, ava_nota, alu_id, pro_id) VALUES 
    (1, 1, '2023-06-10 09:00:00', 8.5, 1, 1),
    (2, 2, '2023-06-10 10:30:00', 7.2, 2, 2),
    (3, 3, '2023-06-10 11:45:00', 9.0, 3, 3),
    (4, 1, '2023-06-10 13:15:00', 6.8, 4, 4),
    (5, 2, '2023-06-10 14:30:00', 9.5, 5, 5),
    (6, 3, '2023-06-10 15:45:00', 8.0, 6, 6),
    (7, 1, '2023-06-10 17:00:00', 7.6, 7, 7),
    (8, 2, '2023-06-10 18:15:00', 9.8, 8, 8),
    (9, 3, '2023-06-10 19:30:00', 6.5, 9, 9),
    (10, 1, '2023-06-10 20:45:00', 8.2, 10, 10);

INSERT INTO COLETA (col_id, col_audio, col_metrica, fra_id, ava_id) VALUES
	(1, '//servidor1/aluno1/audio01.mp3', 6.9, 1, 1),
	(2, '//servidor1/aluno1/audio02.mp3', 6.9, 2, 2),
	(3, '//servidor1/aluno1/audio03.mp3', 6.9, 3, 3),
	(4, '//servidor1/aluno1/audio04.mp3', 6.9, 4, 4),
	(5, '//servidor1/aluno2/audio01.mp3', 6.9, 1, 5),
	(6, '//servidor1/aluno2/audio02.mp3', 6.9, 2, 6),
	(7, '//servidor1/aluno3/audio01.mp3', 6.9, 5, 7),
	(8, '//servidor1/aluno3/audio02.mp3', 6.9, 7, 8),
	(9, '//servidor1/aluno11/audio01.mp3', 6.9, 9, 9),
	(10, '//servidor1/aluno10/audio01.mp3', 6.9, 6, 10);

INSERT INTO CONTRATO (con_id, con_data_ini, con_data_fim, tip_con_id, uni_id) VALUES
	(1, '2022-01-01', '2023-01-01', 1, 1),
	(2, '2023-02-01', '2023-02-01', 2, 2),
	(3, '2021-01-01', '2025-01-01', 3, 5);
