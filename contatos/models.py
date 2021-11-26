from django.db import models


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

DISCP = (
    ("Sim", "Sim"),
    ("Não", "Não"),
)

TIPO = (
    ("Cartão preenchido pelo decidido", "Cartão preenchido pelo decidido"),
    ("Cartão preenchido em atendimento", "Cartão preenchido em atendimento"),
)

CELEBRACAO = (
    ("Dominical", "Dominical"),
    ("Eleve", "Eleve"),
    ("Juniores", "Juniores"),
    ("Outros", "Outros"),
)

DECISAO = (
    ("Aceitar a Jesus Cristo como Salvador", "Aceitar a Jesus Cristo como Salvador"),
    ("Reconciliar-me com Cristo e a Igreja", "Reconciliar-me com Cristo e a Igreja"),
    ("Ser batizado em águas", "Ser batizado em águas"),
)

UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)

class Person(models.Model):
    data_hora = models.CharField(max_length=30, blank=True)
    celebracao = models.CharField(max_length=150, choices=CELEBRACAO)
    hoje_minha_decisao_foi = models.CharField(max_length=150, choices=DECISAO)
    nome = models.CharField(max_length=50, blank=True)
    nascimento = models.CharField(max_length=30, blank=True)
    idade = models.CharField(max_length=30, blank=True)
    cpf = models.CharField(max_length=30, blank=True)
    profissao = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    endereco = models.CharField(max_length=150, blank=True)
    compl = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=2, choices=UF_CHOICES)
    celular_whatsapp = models.CharField(max_length=30, blank=True)
    campus = models.CharField(max_length=30, blank=True)
    tipo_de_preenchimento = models.CharField(max_length=150, choices=TIPO)
    nome_atendente = models.CharField(max_length=30, blank=True)
    codigo_membro_ic = models.CharField(max_length=30, blank=True)
    supervisor = models.CharField(max_length=30, blank=True)
    email_membro = models.CharField(max_length=30, blank=True)
    celular_membro_whatsapp = models.CharField(max_length=30, blank=True)
    discipulador_pessoal = models.CharField(max_length=3, choices=DISCP)
    coordenador_recomeco = models.CharField(max_length=30, blank=True)
    supervisor_recomeco = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)


def __str__(self):
        return self.first_name + ' ' + self.last_name


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero
