import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Fighters, User, Register } from '../../assets/Fighters';
import { map, catchError } from 'rxjs/operators';
import { error } from 'console';

@Injectable({
  providedIn: 'root'
})
export class DjangoApiService {
  private url = "http://localhost:8000";
  private user_url= "http://localhost:8000/user"
  private register_url = "http://localhost:8000/register"

  constructor(private http: HttpClient) { }

  public getFighters(): Observable<Fighters[]> {
    return this.http.get<Fighters[]>(this.url).pipe(
      catchError(this.handleError)
    );
  }


  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error("An error occured:", error.error.message);
    } else {
      console.error(error.status);
    }
    return throwError( () => new Error('bad'));
  }

  public getUser(): Observable<User[]> {
    return this.http.get<User[]>(this.user_url, {withCredentials: true})
  }

  public registerUser(userData: Register) {
    return this.http.post(this.register_url, userData).pipe(
      catchError(this.handleError)
    );
  }

}