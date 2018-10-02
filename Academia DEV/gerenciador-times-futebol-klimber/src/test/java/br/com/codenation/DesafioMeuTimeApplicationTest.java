package br.com.codenation;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.time.LocalDate;

import org.junit.Assert;
import org.junit.Test;

import br.com.codenation.desafio.exceptions.*;

public class DesafioMeuTimeApplicationTest {

	@Test
	public void testeIncluirTime() {
		DesafioMeuTimeApplication teste = new DesafioMeuTimeApplication();

		teste.incluirTime(1l, "Real Madrid", LocalDate.of(2016, 1, 1), "Branco", "Azul");

		try {
			teste.incluirTime(1l, "Real Madrid", LocalDate.of(2016, 1, 1), "Branco", "Azul");
			Assert.assertTrue("Deveria dar exceção", false);
		} catch (Exception e) {
			if (e.getCause() instanceof IdentificadorUtilizadoException) {
				Assert.assertTrue(false);
			}
		}
	}

	@Test
	public void testeIncluirJogador() {
		DesafioMeuTimeApplication teste = new DesafioMeuTimeApplication();
		
		try {
			teste.incluirJogador(1L, 1L, "Allan Krueger", LocalDate.of(1993, 03, 24), 3, BigDecimal.valueOf(2000));
			Assert.assertTrue("Deveria dar exceção de time não encontrado", false);
		} catch (TimeNaoEncontradoException e) {
			if (e.getCause() instanceof TimeNaoEncontradoException) {
				Assert.assertTrue(false);
			}
		}
		teste.incluirTime(1l, "Real Madrid", LocalDate.of(2016, 1, 1), "Branco", "Azul");
		teste.incluirJogador(1L, 1L, "Allan Krueger", LocalDate.of(1993, 03, 24), 3, BigDecimal.valueOf(2000));
		
		try {
			teste.incluirJogador(1L, 1L, "Allan Krueger", LocalDate.of(1993, 03, 24), 3, BigDecimal.valueOf(2000));
			Assert.assertTrue("Deveria dar exceção de identificador existente", false);
		} catch (Exception e) {
			if (e.getCause() instanceof IdentificadorUtilizadoException) {
				Assert.assertTrue(false);
			}
		}

	}

}
