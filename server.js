import express from "express";
import fetch from "node-fetch";
import cors from "cors";

const app = express();
app.use(cors());

app.get("/download", async (req, res) => {
  const videoId = req.query.id; // ?id=VIDEO_ID
  const url = `https://youtube-video-fast-downloader-24-7.p.rapidapi.com/video_details?video_id=${videoId}`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "x-rapidapi-key": "2f6a5aea35msh00a1fb740f1796dp1ff640jsn38401162b010",
        "x-rapidapi-host": "youtube-video-fast-downloader-24-7.p.rapidapi.com"
      }
    });

    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(5000, () => console.log("✅ Server running on http://localhost:5000"));
