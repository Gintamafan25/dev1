import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormGroup, ReactiveFormsModule, FormControl, Validators } from '@angular/forms';
import { Register, CookieMap, Response } from '../../assets/Fighters';
import { DjangoApiService } from '../service/django-api.service';
import { Observable } from 'rxjs';


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

  

  submitRegister() {
    
    const formValue = this.registerForm.value;
    const info = JSON.stringify(formValue)

    return this.data.submitRegistration(info).subscribe(
      res => {
        console.log(res)
      }
    )
  }
  
}


