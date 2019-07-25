# ChiMed

This is a repository to construct ChiMed corpus. 

To crawl the webset and construct the corpus. First download urls and data by running
```python
python ./src/data_collection.py
```

Next, to build ChiMed and datasets for relevancy prediction and adoptation prediction, run
```python
python ./src/build_dataset.py --data_flag dataset
```
```dataset``` denotes the dataset to construct. It must be one of ```corpus```, ```adoption``` and ```relevancy``` (or ```all``` to build all above, which is recommended). You need to build the corpus before the other two datasets.
