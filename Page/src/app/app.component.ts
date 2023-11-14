import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { HttpClientModule } from '@angular/common/http';
import { DjangoApiService } from './service/django-api.service';
import { Fighters } from '../assets/Fighters';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HeaderComponent, HttpClientModule],
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
        this.fighters$ = response;
        console.log(this.fighters$);
      },
      error: (error) => {
        console.error(error);
      }
    })
      
  }


}
