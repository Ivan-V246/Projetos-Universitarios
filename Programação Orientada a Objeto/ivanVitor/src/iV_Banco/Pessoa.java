package iV_Banco;

public class Pessoa {
	
	private int cpf;
	private String nome;
	private Conta conta;
	private String senha;
	
	/*Construtor*/
	public Pessoa (int cpf, String nome, String senha) {
		this.cpf = cpf;
		this.nome = nome;
		this.senha = senha;
	}
	
	/*Getters*/
	public int getCpf() {
		return cpf;
	}
	
	public String getNome() {
		return nome;
	}
	
	public Conta getConta() {
		return conta;
	}
	
	public String getSenha() {
		return senha;
	}
	
	/*Setters*/
	public void setCpf(int cpf) {
		this.cpf = cpf;
	}
	
	public void setNome(String nm) {
		this.nome = nm;
	}
	
	public void setConta(Conta c) {
		this.conta = c;
	}
	
	public void setSenha(String pass) {
		this.senha = pass;
	}
	
	/*Outros métodos*/
	public boolean validar() {
		if (cpf > 0 && nome != null && nome.length() > 0) {
			return true;
		}
		return false;
	}
}
