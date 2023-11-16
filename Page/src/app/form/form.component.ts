import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormGroup, ReactiveFormsModule, FormControl, Validators } from '@angular/forms';
import { Register, CookieMap, Response } from '../../assets/Fighters';
import { DjangoApiService } from '../service/django-api.service';


@Component({
  selector: 'app-form',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './form.component.html',
  styleUrl: './form.component.scss'
})
export class FormComponent {

  registerForm = new FormGroup({
    username: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required),
    password: new  FormControl('', Validators.required),
    confirm_password: new FormControl('', Validators.required)
  })

  constructor(private data: DjangoApiService ) {}

  submitRegister(formData: Register) {
    this.data.registerUser(formData).subscribe(response => {
      const res = response as Response
      const message = res.message
      if (message === "Success") {
        const token = this.getCookie('session_token')

      }
    })
  }

  getCookie(name: string) {

    const cookies: CookieMap = {}
  
    document.cookie.split(';').forEach(function(el) {
  
      let [key,value] = el.split('=');
  
      cookies[key.trim()] = value;
  
    })
  
    return cookies[name];
  
  }


}


