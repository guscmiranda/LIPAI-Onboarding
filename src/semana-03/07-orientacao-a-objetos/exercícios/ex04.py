

class Aluno:
    def __init__(self, string):
        infos_linha = string.split(",")
        self.prontuario = infos_linha[0]
        self.nome = infos_linha[1]
        self.email = infos_linha[2]

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError("Prontuário não pode ser vazio ou nulo.")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("Nome não pode ser vazio ou nulo.")
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email não pode ser vazio ou nulo.")
        self._email = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False


aluno = Aluno('SP0101,João da Silva,joao@email.com')


class Projeto:
    def __init__(self, string):
        infos_linha = string.split(",")
        self.codigo = infos_linha[0]
        self.titulo = infos_linha[1]
        self.responsavel = infos_linha[2]
        self.participacoes = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if not value:
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

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False

    def add_participacao(self, participacao):
        if isinstance(participacao, Participacao):
            self.participacoes.append(participacao)
        else:
            raise TypeError("Deve ser um objeto do tipo Participacao.")

    def print_projeto(self):
        print("Código:", self.codigo)
        print("Título:", self.titulo)
        print("Responsável:", self.responsavel)
        for p in self.participacoes:
            print(
                f" Aluno: {p.aluno.nome}, {p.data_inicio} - {p.data_fim}")


projeto = Projeto('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    def print_participacao(self):
        print("Código:", self.codigo)
        print("Data inicio:", self.data_inicio)
        print("Data fim:", self.data_fim)
        print("Aluno:", self.aluno.nome)
        print("Projeto:", self.projeto.titulo)


part = Participacao(1, '1/1/2001', '19/12/2001', aluno, projeto)

projeto.add_participacao(part)

projeto.print_projeto()
