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
  isDivVisible = false;

  constructor(
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
      private http: HttpClient
  ) { }

  ngOnInit() {
    this.isDivVisible = false;
      this.signupform = this.formBuilder.group({
        first_name: this.formBuilder.control('', Validators.required),
        last_name: this.formBuilder.control('', Validators.required),
        // dob: this.formBuilder.control('', Validators.required),
        email: this.formBuilder.control('', Validators.required),
        password: this.formBuilder.control('', [Validators.required, Validators.minLength(6)]),
        otp_code: this.formBuilder.control('', Validators.required),
        role: this.formBuilder.control('USER',  [Validators.required, Validators.minLength(6)]),
    });
    this.signinform = this.formBuilder.group({
        email: this.formBuilder.control('', Validators.required),
        password: this.formBuilder.control('', [Validators.required, Validators.minLength(6)]),
    })
  }

  signup(){
    console.log(JSON.stringify({'email':this.signupform.value.email,
    'password':this.signupform.value.password,
    'otp_code':this.signupform.value.otp_code}))
    const headers = { 'Content-Type': 'application/json' };
    this.http.post<any>("http://127.0.0.1:5000/api/users/register", JSON.stringify({'email':this.signupform.value.email,
    'password':this.signupform.value.password,
    'otp_code':this.signupform.value.otp_code})
    ,{ headers }).subscribe(data => {
    this.signupform.reset() 
    this.signinchange()
    },
    error => {
      alert("This Account is already registerd")
    this.signupform.reset() 
  }
    )
    console.log(this.signupform.value);
  }

  verify(){
    alert("Verify")
    // remove password
    this.signupform;
    console.log(JSON.stringify({'email':this.signupform.value.email,
                                'first_name':this.signupform.value.first_name,
                                'last_name':this.signupform.value.last_name,
                                "role": "USER"}))
    const headers = { 'Content-Type': 'application/json' };
    this.http.post<any>("http://127.0.0.1:5000/api/users", JSON.stringify({'email':this.signupform.value.email,
    'first_name':this.signupform.value.first_name,
    'last_name':this.signupform.value.last_name,
    "role": "USER"}),{ headers }).subscribe(data => {
      // unhide password
      this.isDivVisible = true;

    // this.signupform.reset() 
    // this.signinchange()

    },
    error => {alert("This Account is already registerd")
    // this.signupform.reset() 
  }
    )
    // console.log(this.signupform.value);
  }

  signin(){
    const headers = { 'Content-Type': 'application/json' };
    this.http.post<any>("http://127.0.0.1:5000/api/users/login", JSON.stringify(this.signinform.value),{ headers }).subscribe(data => {
     // alert("Succesfully login")
     localStorage.setItem("userData",JSON.stringify(data))
     localStorage.setItem("firstName",data.first_name)
     localStorage.setItem("ID",data.id)
      this.router.navigate(['/trending']); 
    },
    error =>{ alert("Incorrect Credentials"),
    this.signinform.reset() }
    )
  }

  signupchange(){
    this.container.nativeElement.classList.add('right-panel-active');
  }

  signinchange(){
    this.container.nativeElement.classList.remove('right-panel-active');
  }

}
