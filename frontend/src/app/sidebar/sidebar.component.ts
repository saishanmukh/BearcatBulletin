import { Component, OnInit } from '@angular/core';

declare const $: any;
declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}
export const ROUTES: RouteInfo[] = [
    { path: '/trending', title: 'Trending',  icon: 'fa fa-bolt', class: '' },
    { path: '/categories', title: 'Categories',  icon:'fa fa-list-alt', class: '' },
    { path: '/subscriptions', title: 'Subscriptions',  icon:'fa fa-user-plus', class: '' },
    { path: '/favorites', title: 'Favorites',  icon:'fa fa-heart', class: '' },
];

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html'
})
export class SidebarComponent implements OnInit {
  menuItems: any[] | undefined;

  constructor() { }

  ngOnInit() {
    this.menuItems = ROUTES.filter(menuItem => menuItem);
  }
  isMobileMenu() {
    // if ($(window).width() > 991) {
    //     return false;
    // }
    return false;
};
  
}
