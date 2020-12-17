# ChiMed

This github repository includes the information about the ChiMed dataset.

## The Copyright

The copyright of the data belongs to [39ask](http://www.39.net/). We release the ChiMed dataset based on our contract.

## Request the ChiMed Dataset

To request the ChiMed dataset, please download the contract in this repository ([English](./User_Contract_(English).pdf), [Chinese](./ChiMed_数据集使用协议（中文）.pdf)), fill the request form, sign it, and send the request file to `yhtian@uw.edu`. We will send the link to download the data to the e-mail address provided in the request form within three business days if the request form meets our requirements.

Please read the following instructions before submitting your request form:
* If your affiliation is in China, please use the [Chinese version](./ChiMed_数据集使用协议（中文）.pdf) of the contract and fill it in Chinese (including the signature).  
* Because the Dataset is restricted to **non-commercial** use, we only accepted e-mail addresses that end with `.edu`.
* To submit a request with a signature, one way is to print the request form, sign, and scan it.


## Important Things to Note before Using the Data

### The Statistics

The ChiMed data **is much larger than the one we used in the paper** and there is **NO** overlap between the current version and the one used in [our paper](https://www.aclweb.org/anthology/W19-5027/), but the paper provides details of the data format. We recommend you to use the new data.

The statistics of the current version is included in the dataset.

| | Number |
|-|-:|
| \# of QA pages | 200,744 |
| \# of departments | 15 |
| \# of questions | 200,744 |
| \# of answers | 401,488 |
| \# of unique keyphrases | 11,724 |
| avg # of keyphrases | 4.51 |

### "Recommended" flag vs. "Adopted" flag

For each answer in the dataset, there are two flags: `Recommended` and `Adopted`. Their differences are:
* `Recommended`: whether the answer is recommended by the 39ask website (chosen by the website system);
* `Adopted`: whether the patient adopts the answer (chosen by the user).


## Citation

Please cite our paper: [ChiMed: A Chinese Medical Corpus for Question Answering](https://www.aclweb.org/anthology/W19-5027/) at BioNLP-2019 if you use ChiMed Dataset.

```
@inproceedings{tian-etal-2019-chimed,
    title = "ChiMed: A Chinese Medical Corpus for Question Answering",
    author = "Tian, Yuanhe and Ma, Weicheng and Xia, Fei and Song, Yan",
    booktitle = "Proceedings of the 18th BioNLP Workshop and Shared Task",
    month = aug,
    year = "2019",
    address = "Florence, Italy",
    pages = "250--260",
}
```

