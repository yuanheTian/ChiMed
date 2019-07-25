# ChiMed

This is a repository to construct ChiMed corpus. 

To use the crawler, please first make sure to download the proper explorer driver (Firefox recommended) and put it into the environment variable path (if using Linux) or put the driver file under the same directory as the program (if using Windows).

To crawl the webset and construct the corpus. First download urls and data by running
```python
cd src && python data_collection.py
```

Next, to build ChiMed and datasets for relevancy prediction and adoptation prediction, run
```python
python ./src/build_dataset.py \-\-data_flag dataset
```
```dataset``` denotes the dataset to construct. It must be one of ```corpus```, ```adoption``` and ```relevancy``` (or ```all``` to build all above, which is recommended). You need to build the corpus before the other two datasets.
