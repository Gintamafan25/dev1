import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Fighters } from '../../assets/Fighters';
import { map, catchError } from 'rxjs/operators';
import { error } from 'console';

@Injectable({
  providedIn: 'root'
})
export class DjangoApiService {
  private url = "http://localhost:8000";
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
    return throwError('bad');
  }
}