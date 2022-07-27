# ChiMed

This github repository includes the information about the ChiMed Corpus.

## Updates

Apr. 29, 2022

**ChiMed** is availabel by valid request! The ChiMST corpus contains 1,000 QA pages with annotations of Chinese word segmentation and medical terms.

## The Copyright

The copyright of the corpus belongs to [39ask](http://www.39.net/). We release the ChiMed corpus based on our contract with 39ask.

## Request the ChiMed and ChiMST Dataset

Please vist [here](https://github.com/synlp/ChiMST) for the information to request the datasets.

## Important Things to Note before Using the ChiMed

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

