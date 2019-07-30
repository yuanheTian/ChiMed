# ChiMed

This is a repository to construct ChiMed corpus. 

## Copyright Issue

We are still negotiating with the 39ask company (who has the copyright of the data) about the data release. For now, we **CANNOT** release the data directly. Once the company agrees us to release the data, we will update our repository and direct you to the right palce to download the data.

Here, we release the code to crawl the data and to construct the corpus in the same way as we did. 

Please note that the crawler may crawl urls that are different from those we used in our paper. If you want to build datasets exactly the same as ours, please wait for the negotiating result. Alternatively, you can send a request e-mail to ```yhtian@uw.edu```. We will send you the urls (not the data) we used to construct the corpus, if you agree that you will use the data for non-profit research porpose only and agree that you will **NOT** send the urls to others. 

## Usage

To use the crawler, please first make sure to download the proper explorer driver (Firefox recommended) and put it into the environment variable path (if using Linux) or put the driver file under the same directory as the program (if using Windows).

To crawl the webset and construct the corpus. First download urls and data by running
```python
python ./src/data_collection.py
```

Next, to build ChiMed and datasets for relevancy prediction and adoptation prediction, run
```python
python ./src/build_dataset.py --data_flag=dataset
```
```dataset``` denotes the dataset to construct. It must be one of ```corpus```, ```adoption``` and ```relevancy``` (or ```all``` to build all above, which is recommended). You need to build the corpus before the other two datasets.
