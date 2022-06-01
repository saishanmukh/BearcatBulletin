import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

export interface IMAGES{
  image_id: Number,
  image_path: String,
  news_id: Number,
}

export interface NEWS {
  category: String,
  channel_id: String,
  description: String,
  edited_date: String,
  hashtag: String,
  headline: String,
  images: IMAGES[],
  news_id: Number,
  posted_by: Number,
  posted_date: String,
}
@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit {
  dataFetched!: NEWS[];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      console.log(data);
      this.dataFetched = data;
    })
  }

}
