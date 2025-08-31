package iV_Estoque;

import java.util.Date;
public class Ocorrencia {
    private Date data = new Date();
    private String tipo = new String();
    private String quant = new String();
    private String valor = new String();
    private String qAtual = new String();
    private double total = 0;

    public Ocorrencia(Date data, String tipo, String quant, String valor, String qAtual, double total) {
        this.data = data;
        this.tipo = tipo;
        this.quant = quant;
        this.valor = valor;
        this.qAtual = qAtual;
        this.total = total;
    }

    //Métodos Getters
    public Date getData() {
        return this.data;
    }
    public String getTipo() {
        return this.tipo;
    }
    public String getQuant() {
        return this.quant;
    }
    public String getValor() {
        return this.valor;
    }
    public String getQAtual() {
        return this.qAtual;
    }
    public double getTotal() {
        return this.total;
    }
}
