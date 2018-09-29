package br.com.academiadev;

/*************************************************************************
 *  2) Faça um programa que:
 *    - Leia a cotação do dólar
 *    - Leia um valor em dólares
 *    - Converta esse valor para Real
 *    - Mostre o resultado
 *
 *************************************************************************/
import java.util.Scanner;

public class ConversorDolarReal {
	

	public void conversorDolarReal() {
		Scanner entrada = new Scanner(System.in);
		double cotacao_dolar, valor_dolar, valor_real;

		System.out.print("Conversor de dólar em real\n\n");

		System.out.print("Digite a cotação do dolar: ");
		cotacao_dolar = entrada.nextDouble();

		System.out.print("Digite o valor em dolar: ");
		valor_dolar = entrada.nextDouble();

		valor_real = conversorDolarReal(valor_dolar, cotacao_dolar);

		System.out.print("O Valor em reais é " + valor_real + "\n");

	}
	
	public double conversorDolarReal(double valorDolar, double cotacaoDolar) {
		return (valorDolar*cotacaoDolar);
	}

}
