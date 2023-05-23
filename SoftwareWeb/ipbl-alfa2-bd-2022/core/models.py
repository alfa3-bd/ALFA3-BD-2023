from django.db import models

class TipoAluno(models.Model):
    tip_alu_id = models.AutoField(primary_key=True, db_column='tip_alu_id')
    tip_alu_desc = models.CharField(db_column='tip_alu_desc', max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_aluno'

class TipoEscola(models.Model):
    tip_escola_id = models.AutoField(primary_key=True, db_column='tip_escola_id')
    tip_escola_desc = models.CharField(db_column='tip_escola_desc', max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_escola'

class TipoFrase(models.Model):
    tip_frase_id = models.AutoField(primary_key=True, db_column='tip_frase_id')
    tip_frase_desc = models.CharField(db_column='tip_frase_desc', max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_frase'

class Frase(models.Model):
    fra_id = models.AutoField(primary_key=True, db_column='fra_id')
    fra_frase = models.CharField(db_column='fra_frase', max_length=255)
    tipo = models.ForeignKey(TipoFrase, on_delete=models.CASCADE,db_column='tip_frase')

    class Meta:
        managed = False
        db_table = 'frase'

class CategoriaEscolar(models.Model):
    cat_escola_id = models.AutoField(primary_key=True, db_column='cat_escola_id')
    cat_escola_desc = models.CharField(db_column='cat_escola_desc', max_length=255)

    class Meta:
        managed = False
        db_table = 'categoria_escolar'

class Cidade(models.Model):
    cid_id = models.AutoField(primary_key=True, db_column='cid_id')
    cid_nome = models.CharField(db_column='cid_nome', max_length=255)
    cid_uf = models.CharField(db_column='cid_uf', max_length=255)
    cid_pais = models.CharField(db_column='cid_pais', max_length=255)

    class Meta:
        managed = False
        db_table = 'cidade'

class Endereco(models.Model):
    end_id = models.AutoField(primary_key=True, db_column='end_id')
    end_rua = models.CharField(db_column='end_rua', max_length=255)
    end_numero = models.IntegerField(db_column='end_numero')
    end_cep = models.CharField(db_column='end_cep', max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,db_column='cid_id')

    class Meta:
        managed = False
        db_table = 'endereco'

class Professor(models.Model):
    pro_id = models.AutoField(primary_key=True, db_column='pro_id')
    pro_primeiro_nome = models.CharField(db_column='pro_primeiro_nome', max_length=255)
    pro_segundo_nome = models.CharField(db_column='pro_segundo_nome', max_length=255)
    pro_identificador = models.CharField(db_column='pro_identificador', max_length=255)
    pro_senha = models.CharField(db_column='pro_senha', max_length=255)

    class Meta:
        managed = False
        db_table = 'professor'

class GestorEscola(models.Model):
    ges_id = models.AutoField(primary_key=True, db_column='ges_id')
    ges_primeiro_nome = models.CharField(db_column='ges_primeiro_nome', max_length=255)
    ges_segundo_nome = models.CharField(db_column='ges_segundo_nome', max_length=255)
    ges_identificador = models.CharField(db_column='ges_identificador', max_length=255)
    ges_senha = models.CharField(db_column='ges_senha', max_length=255)
    ges_ges_id = models.IntegerField(db_column='ges_ges_id')

    class Meta:
        managed = False
        db_table = 'gestor_escola'

class UnidadeEscolar(models.Model):
    uni_id = models.AutoField(primary_key=True, db_column='uni_id')
    uni_codigo_inep = models.IntegerField(db_column='uni_codigo_inep')
    uni_nome = models.CharField(db_column='uni_nome', max_length=255)
    categoria = models.ForeignKey(CategoriaEscolar, on_delete=models.CASCADE,db_column='cat_esc')
    tipo = models.ForeignKey(TipoEscola, on_delete=models.CASCADE,db_column='tip_esc')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE,db_column='end_id')
    gestor = models.ForeignKey(GestorEscola, on_delete=models.CASCADE,db_column='ges_id')

    class Meta:
        managed = False
        db_table = 'unidade_escolar'

class Turma(models.Model):
    tur_id = models.AutoField(primary_key=True, db_column='tur_id')
    tur_ano = models.CharField(db_column='tur_ano', max_length=255)
    tur_ano_escolar = models.CharField(db_column='tur_ano_escolar', max_length=255)
    escola = models.ForeignKey(UnidadeEscolar, on_delete=models.CASCADE,db_column='uni_id')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,db_column='pro_id')

    class Meta:
        managed = False
        db_table = 'turma'

class Aluno(models.Model):

    alu_id = models.AutoField(primary_key=True, db_column='alu_id')
    alu_primeiro_nome = models.CharField(db_column='alu_primeiro_nome', max_length=255)
    alu_segundo_nome = models.CharField(db_column='alu_segundo_nome', max_length=255)
    alu_data_nascimento = models.DateField(db_column='alu_data_nascimento')
    turma = models.ForeignKey(Turma,on_delete=models.CASCADE,db_column='tur_id')
    tipo = models.ForeignKey(TipoAluno,on_delete=models.CASCADE,db_column='tip_alu')

    class Meta:
        managed = False
        db_table = 'aluno'

