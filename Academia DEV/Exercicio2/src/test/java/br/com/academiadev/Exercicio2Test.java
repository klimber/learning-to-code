package br.com.academiadev;

import org.junit.Assert;
import org.junit.Test;

public class Exercicio2Test {

	@Test
	public void calculaValorRealTest() {
		double valorReal = new ConversorDolarReal().conversorDolarReal(50, 4);

		Assert.assertEquals(200, valorReal, 0);
	}

	@Test
	public void calculaValorRealTest2() {
		double valorReal = new ConversorDolarReal().conversorDolarReal(20, 5);

		Assert.assertEquals(100, valorReal, 0);
	}

}
