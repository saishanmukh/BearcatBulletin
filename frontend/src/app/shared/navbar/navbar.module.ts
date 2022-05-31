import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from './navbar.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
    imports: [ RouterModule, CommonModule, FormsModule, ReactiveFormsModule ],
    declarations: [ NavbarComponent ],
    exports: [ NavbarComponent ]
})

export class NavbarModule {}
