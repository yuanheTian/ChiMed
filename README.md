# ChiMed

This is a repository to construct ChiMed corpus. 

## Copyright Issue

Because the copyright issue, we **CANNOT** release the data directly. Therefore, we release the code to crawl the website and to construct the corpus in the same way as we did. 

Please note that the crawler may crawl urls that are different from those we used in our paper. If you want to build the datasets that are exactly the same as ours, please send a request e-mail to ```yhtian@uw.edu```. We will send you the urls we used to construct the corpus, if you agree that you will use the data for non-profit research porpose only and agree that you will **NOT** send the urls to others. 

## Usage

To use the crawler, please first make sure to download the proper explorer driver (Firefox recommended) and put it into the environment variable path (if using Linux) or put the driver file under the same directory as the program (if using Windows).

To crawl the webset and construct the corpus. First go to ```src``` directory and download urls and data by running
```python
python data_collection.py
```

Next, to build ChiMed and datasets for relevancy prediction and adoptation prediction, run
```python
python ./src/build_dataset.py --data_flag=dataset
```
```dataset``` denotes the dataset to construct. It must be one of ```corpus```, ```adoption``` and ```relevancy``` (or ```all``` to build all above, which is recommended). You need to build the corpus before the other two datasets.
