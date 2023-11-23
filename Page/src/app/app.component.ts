import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { HttpClientModule } from '@angular/common/http';
import { DjangoApiService } from './service/django-api.service';
import { Fighters, Register, CookieMap, Response } from '../assets/Fighters';
import { FormComponent } from './form/form.component';
import { HttpClientXsrfModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderComponent, HttpClientModule, FormComponent, HttpClientXsrfModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [DjangoApiService]
})
export class AppComponent implements OnInit {
  
  fighters$: Fighters[] = []

  constructor(private data: DjangoApiService) { }

  ngOnInit() {
    this.showFighters();

  }

  showFighters() {
    this.data.getFighters().subscribe({
      next: (response) => {
        console.log(JSON.stringify(response))
        this.fighters$ = response;
        
        
      },
      error: (error) => {
        console.error(error);
      }
    })
    
      
  }
  

}
