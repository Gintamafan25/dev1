import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class DjangoApiService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  public get(endpoint: string): Observable<any> {
    const url = `${this.apiUrl}/${endpoint}`;
    return this.http.get(url);
  
}

}
