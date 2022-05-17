import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-app-registration',
  templateUrl: './app-registration.component.html',
  styleUrls: ['./app-registration.component.css']
})
export class AppRegistrationComponent implements OnInit {

  @ViewChild("container")
  container!: ElementRef;
  
  form!: FormGroup;
  loading = false;
  submitted = false;

  constructor(
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
  ) { }

  ngOnInit() {
      this.form = this.formBuilder.group({
        firstName: ['', Validators.required],
          lastname: ['', Validators.required],
          dob: ['', Validators.required],
          email: ['', Validators.required],
          password: ['', [Validators.required, Validators.minLength(6)]],
          confirmpassword: ['', [Validators.required, Validators.minLength(6)]]
      });
  }

  signup(){
    console.log(this.form);
  }

  signupchange(){
    console.log(this.form);
    // //const container = document.getElementById('container');
    this.container.nativeElement.classList.add('right-panel-active');
  }

  signinchange(){
    // const container = document.getElementById('container');
    this.container.nativeElement.classList.remove('right-panel-active');
  }

}
