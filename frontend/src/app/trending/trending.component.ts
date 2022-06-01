import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { IMAGES } from 'src/interface/images';
import { NEWS } from 'src/interface/news';

@Component({
  selector: 'app-trending',
  templateUrl: './trending.component.html',
  styleUrls: ['./trending.component.css']
})
export class TrendingComponent implements OnInit {
  dataFetched!: NEWS[];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<NEWS[]>("http://127.0.0.1:5000/api/news").subscribe(data => {
      console.log(data);
      this.dataFetched = data;
    })
  }

}
