package iV_Estoque;

import java.util.ArrayList;
public class Fornecedor {
    private int cnpj;
    private String nome;
    private ArrayList<Produto> produtos = new ArrayList<Produto>();

    //Método construtor
    public Fornecedor(int cnpj, String nome) {
        this.cnpj = cnpj;
        this.nome = nome;
    }

    //Métodos Getters
    public int getCnpj() {
        return this.cnpj;
    }
    public String getNome() {
        return this.nome;
    }
    public ArrayList<Produto> getListaProdutos() {
        return this.produtos;
    }

    public void incluirProduto(Produto p) {
        produtos.add(p);
    }
}
