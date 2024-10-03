from models.funcionario        import Funcionario
from models.endereco           import Endereco
from models.enums.sexo         import Sexo
from models.enums.estadoCivil  import EstadoCivil
from models.enums.setor        import Setor

class Engenheiro(Funcionario):
    def init(self,id:str,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 estadoCivil:EstadoCivil, 
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,setor:Setor,salario:float) -> None:
        super().init(id, nome ,telefone ,email ,endereco ,sexo ,estadoCivil ,dataNascimento)
        self.oab = self._verificar_oab(oab)