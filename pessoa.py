from operator import truediv


class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True,trabalhando=False, salario=None):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_codigo(self):
        return self.__codigo
    def get_estudando(self):
        return self._estudando
    def get_trabalhando(self):
        return self._trabalhando
    def get_salario(self):
        return self._salario
    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print("salario invalido")

    def is_trabalhando(self):
        return self._trabalhando
    def is_estudando(self):
        return self._estudando

    def set_trabalhando(self, status):
        if self._trabalhando and status:
            print("ja esta trabalhando")
        elif not self._trabalhando and status:
            print("que vida boa")
        elif not self._trabalhando and status:
            self._trabalhando = status
            self.set_salario(100)
        else:
            self._trabalhando = status
            self.set_salario(0)

    def set_trabalhando(self, status):
         if self._trabalhando and status:
             print("ja esta trabalhando")
         elif not self._trabalhando and status:
             print("que vida boa")
         elif not self._trabalhando and status:
             self._trabalhando = status
             self.set_salario(100)


    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += 100
            print(f"{self.nome} Começou trabalhar!")
        else:
            print(f"{self.nome} ja esta trabalhando")

    def estudar(self):
        if not self.estudando:
            self.estudando = True
            print(f"{self.nome} começou a estudar!")
        elif self.estudando and self.trabalhando:
            self.salario += 1000
            print(
                f"`{self.nome}"
                f"começou a estudar e aumentou seu salario para "
                f"R${self.salario:.2f}"
            )
        else:
            print(f"{self.nome} ja esta estudando")

    def apresentar(self):
        print(f'ola sou {self.nome}\n'
              f'minha data de nascimento é {self.data_nascimento} '
              f'meu codigo é {self.codigo}'
              )
        if self.estudando:
            print(' estou estudando')
        else:
            print(f"não esta estudando")

        if self.trabalhando:
            print('trabalhando')
        else:
            print(f"não estou trabalhando")

        print("-" * 50)

class Bebe(Pessoa): # herda da classe Pessoa
    def __init__(self, nome, data_nascimento, registro):
        super().__init__(nome, data_nascimento, registro)
        self.fome = True
        self.chorando = True
        self.dormindo = False

    def mamar (self):
        if self.fome:
            print(f"bebe está mamando")
            self.fome = False
            self.chorando = False
        else:
            print(f'bebe não está com fome')




    def dormir(self):
        if not self.dormindo:
            if not self.chorando:
                self.dormindo = True
                print("bebe esta dormindo")
            else:
                print('bebe n pode dormir, esta com fome')
        else:
            print(f"{self.nome} ja esta dormindo")

    def apresentar(self):
        if self.fome:
            print(f"bebe chorando  com fome")
        else:
            print('bebe não esta com fome')
            if self.dormindo:
                print('bebe dormindo')







p1 = Pessoa("vitor","27/09/2007","157")
B1 = Bebe('vitor', '26/01/2025', '2')
B1.mamar()
B1.dormir()
B1.apresentar()
print('-_-' * 20)
p1.apresentar()