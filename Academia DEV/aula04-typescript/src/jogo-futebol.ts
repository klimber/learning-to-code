import { Time } from './time';

export class JogoDeFutebol {

    times: Array<Time> = [];

    incluirTime(id: Number, nome: String, dataCriacao: Date, corUniformePrincipal: String, corUniformeSecundario: String): Time {
        const time = {
            id: id,
            nome: nome,
            dataCriacao: dataCriacao,
            corUniformePrincipal: corUniformePrincipal,
            corUniformeSecundario: corUniformeSecundario
        };

        this.times.push(time);
        return time;
    }
}
