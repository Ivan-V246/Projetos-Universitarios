# Sistema Bancário

**Projeto criado como solução de uma atividade proposta na disciplina de Programação Orienteada a Objeto.**

&nbsp; O código tem como objetivo simular um sistema bancário, se organizando em três classes distintas:

## - **Pessoa** 

#### Atributos 

&nbsp; 1. cpf 
&nbsp; &nbsp; &nbsp;  2. nome

&nbsp; 3. conta
&nbsp; 4. senha
_____
#### Métodos

&nbsp;*Validar*() -> Retorna *True* caso a pessoa seja válido; Retorna *false* caso contrário.

## - **Conta** 

#### Atributos 

&nbsp; 1. numero
&nbsp; 2. saldo

&nbsp; 3. extrato
&nbsp; 4. dono
_____
#### Métodos

&nbsp;*Credito*(double) -> Aumenta o saldo da conta no valor desejado.

&nbsp;*Debito*(double) -> Reduz o saldo da conta no valor desejado. 

&nbsp;*Validar*() -> Retorna *True* caso a conta seja válida; Retorna *false* caso contrário.

## - **Banco** 

#### Atributos 

&nbsp; 1. contas[] 
&nbsp; &nbsp; &nbsp;  2. posContas

&nbsp; 3. pessoas[]
&nbsp; &nbsp;4. posPessoas
_____
#### Métodos

&nbsp;*CadastrarPessoa*(Pessoa) -> Cadastra a Pessoa desejada.

&nbsp;*CadastrarConta*(Conta, int) -> Cadastra a Conta desejada para a Pessoa desejada.

&nbsp;*PesquisarPessoa*(int) -> Retorna o índice caso a pessoa esteja cadastrada; Retorn *null* caso o contrário.

&nbsp;*PesquisarConta*(int) -> Retorna o índice caso a conta esteja cadastrada; Retorn *null* caso o contrário.

&nbsp;*Saldo*(int, String) -> Retorna o saldo da conta caso o acesso e a Conta seja válida; Retorna *-99999* caso o contrário.

&nbsp;*Deposito*(int, double) -> Deposita o valor desejado em uma conta desejada.

&nbsp;*Saque*(int, double, String) -> Saca o valor desejado da conta caso o acesso seja válido.

&nbsp;*Extrato*(int, String) -> Retorna o extrato da conta desejada caso o acesso seja válido.

&nbsp;*Transfere*(int, String, int, double) -> Transfere o valor desejado de uma conta para outra caso o acesso seja válido.

## Obs
- Cada Pessoa só pode ter no máximo uma Conta associada a ela.

- Os acessos as Contas através dos métodos da classe Banco são validados através da senhas.