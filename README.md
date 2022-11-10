# tote_tracker
The code tracks a tote in the system and saves the video

- Currently the code is written for Ottawa AEO only. As more sites come in, the code will be refactored to become scalable

[Link to the source data for Ottawa](https://sunflower.kb.us-central1.gcp.cloud.es.io:9243/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-7d%2Fd,to:now))&_a=(columns:!(message,system_name),filters:!(),index:ce572630-0f58-11ed-bd81-e7f3585b181b,interval:auto,query:(language:kuery,query:'%22Divert%20decision%22%20%20and%20%22770000601205%22'),sort:!(!('@timestamp',desc))))

[Link to the source data for Jacksonville](https://sunflower.kb.us-central1.gcp.cloud.es.io:9243/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-7d%2Fd,to:now))&_a=(columns:!(message,system_name),filters:!(),index:ce572630-0f58-11ed-bd81-e7f3585b181b,interval:auto,query:(language:kuery,query:'%22Divert%20decision%22%20%20and%20%22770000601205%22'),sort:!(!('@timestamp',desc))))

# How to use it

- Go to the link above and download the raw CSV Data for your desired tote and timeframe
- Paste the .csv file in the site directory and rename it as **raw_file.csv**

**Note: Make sure the data in the CSV is in the reverse chronological order**
- Run with the python command : **python3 main_OTT.py**
- All videos will be saved in the videos directory

## Projects currently supported

- Sunflower - SPS - Ottawa
- Britton - SPS - Jacksonville
- Washington- SPS - Phoenix **(in the works)**

## Necessary Packages

    OpenCV - pip3 install opencv-python
    datetime
    Pandas
