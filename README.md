# ChiMed

This github repository includes the information about the ChiMed Corpus.

## The Copyright

The copyright of the corpus belongs to [39ask](http://www.39.net/). We release the ChiMed corpus based on our contract with 39ask.

## Request the ChiMed Dataset

To request the ChiMed Corpus, please download the contract in this repository ([English](./User_Contract_(English).pdf), [Chinese](./ChiMed_数据集使用协议（中文）.pdf)), fill the request form, sign it, and send the request file to `yhtian@uw.edu`. We will send the link to download the corpus to the e-mail address provided in the request form within three business days if the request form meets our requirements.

Please read the following instructions before submitting your request form:
* If your affiliation is in China, please use the [Chinese version](./ChiMed_数据集使用协议（中文）.pdf) of the contract and fill it in Chinese (including the signature).  
* Because the corpus is restricted to **non-commercial** use, we only accepted e-mail addresses that end with `.edu`.


## Important Things to Note before Using the Data

### The Statistics

| | Number |
|-|-:|
| \# of QA pages | 200,744 |
| \# of departments | 15 |
| \# of questions | 200,744 |
| avg \# of characters per question | 55.57 |
| \# of answers | 401,488 |
| avg \# of characters per answer | 85.21 |
| \# of unique keyphrases | 11,724 |
| avg # of keyphrases per QA page | 4.51 |

### "Recommended" flag vs. "Adopted" flag

For each answer in the corpus, there are two flags: `Recommended` and `Adopted`. Their differences are:
* `Recommended`: whether the answer is recommended by the 39ask website (chosen by the website system);
* `Adopted`: whether the patient adopts the answer (chosen by the user).


## Citation

If you use the ChiMed corpus, please cite [the following paper](https://www.aclweb.org/anthology/W19-5027/) (Note: the ChiMed Corpus is larger than the dataset used in this paper).

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

