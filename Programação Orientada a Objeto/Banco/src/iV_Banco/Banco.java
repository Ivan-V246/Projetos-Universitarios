package iV_Banco;

public class Banco {

	private Conta[] contas = new Conta[50];
	private int posContas = 0;
	private Pessoa[] pessoas = new Pessoa[50];
	private int posPessoas = 0;
	
	/*Pesquisas*/
	private Pessoa pesquisarPessoa(int cpf) {
		for (int i = 0; i < posPessoas; i++) {
			if (pessoas[i].getCpf() == cpf) {
				return pessoas[i];
			}
		}
		return null;
	}
	
	private Conta pesquisarConta(int num) {
		for (int i = 0; i < posContas; i++) {
			if (contas[i].getNumero() == num) {
				return contas[i];
			}
		}
		return null;
	}
	
	/*Cadastros*/
	public boolean cadastrarPessoa(Pessoa p) {
		if (p.validar() && pesquisarPessoa(p.getCpf()) == null) {
			pessoas[posPessoas++] = p;
			return true;
		} else {
			System.out.println("Pessoa inválida ou já cadastrada.");
			return false;
		}
	}
	
	
	public boolean cadastrarConta(Conta c, int cpf) {
		Pessoa p = pesquisarPessoa(cpf);
		if (c.validar() && p != null && pesquisarConta(c.getNumero()) == null) {
			if(p.getConta() != null) {
				System.out.println("Usuário já possui uma conta cadastrada.");
				return false;
			}
			contas[posContas++] = c;
			c.setDono(p);
			p.setConta(c);
			return true;
		} else {
			System.out.println("Conta inválida ou já cadastrada.");
			return false;
		}
	}
	
	/*Operações bancárias*/
	public double saldo(int num, String passwd) {
		Conta c = pesquisarConta(num);
		if (c != null) {
			if (c.getDono().getSenha().equals(passwd)) {
				return c.getSaldo();
			}
		}
		return -9999999;
	}
	
	public void deposito(int num, double v) {
		Conta c = pesquisarConta(num);
		if (c != null && v > 0) {
			c.credito(v);
		} else {
			System.out.println("Conta destino inexistente ou valor inválido.");
		}
	}
	
	public void saque(int num, double v, String passwd) {
		Conta c = pesquisarConta(num);
		if(c != null) {
			if(c.getDono().getSenha().equals(passwd)) {
				if(c.getSaldo() >= v) {
					c.debito(v);
				} else {
					System.out.println("Saldo insuficiente.");
				}
			} else {
				System.out.println("Senha incorreta.");
			}
		} else {
			System.out.println("Conta inexistente.");
		}
	}
	
	public String extrato(int num, String passwd) {
		Conta c = pesquisarConta(num);
		if(c!= null) {
			if(c.getDono().getSenha().equals(passwd)) {
				return c.getExtrato();
			} else {
				System.out.print("Senha incorreta!");
			}
		} else {
			System.out.println("Conta inexistente.");
		}
		return "Extrato não disponível.";
	}
	
	public void transfere(int n1, String pass, int n2, double v) {
		Conta c1 = pesquisarConta(n1);
		Conta c2 = pesquisarConta(n2);
		if(c1 == null || c2 == null || v < 0) {
			System.out.println("Contas inexistentes ou valor inválido.");
		} else {
			if(c1.getDono().getSenha().equals(pass)) {
				if(c1.getSaldo() >= v) {
					c1.debito(v);
					c2.credito(v);
					System.out.println("Operação concluída com sucesso.");
				} else {
					System.out.println("Saldo da conta origem insuficiente.");
				}
			} else {
				System.out.println("Senha incorreta.");
			}
		}
	}
}
