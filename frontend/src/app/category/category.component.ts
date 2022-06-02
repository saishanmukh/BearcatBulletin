import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { IMAGES } from 'src/interface/images';
import { NEWS } from 'src/interface/news';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit {
  dataFetched!: NEWS[];
  toggle = true;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.All()
  }

  All(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data;
    })
  }

  Announcements(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "announcements"
      }
      );
    })
  }

  Events(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "events"
      }
      );
    })
  }

  Sports(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "sports"
      }
      );
    })
  }

  Health(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "health"
      }
      );
    })
  }
  UPD(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "upd"
      }
      );
    })
  }
  Local(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "local"
      }
      );
    })
  }
  Library(){
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "library"
      }
      );
    })
  }

}
