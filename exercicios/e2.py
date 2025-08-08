class Musica:

    nome = ''

    artista = ''

    duracao = int

    playlist = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.playlist.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista}'
    
    def listar_musicas():
        for musicas in Musica.playlist:
            print(f'Musica: {musicas.nome} | Artista: {musicas.artista} | Duração: {musicas.duracao} minutos') 

vida_loka = Musica('Vida Loka', 'Mano B.','2')

Musica.listar_musicas()
