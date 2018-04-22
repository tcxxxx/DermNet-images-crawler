# DermNet-imgsCrawler
### DermNet
<img src="http://119.29.151.114/dermnet.jpg"><br><br>
Dermnet (www.dermnet.com)is a publicly available dataset of more than 23000 dermatologist-curated skin disease images.
According to [this doc](https://pdfs.semanticscholar.org/af34/fc0aebff011b56ede8f46ca0787cfb1324ac.pdf), Dermnet organizes the skin diseases biologically in a **two-level** taxonomy. The bottom-level contains more than 600 skin diseases in a fine-grained granularity. The top-level contains **23** skin disease classes. Each of the top-level skin disease class contains a subcollection of the bottom-level skin diseases.

--------------------------------------------------------------------------
### Overview
This repo keeps the code to fetch water-marked images (relatively low resolution) automatically from DermNet. Here are some examples of melanoma fetched from DermNet:<br>
<img src="http://119.29.151.114/nevus-spilus-1.jpg" width="300" height="200">
<img src="http://119.29.151.114/nevus-spilus-2.jpg" width="300" height="200">
<img src="http://119.29.151.114/nevus-spilus-3.jpg" width="300" height="200">
<img src="http://119.29.151.114/nevus-spilus-4.jpg" width="300" height="200"><br><br>

The Python codes in the repo could download the whole dataset from DermNet:<br><br>
<img src="http://119.29.151.114/dermnetsample1.jpg"><br>


--------------------------------------------------------------------------
#### Recommended literatures about *skin disease classification*
- [Skin disease classification versus skin lesion characterization: Achieving robust diagnosis using multi-label deep neural networks](https://ieeexplore.ieee.org/document/7899659/)
- [A Deep Learning Approach to Universal Skin Disease Classification (proj report)](https://pdfs.semanticscholar.org/af34/fc0aebff011b56ede8f46ca0787cfb1324ac.pdf)
