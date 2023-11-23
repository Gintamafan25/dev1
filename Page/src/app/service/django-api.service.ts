import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Fighters, User, Register, Response } from '../../assets/Fighters';
import { map, catchError } from 'rxjs/operators';
import { error } from 'console';
import { HttpXsrfTokenExtractor } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class DjangoApiService {
  private url = "http://localhost:8000";
  private user_url= "http://localhost:8000/user"
  private register_url = "http://localhost:8000/register"

  constructor(private http: HttpClient, private xtractor: HttpXsrfTokenExtractor) { }

  getFighters(): Observable<Fighters[]> {
    const headers = new HttpHeaders({});
    const xsrfToken = this.xtractor.getToken();
    if (xsrfToken) {
      headers.append('X-XSRF-Token', xsrfToken);
    }
    return this.http.get<any[]>(this.url, { headers })
      .pipe(
        catchError(this.handleError)
      );
  }
  
    
  

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error("An error occured:", error.error.message);
    } else {
      console.error(error.status);
      console.log(error.message)
      console.log(error.headers)
      console.log(error.url)
      console.log(error.name)
    }
    return throwError( () => new Error('bad'));
  }

  public submitRegistration(data: Register) {
    const headers = new HttpHeaders({
      "content-type": "application/json"
    });
    
    return this.http.post<Response>(this.register_url, data, { headers }).pipe(
      catchError(this.handleError)
    )
  }
  
}