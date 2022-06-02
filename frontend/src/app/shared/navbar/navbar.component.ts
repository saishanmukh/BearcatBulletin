import { Component, OnInit, ElementRef } from '@angular/core';
import { ROUTES } from '../../sidebar/sidebar.component';
import { Location, LocationStrategy, PathLocationStrategy } from '@angular/common';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
    // moduleId: module.id,
    selector: 'navbar-cmp',
    templateUrl: 'navbar.component.html',
    styleUrls: ['./navbar.component.css']
})

export class NavbarComponent implements OnInit {
    displayPostModal = "none";
    private listTitles!: any[];
    location: Location;
    private toggleButton: any;
    private sidebarVisible: boolean;
    firstName = localStorage.getItem('firstName');
    ID = localStorage.getItem('ID');
    newpostForm!: FormGroup;
    public files: any[];
    imageData = new FormData();


    constructor(location: Location, private element: ElementRef, private formBuilder: FormBuilder, private http: HttpClient) {
        this.location = location;
        this.sidebarVisible = false;
        this.files = [];
    }

    ngOnInit() {
        this.listTitles = ROUTES.filter(listTitle => listTitle);
        const navbar: HTMLElement = this.element.nativeElement;
        this.toggleButton = navbar.getElementsByClassName('navbar-toggle')[0];

        this.newpostForm = this.formBuilder.group({
            headline: this.formBuilder.control('', Validators.required),
            headlineDesc: this.formBuilder.control('', Validators.required),
            category: this.formBuilder.control('', Validators.required),
        })
    }
    sidebarOpen() {
        const toggleButton = this.toggleButton;
        const body = document.getElementsByTagName('body')[0];
        setTimeout(function () {
            toggleButton.classList.add('toggled');
        }, 500);
        body.classList.add('nav-open');

        this.sidebarVisible = true;
    };
    sidebarClose() {
        const body = document.getElementsByTagName('body')[0];
        this.toggleButton.classList.remove('toggled');
        this.sidebarVisible = false;
        body.classList.remove('nav-open');
    };
    sidebarToggle() {
        // const toggleButton = this.toggleButton;
        // const body = document.getElementsByTagName('body')[0];
        if (this.sidebarVisible === false) {
            this.sidebarOpen();
        } else {
            this.sidebarClose();
        }
    };

    getTitle() {
        var titlee = this.location.prepareExternalUrl(this.location.path());
        if (titlee.charAt(0) === '#') {
            titlee = titlee.slice(1);
        }

        for (var item = 0; item < this.listTitles.length; item++) {
            if (this.listTitles[item].path === titlee) {
                return this.listTitles[item].title;
            }
        }
        return 'Dashboard';
    }

    menuToggle() {
        const toggleMenu = document.querySelector('.menu');
        toggleMenu?.classList.toggle('change')
    }
    openPopup() {
        this.displayPostModal = "block";
    }
    post() {
        if (this.newpostForm.valid) {
            this.imageData.set("headline", this.newpostForm.get('headline')?.value);
            this.imageData.set("description", this.newpostForm.get('headlineDesc')?.value);
            this.imageData.set("category", this.newpostForm.get('category')?.value);
            this.imageData.set("posted_by", localStorage.getItem('ID')!);
            this.imageData.forEach((value,key) => {
                console.log(key+" "+value)
            });
            this.http.post<any>("http://127.0.0.1:5000/api/news", this.imageData).subscribe({
                next: (response) => {console.log(response)
                this.imageData = new FormData();
            },
                error: (error) => console.log(error),
            })
            this.displayPostModal = "none";
            this.newpostForm.reset();
        } else {
            Object.keys(this.newpostForm.controls).forEach(field => { // {1}
                const control = this.newpostForm.get(field);            // {2}
                control?.markAsTouched({ onlySelf: true });       // {3}
            });
        }
    }
    close() {
        this.newpostForm.reset()
        this.displayPostModal = "none";
    }

    onFileChanged(event: any) {
        this.files = event.target.files;
        this.onUpload()
    }

    onUpload() {
        for (const file of this.files) {
            this.imageData.set("image", file, file.name)
            //this.formData.append("post", file, file.name);
        }

    }
}
