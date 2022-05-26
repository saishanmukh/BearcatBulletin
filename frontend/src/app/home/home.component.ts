import { Component, OnInit } from '@angular/core';
import { LocationStrategy, PlatformLocation, Location } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  mockData = [{
    id: 1,
    imageURL: "https://www.nwmissouri.edu/media/news/2021/11/images/211103Bell-footballgame.jpg",
    headline: "Headline",
    description: "Joe and Judy Bell were recognized during the Homecoming football game Saturday. Joe graduated from the University in 1963 as its first African American to complete a degree. He and Judy have been married 60 years.",
    updatedby: "Last updated 3 mins ago"
  },
    {
    id: 2,
    imageURL: "https://www.nwmissouri.edu/media/news/2022/04/images/220428studentsatisfaction.jpg",
     headline: "Headline",
    description: "Results of the 2021 Ruffalo Noel Levitz Student Satisfaction Inventory show that Northwest outperforms its peers and national groups in student satisfaction. The survey asks students about a variety of topics, including campus life, instructional effectiveness, classroom support services and academic advising.",
    updatedby: "Last updated 3 mins ago"
  },
  {
    id: 3,
    imageURL: "https://www.nwmissouri.edu/media/news/2022/04/images/220428studentengagement.jpg",
     headline: "Headline",
    description: "The B.D. Owens Library offers spaces for students to collaborate and take study breaks.",
    updatedby: "Last updated 3 mins ago"
  },
{
  id: 4,
    imageURL: "https://www.nwmissouri.edu/media/news/2022/05/images/220513knacktive.jpg",
     headline: "Headline",
    description: "The Knacktive team comprising The Magic Beanstalk was named the winning team of this spring's task to create a comprehensive marketing campaign for Ringgold County, Iowa.",
    updatedby: "May 13, 2022"
  },
  {
    id: 5,
    imageURL: "https://www.nwmissouri.edu/media/news/2022/05/images/220507commencement1tw.jpg",
     headline: "Headline",
    description: "Northwest graduates turn their tassels in recognition of their degree conferrals during one of the University's four commencement ceremonies Friday and Saturday in Bearcat Arena.",
    updatedby: "Last updated 3 mins ago"
  },
{
  id: 6,
    imageURL: "https://www.nwmissouri.edu/media/news/2022/04/images/220429mockiep.jpg",
    headline: "Headline",
    description: "Elementary education and special education majors in Northwest's School of Education participated on Thursday in simulated meetings to discuss individual education plans, or IEPs.",
    updatedby: "Last updated 3 mins ago"
  }
]
  constructor() { }

  ngOnInit() {
  
    }

  moveToLiked(id: any) {
  }
}
