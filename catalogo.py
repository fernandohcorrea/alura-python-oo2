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



class Filme(Programa) :

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa) :

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



if( __name__ == '__main__'):

    filme = Filme('Vidadores - guerra infinita', 2018 ,160)
    filme.dar_like()
    filme.dar_like()
    serie = Serie('Atanta', 2018, 2)
    serie.dar_like()

    print(f'Nome: {filme.nome} - Ano:  {filme.ano} -  Duração: {filme.duracao} - Likes: {filme.likes}')
    print(f'Nome: {serie.nome} - Ano:  {serie.ano} -  Temporadas: {serie.temporadas} - Likes: {serie.likes}')


