import { Component, OnInit, inject} from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { HttpClientModule } from '@angular/common/http';
import { DjangoApiService } from './service/django-api.service';
import { Fighters, Register, CookieMap, Response } from '../assets/Fighters';
import { FormComponent } from './form/form.component';
import { HttpClientXsrfModule } from '@angular/common/http';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderComponent, HttpClientModule, FormComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  
  fighters$: Fighters[] = []
  token!: string

  constructor(private data: DjangoApiService) { }

  ngOnInit() {
    this.showFighters();
    this.setToken()
    this.data.saveToken(this.token)
    console.log(this.token)

  }

  showFighters() {
    this.data.getFighters().subscribe({
      next: (response) => {
        this.fighters$ = response;
        console.log(this.fighters$)
      },
      error: (error) => {
        console.error(error);
      }
    })
  }
  setToken() {
    return this.data.getToken().subscribe(response => {
      this.token = response.customToken
      
      
    })
  
  }
}
