# ChiMed

This is the ChiMed dataset for [ChiMed: A Chinese Medical Corpus for Question Answering](https://www.aclweb.org/anthology/W19-5027/) at BioNLP-2019.

## The Copyright

The copyright of the data belongs to [39ask](http://www.39.net/). We release the ChiMed dataset based on our contract.

## Request the ChiMed Dataset

To request the ChiMed Dataset, please download the contract in this repository ([English](./User_Contract_(English).pdf), [Chinese](./ChiMed_数据集使用协议（中文）.pdf)), fill the request form, sign it, and send the request file to `yhtian@uw.edu`. We will e-mail the data to the e-mail address provided in the request form within three business days if the request form meets our requirement.

Please read the following instructions before submit your request form:
* If your affiliation is in China, please use the [Chinese version](./ChiMed_数据集使用协议（中文）.pdf) of the contract and fill it in Chinese (including the signiture).  
* Because the Dataset is restrict to **non-commercial** use, we only accepted e-mail addresses that end with `.edu`.
* To submit a request with signiture, one way is to print the request form, sign, and scan it.


## Important Things to Note before Using the Data

### The Statistics

According to our contract with 39ask, the ChiMed data **is much larger than the one we used in the paper** and there is **NO** overlap between the current version and the one used in our paper. We recommend you to use the new data.

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
* `Recommended`: whether the answer is recommended by the webset (choose by the webset system);
* `Adopted`: whether the patient adopt the answer (choose by the user).
