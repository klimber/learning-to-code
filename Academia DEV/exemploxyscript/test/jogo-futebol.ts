import { JogoDeFutebol } from "../src/jogo-futebol";
import { expect } from "chai";
import { Time } from "../src/time";


describe("Inclusão de Jogador", () => {
    const jogo = new JogoDeFutebol();

    it("Adicionar jogador com sucesso", () => {
        let timeAtual = jogo.incluirTime(1, "Real Madrid", new Date(2017, 1, 1), "Branco", "Preto", []);

        let timeExpected: Time = {
            id: 1,
            nome: "Real Madrid",
            dataCriacao: new Date(2017, 1, 1),
            corUniformePrincipal: "Branco",
            corUniformeSecundario: "Preto"
        }
    })
})