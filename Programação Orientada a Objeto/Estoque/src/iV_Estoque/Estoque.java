package iV_Estoque;

import java.util.ArrayList;
import java.util.Date;
public class Estoque {
    private ArrayList<Produto> produtos = new ArrayList<Produto>();
    private ArrayList<Fornecedor> fornecedores = new ArrayList<Fornecedor>();

    //Método de Checagem
    public int pesquisarProduto (int cod) {
        for(int i = 0; i < produtos.size(); i++) {
            if(cod == produtos.get(i).getCod()) {
                return i;
            }
        }
        return -1;
    }

    public void incluir(Produto p) {
        int pos = pesquisarProduto(p.getCod());
        if(pos == -1) {
            produtos.add(p);
        } else {
            System.out.println("Produto já cadastrado!");
        }
    }

    public void comprar(int cod, int quant, double preco) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não existe no estoque!");
        } else {
            produtos.get(pos).compra(quant, preco);
        }
    }

    public double vender(int cod, int quant) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não existe no estoque!");
            return pos;
        } else {
            double v = produtos.get(pos).venda(quant);
            if(v == -1) {
                System.out.println("Não há unidades suficientes deste produto.");
            } else {
                System.out.println("Venda efetuada com sucesso!");
            }
            return v;
        }
    }

    public int quantidade(int cod) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não existe no estoque!");
            return -1;
        } else {
            return produtos.get(pos).getQuant();
        }
    }

    public String movimentacao(int cod, Date inicio, Date fim) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não cadastrado.");
            return "";
        } else {
            return produtos.get(pos).movimentos(inicio, fim);
        }
    }

    public ArrayList<Fornecedor> fornecedores(int cod) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não cadastrado!");
            return null;
        } else {
            return produtos.get(pos).getListaf();
        }
    }

    public ArrayList<Produto> estoqueAbaixoDoMinimo() {
        ArrayList <Produto> resp = new ArrayList<Produto>();
        for(int i = 0; i < produtos.size(); i++) {
            if(!(produtos.get(i).suficiente())) {
                resp.add(produtos.get(i));
            }
        }
        return resp;
    }

    public void adicionarFornecedor(int cod, Fornecedor f) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não cadastrado.");
        } else {
            produtos.get(pos).incluirF(f);
        }
    }

    public double precoDeVenda(int cod) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("Produto não existe no estoque!");
            return -1;
        } else {
            return produtos.get(pos).getVenda();
        }
    }

    public double precoDeCompra(int cod) {
        int pos = pesquisarProduto(cod);
        if(pos == -1) {
            System.out.println("iV_Estoque.Produto não existe no estoque!");
            return -1;
        } else {
            return produtos.get(pos).getCompra();
        }
    }
}
