from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['data_hora', 'celebracao',
                  'hoje_minha_decisao_foi', 'nome', 'nascimento', 'idade', 'cpf',
                  'profissao', 'email', 'endereco', 'compl', 'bairro', 'cidade', 'estado', 'celular_whatsapp', 'campus',
                  'tipo_de_preenchimento', 'nome_atendente', 'codigo_membro_ic', 'supervisor', 'email_membro',
                  'celular_membro_whatsapp', 'discipulador_pessoal', 'coordenador_recomeco', 'supervisor_recomeco'
                  ]
