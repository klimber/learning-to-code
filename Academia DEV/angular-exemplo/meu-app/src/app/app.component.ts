import { Component, OnInit } from '@angular/core';
import { TimeService } from './time.service';
import { FormGroup } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  title = 'meu-app';

  nocoTimeForm = new FormGroup(null);

  public times: Array<Time> = [];

  constructor(
    private timeService: TimeService
  ) { }
  ngOnInit(): void {
    this.timeService.buscarTime().subscribe(res => {
      this.times = <Array<Time>>res;
      console.log(this.times);
    });

    this.timeService.incluirTime({
      id: 2,
      nome: 'Real Madrid',
      dataCriacao: new Date(2015, 5, 8),
      corUniformePrincipal: 'Branco',
      corUniformeSecundario: 'Preto'
    });
  }
}

