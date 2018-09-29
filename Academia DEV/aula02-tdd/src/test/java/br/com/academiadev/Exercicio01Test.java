package br.com.academiadev;

import org.junit.Assert;
import org.junit.Test;

public class Exercicio01Test {

	@Test
	public void calculaEstoqueMinimoTest() {
		double estoqueMedio = new Exercicio01().calculaEstoqueMedio(10, 20);

		Assert.assertEquals(15, estoqueMedio, 0);
	}

	@SuppressWarnings("deprecation")
	@Test
	public void calculaEstoqueMinimoTest2() {
		double estoqueMedio = new Exercicio01().calculaEstoqueMedio(5, 70);

		Assert.assertEquals(37.5, estoqueMedio, 0);
	}

}
