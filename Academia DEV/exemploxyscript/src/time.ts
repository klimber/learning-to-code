import { Jogador } from "./jogador";

export interface Time {
    id: Number;
    nome: String;
    dataCriacao: Date;
    corUniformePrincipal: String;
    corUniformeSecundario: String;
    jogadores: Array<Jogador>;
}