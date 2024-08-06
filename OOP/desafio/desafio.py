
from bioclass.reino import Reino
from bioclass.filo import Filo
from bioclass.classe import Classe
from bioclass.ordem import Ordem
from bioclass.familia import Familia
from bioclass.genero import Genero
from bioclass.especie import Especie
from bioclass.individuo import Individuo





#Reinos
animalia = Reino('Animalia', 'Heretotrófico', 'Multicelular', 'Aeróbico')

#Filos
chordata = Filo(filo='Chordata',caract_filo='Espinha dorsal oca percorrida por um cordão nervoso')
chordata.addReino(animalia)

#Classes
mamalia = Classe(classe='Mammalia', caract_classe='Presença de pelos, glândulas mamárias, diafragma e dentes diferenciados')
mamalia.addFilo(chordata)

#Ordems
primata = Ordem(ordem='Primata', caract_ordem='Cérebro grande, olhos voltados para a frente e polegares opositores')
primata.addClasse(mamalia)
carnivora = Ordem(ordem='Carnivora', caract_ordem='Presença de pés com quatro ou cinco dedos, apresentando garras; machos com báculo; e dentes adaptados para cortar, com presença de caninos fortes, cônicos e pontiagudos')
carnivora.addClasse(mamalia)
#Familias
hominidae = Familia(familia='Hominidae', caract_familia='Dedos com unha, pólex e hálux (com exceção dos humanos) oponíveis e dentição com dois pré-molares')
hominidae.addOrdem(primata)
atelidae = Familia(familia='Atelidae', caract_familia='Têm caudas adaptadas para agarrar e manipular objetos')
atelidae.addOrdem(primata)
canidae = Familia(familia='Canidae', caract_familia='Garras não retrácteis adaptadas para tração em corrida. O tamanho é variável, bem como os hábitos sociais que podem ser gregários')
canidae.addOrdem(carnivora)
felidae = Familia(familia='Felidae', caract_familia='Possuem corpos ágeis e flexíveis com pernas musculosas')
felidae.addOrdem(carnivora)
#Generos
homo = Genero(genero='Homo', caract_genero='Mais robustos que os outros primatas, têm crânio maior e cérebro mais desenvolvido')
homo.addFamilia(hominidae)
ateles = Genero(genero='Ateles', caract_genero='usam uma locomoção suspensa rápida e são caracterizados por corpos e membros alongados que se adaptaram ao seu padrão locomotor distinto')
ateles.addFamilia(atelidae)
canis = Genero(genero='Canis', caract_genero='As espécies deste gênero se distinguem por seu tamanho moderado a grande, crânios e dentição enormes e bem desenvolvidos, pernas longas e orelhas e caudas comparativamente curtas.')
canis.addFamilia(canidae)
felis = Genero(genero='Felis', caract_genero='Crânios altos e largos, mandíbulas curtas e orelhas estreitas com tufos curtos, mas sem manchas brancas na parte posterior das orelhas')
felis.addFamilia(felidae)
#Especies
humano = Especie(especie='Homo Sapiens Sapiens', nome_popular='Humano')
humano.addGenero(homo)
neandertal = Especie(especie= 'Homo neanderthalensis', nome_popular='homem de Neandertal')
neandertal.addGenero(homo)
macacoAranha = Especie(especie='Ateles Fusciceps', nome_popular='Macaco-aranha')
macacoAranha.addGenero(ateles)
macacoTesta = Especie(especie='Ateles marginatus', nome_popular='macaco-aranha-de-testa-branca')
macacoTesta.addGenero(ateles)
cachorro = Especie(especie='Canis lupus familiaris', nome_popular='Cachorro')
cachorro.addGenero(canis)
loboEt = Especie(especie='Canis simensis', nome_popular='chacal-vermelho')
loboEt.addGenero(canis)
gato = Especie(especie='Felis Silvestris Catus', nome_popular='Gato')
gato.addGenero(felis)
gatoDeserto = Especie(especie='Felis margarita', nome_popular='Gato-do-Deserto')
gatoDeserto.addGenero(felis)

animals = [humano, neandertal, macacoAranha, macacoTesta, cachorro, loboEt, gato, gatoDeserto]

for animal in animals:
    print(animal)
