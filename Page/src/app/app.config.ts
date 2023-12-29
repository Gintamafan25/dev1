import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';
import { provideHttpClient, withFetch, HttpClientXsrfModule, withInterceptorsFromDi, HTTP_INTERCEPTORS } from '@angular/common/http';
import { TokenInterceptor } from './service/django-api.service';
import { Token } from '@angular/compiler';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), provideClientHydration(), provideHttpClient(withFetch(),withInterceptorsFromDi()), 
    {provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true}]
};
