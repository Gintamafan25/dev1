import { Inject, Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpResponse, HttpHeaders, HttpInterceptor, HttpHandler, HttpEvent, HttpRequest } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Fighters, User, Register, Response } from '../../assets/Fighters';
import { map, catchError, tap } from 'rxjs/operators';
import { error } from 'console';
import { DOCUMENT } from '@angular/common';




@Injectable({
  providedIn: 'root'
})
export class DjangoApiService {
  private url = "http://localhost:8000";
  private user_url= "http://localhost:8000/user"
  private register_url = "http://localhost:8000/register"
  private csrf_url = "http://localhost:8000/csrf"
  token! : string;
  cookies!: string

  constructor(private http: HttpClient) {}

  getFighters(): Observable<any> {
    
    return this.http.get<any[]>(this.url, this.httpOptions)
      .pipe(
        catchError(this.handleError)
      );
  }
  
    
  

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error("An error occured:", error.error.message);
    } 
    return throwError( () => new Error('bad'));
  }

  private httpOptions = {
     headers : new HttpHeaders({
      'content-type': 'application/json'
    }),
    withCredentials:true,
    observe: 'response' as 'response'
      
  }
  

  public submitRegistration(data: string) {
    
    return this.http.post<any>(this.register_url, data, this.httpOptions ).pipe(
      catchError(this.handleError)
    )
  }

  public getToken(): Observable<any> {
    return this.http.get<any>(this.csrf_url, this.httpOptions)
  }

  public saveToken(info: string) {
    this.token = info
  }

  public showToken() {
    return this.token
  }

  @Inject(DOCUMENT)
  set document(doc: Document) {
    this.cookies = doc.cookie
    console.log(this.cookies)
  }
  
}

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  constructor(private service: DjangoApiService) {}
  intercept(req:HttpRequest<any>, handler: HttpHandler): Observable<HttpEvent<any>> {
  
    if (req.method === "POST") {
      let token = this.service.showToken();
      console.log(token)
      let cloneReq = req.clone({
        headers: req.headers
        .set('Authorization', `bearer ${token}`)
      });
      
      console.log(cloneReq.headers)
      console.log(cloneReq.headers.keys())
      return handler.handle(cloneReq).pipe(
        catchError(error => {
          console.error(error);
          return throwError( () => new error)
        })
      )
    }
    return handler.handle(req)
  }
}