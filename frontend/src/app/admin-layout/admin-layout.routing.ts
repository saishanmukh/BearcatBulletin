import { Routes } from '@angular/router';

import { HomeComponent } from '../../app/home/home.component';
import { CategoryComponent } from '../category/category.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'trending', component: HomeComponent },
    { path: 'categories', component: CategoryComponent },
    { path: 'subscriptions', component: HomeComponent },
    { path: 'favorites', component: HomeComponent },
];
