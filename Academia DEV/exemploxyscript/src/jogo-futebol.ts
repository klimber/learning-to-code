import { Time } from "./time";
import { Jogador } from "./jogador";


// let numero: Number = 12345;
// let letras: String = "Olá";
// let data: Date = new Date(2017,1,1);
// let lista: Array<String> = [];

export class JogoDeFutebol {
    times: Array<Time> = [];

    incluirTime(id: Number, nome: String, dataCriacao: Date, corUniformePrincipal: String, corUniformeSecundario: String, jogadores: Array<Jogador>) {
        const time = {
            id: id,
            nome: nome,
            dataCriacao: dataCriacao,
            corUniformePrincipal: corUniformePrincipal,
            corUniformeSecundario: corUniformeSecundario,
            jogadores: jogadores
        }
    }
}