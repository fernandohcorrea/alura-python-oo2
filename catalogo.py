class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome; novo_nome.title()

    def __str__(self):
        return f'{programa.nome} - {self.ano} - {programa.likes} likes'


class Filme(Programa) :

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{programa.nome} - {self.ano} - {self.duracao} min - {programa.likes} likes'


class Serie(Programa) :

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{programa.nome} - {self.ano} - {self.temporadas} temporadas - {programa.likes} likes'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    @property
    def programas(self) : 
        return self.__programas

    @property
    def size(self):
        return len(self.__programas)


if( __name__ == '__main__'):

    vindadores = Filme('Vidadores - guerra infinita', 2018 ,160)
    vindadores.dar_like()
    vindadores.dar_like()
    vindadores.dar_like()
    
    dune = Filme('Dune', 2021 ,160)
    dune.dar_like()
    dune.dar_like()

    tmep = Filme('Todo mundo em pânico', 2015 ,160)
    tmep.dar_like()

    atlanta = Serie('Atanta', 2018, 2)
    spartacus = Serie('Spartacus', 2019, 2)
    spartacus.dar_like()
    spartacus.dar_like()


    catalogo_filmes_series = [ vindadores, dune, spartacus, tmep ]

    pl_fim_de_semana = Playlist('Fin de semanda', catalogo_filmes_series)

    print(f'Tamanho da minha playlist: {pl_fim_de_semana.size}')

    for programa in pl_fim_de_semana.programas:
        print(programa)

    print(f'Ta ou não esta? {dune in pl_fim_de_semana.programas}')