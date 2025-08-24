package iV_Banco;

public class Conta {

	private int numero;
	private double saldo;
	private String extrato = "";
	private Pessoa dono;
	
	/*Construtor*/
	public Conta(int n) {
		this.numero = n;
	}
	
	/*Getters*/
	public int getNumero() {
		return numero;
	}
	
	public double getSaldo() {
		return saldo;
	}
	
	public String getExtrato() {
		return extrato;
	}

	public Pessoa getDono() {
		return dono;
	}
	
	/*Setters*/
	public void setDono(Pessoa dono) {
		this.dono = dono;
	}
	
	/*Outros métodos*/
	public void credito(double valor) {
		saldo = saldo + valor;
		extrato = extrato + "Conta: " + numero + ". Credito: " + valor + ". Saldo: "  + saldo + ".\n";
	}
	
	public void debito(double valor) {
		saldo = saldo - valor;
		extrato = extrato + "Conta: " + numero + ". Debito: " + valor + ". Saldo: "  + saldo + ".\n";
	}

	public boolean validar() {
		if (numero > 0) {
			return true;
		}
		return false;
	}
	
}
