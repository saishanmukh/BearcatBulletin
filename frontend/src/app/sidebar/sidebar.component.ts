import { Component, OnInit } from '@angular/core';

declare const $: any;
declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}
export const ROUTES: RouteInfo[] = [
    { path: '/trending', title: 'Trending',  icon: 'pe-7s-graph', class: '' },
    { path: '/categories', title: 'Categories',  icon:'pe-7s-user', class: '' },
    { path: '/subscriptions', title: 'Subscriptions',  icon:'pe-7s-note2', class: '' },
    { path: '/favorites', title: 'Favorites',  icon:'pe-7s-news-paper', class: '' },
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
