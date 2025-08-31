# Estoque
&nbsp;
**Projeto criado como solução de uma atividade proposta na disciplina de Programação Orienteada a Objeto.**

&nbsp; O projeto se visa simular o estoque de um supermercado, se organizando em quatro classes principais:

## - **Produto**

#### Atributos

&nbsp; 1. cod
&nbsp; &nbsp;&nbsp; &nbsp;2. desc
&nbsp; &nbsp;&nbsp;3. compra 

&nbsp; 4. venda
&nbsp; 5. lucro
&nbsp;&nbsp; 6. quant

&nbsp; 7. min 
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; 8. listaF<>
&nbsp; 9. extrato<>

---
#### **Métodos**

&nbsp;*compra*(int, double) -> Realiza uma compra da quantidade desejada, cada unidade pelo valor desejado para aquele produto. Ambos os valores devem ser maiores do que zero.

&nbsp;*venda(int)* -> Vende a quantidade desejada daquele produto. O valor deve ser maior do que zero.

&nbsp;*pesquisarFornecedor*(int) -> Retorna a posição do fornecedor dono do cnpj desejado caso o mesmo já esteja cadastrado para aquele produto. Retorna -1 caso o contrário.

&nbsp;*incluirF*(Fornecedor) -> Cadastra o fornecedor desejado ao produto.

&nbsp;*suficiente*() -> Retorna *True* caso a quantidade daquele produto seja maior ou igual a quantidade mínima. Retorna *false* caso contrário.

&nbsp; *movimentos*(Date, Date) -> Retorna uma string com todas as movimentações que ocorreram com aquele produto dentro do espaço de tempo desejado. Retorna uma string vazia caso não tenha havido nenhuma. 

## - **Fornecedor** 

#### Atributos

&nbsp; 1. cnpj

&nbsp; 2. nome

&nbsp; 3. produtos<>

#### Métodos

&nbsp; *incluirP*(Produto) -> Adiciona um produto a lista daquele fornecedor.

## - **Ocorrencia**

&nbsp; 1. data
&nbsp; &nbsp; 2. tipo
&nbsp; &nbsp;&nbsp; 3. quant

&nbsp; 4. valor
&nbsp; 5. qAtual
&nbsp; 6. total

## - **Estoque** 

#### Atributos 

&nbsp; 1. produtos<>

&nbsp; 2. fornecedores<>

#### Métodos

&nbsp;*pesquisarProduto*(int) -> Retorna a posição do Produto associado ao código desejado caso o mesmo já esteja cadastrado. Retorna -1 caso o contrário.

&nbsp; *incluir*(Produto) -> Cadastra o produto desejado caso o mesmo não esteja cadastrado.

&nbsp; *comprar*(int, int, double) -> Caso o produto esteja cadastrado, realiza uma compra da quantidade desejada pelo valor desejado.

&nbsp; *vender*(int, int) -> Caso o produto esteja cadastrado, realiza uma venda da quantidade desejada.

&nbsp; *quantidade*(int) -> Caso o produto esteja cadastrado, retorna a quantidade disponível atual dele. Retorna *-1* caso o contrário.

&nbsp; *movimentacao*(int, Date, Date) -> Caso o produto esteja cadastrado, retorna uma string contendo todas as movimentações que ocorrem no período desejado. Retorna uma string vazia caso o contrário.

&nbsp; *fornecedores*(int) -> Caso o produto esteja cadastrado, retorna uma lista dos fornecedores deles. Retorna *null* caso o contrário.

&nbsp; *estoqueAbaixoDoMinimo*() -> Retorna uma lista contendo todos os produtos cadastrados que possuem menos unidades disponíveis do que o mínimo para eles.

&nbsp; *adicionarFornecedor*(int, Fornecedor) -> Caso o produto esteja cadastrado, adiciona o Fornecedor desejado a lista de fornecedores dele.

&nbsp; *precoDeVenda*(int) -> Caso o produto esteja cadastrado, retorna seu atual preço de venda. Retorna *-1* caso o contrário.

&nbsp; *precoDeCompra*(int) -> Caso o produto esteja casdastrado, retorna seu atual preço de compra. Retorna -1 caso o contrário.

## Obs 

- O preço de compra de um produto é calculado a cada nova compra seguindo a seguinte fórmula: 

*( (Preço de compra atual * Quantidade atual) + (Preço da nova compra * Quantidade comprada) ) /
(Quantidade atual + Quantidade Comprada)*

- O preço de venda de um produto é calculado a cada vez que o preço de compra se altera, pela seguinte fórmula:

*(Preço de compra atual * (1 + lucro))*