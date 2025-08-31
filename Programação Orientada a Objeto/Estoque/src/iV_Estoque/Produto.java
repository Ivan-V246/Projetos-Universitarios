package iV_Estoque;

import java.util.ArrayList;
import java.util.Date;
public class Produto {
    private int cod;
    private String desc;
    private double compra;
    private double venda;
    private double lucro;
    private int quant;
    private int min;
    private ArrayList<Fornecedor> listaF = new ArrayList<Fornecedor>();
    private ArrayList<Ocorrencia> extrato = new ArrayList<Ocorrencia>();

    //Método construtor
    public Produto(int cod, String desc, int min, double lucro) {
        this.cod = cod;
        this.desc = desc;
        this.min = min;
        this.lucro = lucro;
    }

    //Métodos Getters
    public int getCod() {
        return this.cod;
    }
    public String getDesc() {
        return this.desc;
    }
    public double getCompra() {
        return this.compra;
    }
    public double getVenda() {
        return this.venda;
    }
    public double getLucro() {
        return this.lucro;
    }
    public int getQuant() {
        return this.quant;
    }
    public int getMin() {
        return this.min;
    }
    public ArrayList<Fornecedor> getListaf() {
        return listaF;
    }

    public void compra(int quant, double val) {
        if(quant > 0) {
            if(val > 0) {
                this.compra = ((this.compra * this.quant) + (val * quant)) / (this.quant + quant);
                this.quant += quant;
                this.venda = this.compra + (this.compra * lucro);
                Ocorrencia o = new Ocorrencia(new Date(), "COMPRA", String.valueOf(quant), String.valueOf(val), String.valueOf(this.quant), quant*val);
                extrato.add(o);
            } else {
                System.out.println("Preço inválido.");
            }
        } else {
            System.out.println("Quantidade inválida.");
        }
    }

    public double venda(int quant) {
        if(this.quant >= quant) {
            if(quant > 0) {
                this.quant -= quant;
                Ocorrencia o = new Ocorrencia(new Date(), "VENDA", String.valueOf(quant), String.valueOf(this.venda), String.valueOf(this.quant), (this.venda*quant));
                extrato.add(o);
                return quant * venda;
            } else {
                System.out.println("Quantidade inválida.");
                return -1;
            }
        } else {
            System.out.print("Quantidade insuficiente.");
            return -1;
        }
    }

    public int pesquisarFornecedor(int cnpj) {
        for(int i = 0; i < listaF.size(); i++) {
            if(listaF.get(i).getCnpj() == cnpj) {
                return i;
            }
        }
        return -1;
    }

    public void incluirF(Fornecedor f) {
        int pos = pesquisarFornecedor(f.getCnpj());
        if(pos == -1) {
            listaF.add(f);
            f.incluirProduto(this);
        } else {
            System.out.println("Fornecedor já existente para esse produto.");
        }
    }

    public boolean suficiente() {
        return this.quant >= this.min;
    }

    public String movimentos(Date ini, Date fim) {
        String resp = "";
        String ans = "Extrato completo do produto " + String.valueOf(this.cod) + " no período requisitado: \n \n";
        Ocorrencia last = null;
        for(int i = 0; i < extrato.size(); i++) {
            Ocorrencia o = extrato.get(i);
            if(!(o.getData().before(ini)) & !(o.getData().after(fim)) ) {
                resp = resp + o.getTipo() + ": " + o.getQuant() + " unidades à " + o.getValor() + " reais cada unidade. Total de " + String.valueOf(o.getTotal()) + " reais.\n";
                last = o;
            }
        }
        if(resp == "") {
            return resp;
        }
        if(last != null) {
            resp = resp + "Estoque de " + last.getQAtual() + " unidades disponíveis ao fim do período.";
        }
        return ans + resp;
    }

}
