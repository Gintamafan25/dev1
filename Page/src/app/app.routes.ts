import { Routes } from '@angular/router';
import { FormComponent } from './form/form.component'
import { AppComponent } from './app.component'

export const routes: Routes = [
    {path: "", title: "Home Page", component:AppComponent},
    {path: "register", title:"register", component:FormComponent}

];
