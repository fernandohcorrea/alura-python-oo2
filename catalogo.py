class Filme :

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome; novo_nome.title()

    @property
    def likes(self):
        return self.__likes

class Serie :

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome; novo_nome.title()

    @property
    def likes(self):
        return self.__likes


if( __name__ == '__main__'):

    filme = Filme('Vidadores - guerra infinita', 2018 ,160)
    filme.dar_like()
    filme.dar_like()
    serie = Serie('Atanta', 2018, 2)
    serie.dar_like()

    print(f'Nome: {filme.nome} - Ano:  {filme.ano} -  Duração: {filme.duracao} - Likes: {filme.likes}')
    print(f'Nome: {serie.nome} - Ano:  {serie.ano} -  Temporadas: {serie.temporadas} - Likes: {serie.likes}')


