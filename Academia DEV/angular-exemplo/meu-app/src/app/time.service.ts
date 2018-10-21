import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TimeService {

  constructor(
    private httpClient: HttpClient
  ) { }

  buscarTime(): Observable<Object> {
    return this.httpClient
      .get('https://desafio-time-futebol.herokuapp.com/api/time');
  }
  incluirTime(time: Time): Observable<Object> {
    return this.httpClient.post('https://desafio-time-futebol.herokuapp.com/api/time', time);
  }
}
