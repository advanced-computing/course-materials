# Example API Documentation

## Connecting to the API
Since we are running our API locally we will access the endpoint at ```http://127.0.0.1:5000``` (or the address the appears on your console).

## Welcome
- Method: GET
- Path: ```/```
- Query parameters: None

This is just a friendly welcome to the API.

## Sum
- Method: GET
- Path: ```/sum```
- Query parameters: two integers ```a``` and ```b```

This query returns the sum of the two numbers in json format.

## Factorial
- Method: GET
- Path: ```/factorial```
- Query parameters: An integer number ```n```

This query display a message with the result of n!. If no number is provided, it takes ```n = 10``` by default.


## List Most Popular 1000 Youtube Videos
source: [Kaggle](https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos?resource=download)
- Method: GET
- Path: ```/api/list```
- Query parameters: 
    -format: ```json``` or ```csv```
    - filterby (optional): name of the column to filter the list. Columns:
        - ```Rank```: The rank of the videos.
        - ```Video```: Description of the videos.
        - ```VideoViews``` : No of views for the videos.
        - ```Likes```: No of likes for the videos.
        - ```Dislikes```: No of dislikes for the videos.
        - ```Category```:  Category of the videos.
        - ```Published```: Year on which the video was publishedblished
    - filtervalue (optional): value to filter the list by the column specified in filterby.
    - limit (optional): limit the number of results to show.
    - offset (optional): offset the results to show
- Example query:
```
http://127.0.0.1:5000/api/list?format=json&filterby=Published&filtervalue=2019&limit=5&offset=2
```

