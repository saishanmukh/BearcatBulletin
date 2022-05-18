import { Routes } from '@angular/router';

import { HomeComponent } from '../../app/home/home.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'trending', component: HomeComponent },
    { path: 'categories', component: HomeComponent },
    { path: 'subscriptions', component: HomeComponent },
    { path: 'favorites', component: HomeComponent },
];
