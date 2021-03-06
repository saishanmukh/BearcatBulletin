import { Routes } from '@angular/router';

import { HomeComponent } from '../../app/home/home.component';
import { CategoryComponent } from '../category/category.component';
import { TrendingComponent } from '../trending/trending.component';
import { UserProfileComponent } from '../user-profile/user-profile.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'trending', component: TrendingComponent },
    { path: 'categories', component: CategoryComponent },
    { path: 'subscriptions', component: HomeComponent },
    { path: 'favorites', component: HomeComponent },
    { path: 'profile', component: UserProfileComponent}
];
