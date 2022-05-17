import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-app-registration',
  templateUrl: './app-registration.component.html',
  styleUrls: ['./app-registration.component.css']
})
export class AppRegistrationComponent implements OnInit {

  @ViewChild("container")
  container!: ElementRef;
  
  signupform!: FormGroup;
  signinform!: FormGroup;
  loading = false;
  submitted = false;

  constructor(
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
      private http: HttpClient
  ) { }

  ngOnInit() {
      this.signupform = this.formBuilder.group({
        firstName: this.formBuilder.control('', Validators.required),
        lastname: this.formBuilder.control('', Validators.required),
        dob: this.formBuilder.control('', Validators.required),
        email: this.formBuilder.control('', Validators.required),
        password: this.formBuilder.control('', [Validators.required, Validators.minLength(6)]),
        confirmpassword: this.formBuilder.control('',  [Validators.required, Validators.minLength(6)]),
    });
    this.signinform = this.formBuilder.group({
        email: this.formBuilder.control('', Validators.required),
        password: this.formBuilder.control('', [Validators.required, Validators.minLength(6)]),
    })
  }

  signup(){
    this.http.post<any>('https://reqres.in/api/posts', { data: this.signupform.value }).subscribe(data => {
      console.log(data)
    })
    console.log(this.signupform.value);
  }

  signupchange(){
    console.log(this.signupform);
    // //const container = document.getElementById('container');
    this.container.nativeElement.classList.add('right-panel-active');
  }

  signinchange(){
    // const container = document.getElementById('container');
    this.container.nativeElement.classList.remove('right-panel-active');
  }

}
