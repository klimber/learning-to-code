package br.com.codenation;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.TreeMap;


import br.com.codenation.desafio.annotation.Desafio;
import br.com.codenation.desafio.app.MeuTimeInterface;
import br.com.codenation.desafio.exceptions.*;

public class DesafioMeuTimeApplication implements MeuTimeInterface {
	
	HashMap<Long, Time> listaTime = new HashMap<Long, Time>();
	HashMap<Long, Jogador> listaJogador = new HashMap<Long, Jogador>();

	@Desafio("incluirTime")
	public void incluirTime(Long id, String nome, LocalDate dataCriacao, String corUniformePrincipal, String corUniformeSecundario) {
		if(listaTime.containsKey(id)) {
			throw new IdentificadorUtilizadoException();
			
		} else {
			Time timeadd = new Time();
			timeadd.nome = nome;
			timeadd.dataCriacao = dataCriacao;
			timeadd.corUniformePrincipal = corUniformePrincipal;
			timeadd.corUniformeSecundario = corUniformeSecundario;
			listaTime.put(id,timeadd);	
		}
	}

	@Desafio("incluirJogador")
	public void incluirJogador(Long id, Long idTime, String nome, LocalDate dataNascimento, Integer nivelHabilidade, BigDecimal salario) {
		
		if(listaJogador.containsKey(id)) {
			throw new IdentificadorUtilizadoException();
		}
		
		if(listaTime.containsKey(idTime)==false) {
			throw new TimeNaoEncontradoException();
		}
		
		if(listaJogador.containsKey(id)==false && listaTime.containsKey(idTime)) {
			Jogador jogadoradd = new Jogador();
			jogadoradd.idTime = idTime;
			jogadoradd.nome = nome;
			jogadoradd.dataNascimento = dataNascimento;
			jogadoradd.nivelHabilidade = nivelHabilidade;
			jogadoradd.salario = salario;
			listaJogador.put(id, jogadoradd);
			
		}
	}

	@Desafio("definirCapitao")
	public void definirCapitao(Long idJogador) {
		
		if(listaJogador.containsKey(idJogador)) {
			Jogador jogadorcapitao = listaJogador.get(idJogador);
			
			for (Long id : listaJogador.keySet()) {
				Jogador outrojogador = listaJogador.get(id);
			
				if(outrojogador.idTime == jogadorcapitao.idTime) {
					outrojogador.capitao = false;
				}
			}
			jogadorcapitao.capitao = true;
		} else {
			throw new JogadorNaoEncontradoException();
		}
	}

	@Desafio("buscarCapitaoDoTime")
	public Long buscarCapitaoDoTime(Long idTime) {
		
		Long idCapitao = 0L;
		int contador = 0;
		
		if(listaTime.containsKey(idTime)==false) {
			throw new TimeNaoEncontradoException();
			
		} else {
			
			for(Long id : listaJogador.keySet()) {
				Jogador jogador = listaJogador.get(id);
				if(jogador.idTime==idTime) {
					if(jogador.capitao==true) {
						idCapitao = id;
						contador += 1;
					}
				}
			}
		}
		
		if(contador == 0) {
			throw new CapitaoNaoInformadoException();
			
		} else {
			return idCapitao;
		}
	}

	@Desafio("buscarNomeJogador")
	public String buscarNomeJogador(Long idJogador) {
		
		if(listaJogador.containsKey(idJogador)) {
			Jogador jogador = listaJogador.get(idJogador);
			return jogador.nome;
		} else {
			throw new JogadorNaoEncontradoException();
		}
	}

	@Desafio("buscarNomeTime")
	public String buscarNomeTime(Long idTime) {
		
		if(listaTime.containsKey(idTime)) {
			Time time = listaTime.get(idTime);
			return time.nome;
		} else {
			throw new TimeNaoEncontradoException();
		}
	}

	@Desafio("buscarJogadoresDoTime")
	public List<Long> buscarJogadoresDoTime(Long idTime) {
		
		ArrayList<Long> listaJogadores = new ArrayList<Long>();
		if(listaTime.containsKey(idTime)) {
			for(Long id : listaJogador.keySet()) {
				Jogador jogador = listaJogador.get(id);
				if(jogador.idTime == idTime) {
					listaJogadores.add(id);
				}
			}
			Collections.sort(listaJogadores);
			return listaJogadores;
			
		} else {
			throw new TimeNaoEncontradoException();
		}
	}

	@Desafio("buscarMelhorJogadorDoTime")
	public Long buscarMelhorJogadorDoTime(Long idTime) {
		
		Long idmelhorjogador = Long.MAX_VALUE;
		Integer habilidademax = 0;
		if(listaTime.containsKey(idTime)) {
			for(Long id : listaJogador.keySet()) {
				Jogador jogador = listaJogador.get(id);
				if(jogador.idTime == idTime) {
					if(jogador.nivelHabilidade > habilidademax) {
						habilidademax = jogador.nivelHabilidade;
						idmelhorjogador = id;
					} else if (jogador.nivelHabilidade == habilidademax) {
						if(id < idmelhorjogador) {
							idmelhorjogador = id;
						}
					}
					
				}
			}
			return idmelhorjogador;
		} else {
			throw new TimeNaoEncontradoException();
		}		
	}

	@Desafio("buscarJogadorMaisVelho")
	public Long buscarJogadorMaisVelho(Long idTime) {
		
		Long idmaisvelho = Long.MAX_VALUE;
		LocalDate data = LocalDate.now();
		if(listaTime.containsKey(idTime)) {
			for(Long id : listaJogador.keySet()) {
				Jogador jogador = listaJogador.get(id);
				if(jogador.idTime == idTime) {
					if(data.isAfter(jogador.dataNascimento)){
						data = jogador.dataNascimento;
						idmaisvelho = id;
					}else if (data.isEqual(jogador.dataNascimento)) {
						if(idmaisvelho > id) {
							idmaisvelho = id;
						}
					}
				}
			}
			return idmaisvelho;
		} else {
			throw new TimeNaoEncontradoException();
		}
	}

	@Desafio("buscarTimes")
	public List<Long> buscarTimes() {
		
		
		
		if(listaTime.isEmpty()) {
			return new ArrayList<Long>();
			
		} else {
			ArrayList<Long> listaTimes = new ArrayList<Long>(listaTime.keySet());
			Collections.sort(listaTimes);
			return listaTimes;
		}
	}

	@Desafio("buscarJogadorMaiorSalario")
	public Long buscarJogadorMaiorSalario(Long idTime) {
		
		Long idmaiorsalario = Long.MAX_VALUE;
		BigDecimal maiorsalario = BigDecimal.ZERO;
		if(listaTime.containsKey(idTime)) {
			for(Long id : listaJogador.keySet()) {
				Jogador jogador = listaJogador.get(id);
				if(jogador.salario.compareTo(maiorsalario) == 1) {
					maiorsalario = jogador.salario;
					idmaiorsalario = id;
					
				} else if(maiorsalario.equals(jogador.salario)) {
					if(id < idmaiorsalario) {
						idmaiorsalario = id;
					}
				}
			}
			return idmaiorsalario;
			
		} else {
			throw new TimeNaoEncontradoException();
		}
	}

	@Desafio("buscarSalarioDoJogador")
	public BigDecimal buscarSalarioDoJogador(Long idJogador) {
		
		if(listaJogador.containsKey(idJogador)) {
			Jogador jogador = listaJogador.get(idJogador);
			return jogador.salario;
			
		} else {
			throw new JogadorNaoEncontradoException();
		}
	}

	@Desafio("buscarTopJogadores")
	public List<Long> buscarTopJogadores(Integer top) {
		TreeMap<Integer, Long> listatop = new TreeMap<Integer, Long>();
		if(listaJogador.isEmpty()) {
			return new ArrayList<Long>();
		}else {
			for(Long id : listaJogador.keySet()) {
				listatop.put(listaJogador.get(id).nivelHabilidade, id);			
			}
			List<Long> arraytop = new ArrayList<Long>(listatop.values()).subList(0, top);
			Collections.reverse(arraytop);
			return arraytop;
		}
	}

	@Desafio("buscarCorCamisaTimeDeFora")
	public String buscarCorCamisaTimeDeFora(Long timeDaCasa, Long timeDeFora) {
		if(listaTime.containsKey(timeDaCasa) && listaTime.containsKey(timeDeFora)) {
			Time dacasa = listaTime.get(timeDaCasa);
			Time defora = listaTime.get(timeDeFora);
			if(dacasa.corUniformePrincipal == defora.corUniformePrincipal) {
				return defora.corUniformeSecundario;
			} else {
				return defora.corUniformePrincipal;
			}
		} else {
			throw new TimeNaoEncontradoException();
		}
	}

}
