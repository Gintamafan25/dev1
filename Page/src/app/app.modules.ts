// Import necessary Angular modules
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule for HTTP requests

// Import your components and services
import { AppComponent } from './app.component'; 
import { DjangoApiService } from './django-api.service'; // Example service import

@NgModule({
  
  imports: [
    AppComponent,
    BrowserModule,
    HttpClientModule, 
  ],
  providers: [
    
    DjangoApiService, 
    
  ],
  bootstrap: [],
})
export class AppModule {}
