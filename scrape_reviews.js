const { getJson } = require("serpapi");
const fs = require('fs');
const { DateTime } = require('luxon');

const apiKey = 'YOUR_API_KEY_HERE';
const productId = 'com.superplaystudios.dicedreams';

const params = {
  api_key: apiKey,
  engine: "google_play_product",
  gl: "us",
  store: "apps",
  product_id: productId,
  platform: "phone",
  sort_by: "2",
  all_reviews: "true",
  no_cache: "true",
  num: "100",
  hl: "en"
};

const getResults = async () => {
  const sevenDaysAgo = DateTime.now().minus({ days: 7 }).startOf('day');
  const today = DateTime.now().startOf('day');
  const allReviews = [];
  let nextPageToken = null;
  let searchCount = 0;
  const maxSearches = 50;

  // Delete the existing fetch.json file at the start of each execution
  if (fs.existsSync('fetch.json')) {
    fs.unlinkSync('fetch.json');
    console.log('Existing fetch.json file deleted.');
  }

  try {
    while (searchCount < maxSearches) {
      console.log(`Fetching reviews... (Search ${searchCount + 1}/${maxSearches})`);
      const currentParams = { ...params, next_page_token: nextPageToken };
      const json = await new Promise((resolve, reject) => {
        getJson(currentParams, (data) => {
          if (data.error) {
            reject(data.error);
          } else {
            resolve(data);
          }
        });
      });

      if (!json.reviews || json.reviews.length === 0) {
        console.log('No reviews found in the response.');
        break;
      }

      console.log(`Fetched ${json.reviews.length} reviews`);

      for (const review of json.reviews) {
        const reviewDate = DateTime.fromFormat(review.date, 'MMMM d, yyyy');

        if (reviewDate >= sevenDaysAgo && reviewDate < today) {
          allReviews.push({
            name: review.title || 'No Title',
            avatar: review.avatar || 'No Avatar',
            review_rating: review.rating || 'No Rating',
            review_likes: review.likes || 0,
            review_snippet: review.snippet || 'No Snippet',
            review_date: review.date
          });
        }
      }

      if (!json.serpapi_pagination?.next_page_token) {
        break;
      }

      nextPageToken = json.serpapi_pagination.next_page_token;
      searchCount++;
    }

    if (allReviews.length > 0) {
      fs.writeFileSync('fetch.json', JSON.stringify(allReviews, null, 2), 'utf-8');
      console.log(`Saved ${allReviews.length} reviews to fetch.json`);
    } else {
      console.log('No reviews found within the last 7 days.');
    }
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
};

getResults()
  .then(() => console.log('Scraping completed.'))
  .catch(error => console.error('Scraping failed:', error));
