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



if( __name__ == '__main__'):

    filme = Filme('Vidadores - guerra infinita', 2018 ,160)
    filme.dar_like()
    filme.dar_like()
    serie = Serie('Atanta', 2018, 2)
    serie.dar_like()

    catalogo_filmes_series = [ filme, serie ]

    for programa in catalogo_filmes_series:
        print(programa)
