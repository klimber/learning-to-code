package br.com.neogrid;

import br.com.neogrid.desafio.app.QuemSouEuInterface;

public class QuemSouEu implements QuemSouEuInterface {

	@Override
	public String getNome() {
		return "Alan && Bruno";
	}

	@Override
	public String getEmail() {
		return "klimber.mail@gmail.com && bm.morais21@gmail.com";
	}

	@Override
	public String getCelular() {
		return "0";
	}

	@Override
	public String getCurso() {
		return "Academia Dev";
	}

}
