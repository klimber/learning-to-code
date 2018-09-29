package br.com.academiadev;

import java.util.Scanner;

/*************************************************************************
 * 1-)Faça um programa para calcular o estoque médio de uma peça, sendo que:
 * ESTOQUE MÉDIO = (QUANTIDADE_MÍNIMA + QUANTIDADE_MÁXIMA) / 2.
 *
 *************************************************************************/
public class Exercicio01 {

	public void calculaEstoqueMedio() {
		Scanner entrada = new Scanner(System.in);

		double quantidade_minima, quantidade_maxima, estoque_medio;

		System.out.print("Calculadora de Estoque Médio\n\n");

		System.out.print("Digite a quantidade mímima:");
		quantidade_minima = entrada.nextDouble();

		System.out.print("Digite a quantidade máxima:");
		quantidade_maxima = entrada.nextDouble();

		estoque_medio = calculaEstoqueMedio(quantidade_minima, quantidade_maxima);
		System.out.print("Estoque Médio = " + estoque_medio + "\n");

		calculaEstoqueMedio(0, 0);
	}

	public double calculaEstoqueMedio(double quantidadeMinima, double quantidadeMaxima) {
		return (quantidadeMinima + quantidadeMaxima) / 2 ;
	}

}
