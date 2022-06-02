import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { IMAGES } from 'src/interface/images';
import { NEWS } from 'src/interface/news';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit {
  dataFetched!: NEWS[];
  toggle = true;

  constructor(private http: HttpClient, private datePipe: DatePipe) { }

  ngOnInit(): void {
    this.All()
    
  }

  All() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data;
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }

  Announcements() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "announcements"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }

  Events() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "events"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }

  Sports() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "sports"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }

  Health() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "health"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }
  UPD() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "upd"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }
  Local() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "local"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }
  Library() {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      this.dataFetched = data.filter(function (el) {
        return el.category == "library"
      }
      );
      this.dataFetched.forEach(obj => {
        obj.updated_date = this.datePipe.transform(obj.posted_date, 'MMM d, y, h:mm a');
      });
    })
  }

}
