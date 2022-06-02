import { IMAGES } from "./images";

export interface NEWS {
    updated_date: string | null;
    category: String,
    channel_id: String,
    description: String,
    edited_date: String,
    hashtag: String,
    headline: String,
    images: IMAGES[],
    news_id: Number,
    posted_by: Number,
    posted_date: Date,
  }