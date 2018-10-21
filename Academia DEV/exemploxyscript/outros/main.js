console.log("Hello World");

const listaTimes = [];

function incluirTime(id, nome, dataCriacao, corUniformePrincipal, corUniformeSecundario) {

    listaTimes.push({
        id: id,
        nome: nome,
        dataCriacao: dataCriacao,
        corUniformePrincipal: corUniformePrincipal,
        corUniformeSecundario: corUniformeSecundario,
        jogadores: []
    });
}

function incluirJogador(id, idTime, nome, dataNascimento, nivelHabilidade, salario) {
    let time = buscarTimesPorId(idTime);

    let jogador = {
        id: id,
        idTime: time.id,
        nome: nome,
        dataNascimento: dataNascimento,
        nivelHabilidade: nivelHabilidade,
        salario: salario
    }

    time.jogadores.push(jogador);
}

function buscarTimesPorId(idTime) {
    return listaTimes.filter(t => t.id == idTime)[0];
}

function buscarJogadorMaiorSalario() {
    return buscarJogadores().sort(porSalarioEId());
}

function buscarJogadores() {
    return listaTimes.reduce((previous, current) => {
        return previous.concat(current.jogadores);
    }, []);
}   

function porSalarioEId() {
    return (j1, j2) => {
        if(j1.salario > j2.salario){
            return -1;
        }
        if(j1.salario < j2.salario){
            return 1;
        }
        if(j1.id > j2.id){
            return 1;
        }
        else return 0;
    };
}

incluirTime(1, "Real Madrid", Date(2017, 1, 1), "Branco", "Preto");
incluirTime(2, "Fluminense", Date(2015, 1, 1), "Vermelho", "Verde");
incluirJogador(1001, 1, "Allan1", Date(1993, 03, 24), 18, 50000);
incluirJogador(1003, 1, "Allan2", Date(1993, 03, 24), 18, 25000);
incluirJogador(1002, 1, "Allan3", Date(1993, 03, 24), 18, 25000);