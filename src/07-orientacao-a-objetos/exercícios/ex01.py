

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

    def print_aluno(self):
        print("Protuário:", self.prontuario)
        print("Nome:", self.nome)
        print("Email:", self.email)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False


aluno = Aluno('SP0101,João da Silva,joao@email.com')
aluno2 = Aluno('SP0101,João da Silva,joao@email.com')
aluno3 = Aluno('SP1111,Felipe Luis, felu@email.com')
aluno.print_aluno()
aluno2.print_aluno()
aluno3.print_aluno()

if aluno == aluno2:
    print("São iguais!!!")
else:
    print("São diferentes!!!")

if aluno == aluno3:
    print("São iguais!!!")
else:
    print("São diferentes!!!")
