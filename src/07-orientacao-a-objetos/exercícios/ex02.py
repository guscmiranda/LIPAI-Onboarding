

class Projeto:
    def __init__(self, string):
        infos_linha = string.split(",")
        self.codigo = int(infos_linha[0])
        self.titulo = infos_linha[1]
        self.responsavel = infos_linha[2]

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if not value and value != 0:
            raise ValueError("Código não pode ser vazio ou nulo.")
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Título não pode ser vazio ou nulo.")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Responsável não pode ser vazio ou nulo.")
        self._responsavel = value

    def print_projeto(self):
        print("Código:", self.codigo)
        print("Título:", self.titulo)
        print("Responsável:", self.responsavel)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False


projeto = Projeto('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto2 = Projeto('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto3 = Projeto('2,LIPAI,Marcelo')
projeto.print_projeto()
projeto2.print_projeto()
projeto3.print_projeto()

if projeto == projeto2:
    print("São iguais!!!")
else:
    print("São diferentes!!!")

if projeto == projeto3:
    print("São iguais!!!")
else:
    print("São diferentes!!!")
