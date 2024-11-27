from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    is_avaliador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - Avaliador: {'Sim' if self.is_avaliador else 'Não'}"

class ONG(models.Model):
    nome = models.CharField(max_length=255,default='ONG')
    cnpj = models.CharField(max_length=18, default='00.000.000/0001-00')
    endereco = models.CharField(max_length=255,null=True, blank=True,default='Rua')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    informacao = models.TextField(blank=True, null=True)
    imagem = models.CharField(max_length=1000, null=True, blank=True, default='https://www.google.com/imgres?q=default%20coloque%20sua%20imagem&imgurl=https%3A%2F%2Fwww.quadrorama.com.br%2Fwp-content%2Fuploads%2F2018%2F05%2Fquadro-com-foto-imagem-personalizada.png&imgrefurl=https%3A%2F%2Fwww.quadrorama.com.br%2Fproduto%2Ffoto-personalizada%2F&docid=Rf3tWzXG5ZJ58M&tbnid=JyJzwRzOMJN5vM&vet=12ahUKEwiPsNa60_qJAxVYq5UCHfzfCAYQM3oECFAQAA..i&w=351&h=497&hcb=2&ved=2ahUKEwiPsNa60_qJAxVYq5UCHfzfCAYQM3oECFAQAA')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ong',null=True)
    telefone = models.CharField(max_length=30, default='(00) 00000-0000')
    whatsapp = models.CharField(max_length=30, default='http://wa.me/5581994382896')
    capacidade_maxima = models.FloatField(default=0)

    def __str__(self):
        return self.nome
    @property
    def capacidade(self):
        return sum(residuo.peso for residuo in self.residuos.all())
    @property
    def capacidade_percentual(self):
        if self.capacidade_maxima > 0:
            return (self.capacidade / self.capacidade_maxima) * 100
        return 0

class Residuos(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='residuos')
    tipo = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    peso = models.FloatField(blank=True, null=True)
    status = models.CharField(
        max_length=50, 
        choices=[('armazenado', 'Armazenado'), ('reciclado', 'Reciclado'), ('descartado', 'Descartado')]
    )
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.quantidade} unidades"
    
class AvaliacaoONG(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('ong', 'usuario')

    def __str__(self):
        return f"{self.ong.nome} - {self.nota} ({self.usuario.username})"
    
class RemoverAvaliacao(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='remover_avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remover_avaliacoes')

    class Meta:
        unique_together = ('ong', 'usuario')

    def __str__(self):
        return f"{self.ong.nome} - {self.usuario.username}" 
    
class EditarAvaliacao(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='editar_avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editar_avaliacoes')

    class Meta:
        unique_together = ('ong', 'usuario')

    def __str__(self):
        return f"{self.ong.nome} - {self.usuario.username}" 