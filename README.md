
## Network Intrusion Detection using Natural Language Processing and Ensemble Machine Learning

Security and its Applications 2023 | Mid Term Project

**Paper:** 

S. Das, M. Ashrafuzzaman, F. T. Sheldon and S. Shiva, "Network Intrusion Detection using Natural Language Processing and Ensemble Machine Learning," 2020 IEEE Symposium Series on Computational Intelligence (SSCI), Canberra, ACT, Australia, 2020, pp. 829-835, doi: 10.1109/SSCI47803.2020.9308268.

Ref : https://ieeexplore.ieee.org/document/9308268

**Brief Description:**

 Authors proposed an intrusion detection system (NLPIDS) that utilizes natural language processing and ensemble-based machine learning. The proposed NLPIDS converts natural language HTTP requests into vectors which are then used to train several supervised and ensemble-based machine learning models. The trained models are then used to detect anomalous traffic. We validated our method using HTTP DATASET CSIC 2010. The results show the efficacy of the NLPIDS by producing better F1-score (0.999) and negligible false alarms (0.007) compared to existing methods. The NLPIDS does not depend on attack methods and feature vectors.

**Dataset Source:**

https://www.tic.itefi.csic.es/dataset/

The HTTP dataset CSIC 2010 contains the generated traffic targeted to an e- Commerce web application developed at our department. In this web application, users can buy items using a shopping cart and register by providing some personal information. As it is a web application in Spanish, the data set contains some Latin characters.
The dataset is generated automatically and contains 36,000 normal requests and more than 25,000 anomalous requests. The HTTP requests are labeled as normal or anomalous and the dataset includes attacks such as SQL injection, buffer overflow, information gathering, files disclosure, CRLF injection, XSS, server side include, parameter tampering and so on. This dataset has been successfully used for web detection in previous works [4, 5, 6, 7, 8, 9].

The traffic is generated following the next steps:

First, real data are collected for all the parameters of the web application. All the data (names, surnames, addresses, etc.) are extracted from real databases. These values are stored in two databases: one for the normal values and other for the anomalous ones. Additionally, all the public available pages of the web application are listed.
Next, normal and anomalous requests are generated for every web page. In the case that normal requests have parameters, the parameter values are filled out with data taken from the normal database randomly. The process is analogous for anomalous requests, where the values of the parameters are taken from the anomalous database.

Three types of anomalous requests were considered:

1) Static attacks try to request hidden (or non-existent) resources. These requests include obsolete files, session ID in URL rewrite, configuration files, default files, etc.

2) Dynamic attacks modify valid request arguments: SQL injection, CRLF injection, cross-site scripting, buffer overflows, etc.

3) Unintentional illegal requests. These requests do not have malicious intention, however they do not follow the normal behavior of the web application and do not have the same structure as normal parameter values (for example, a telephone number composed of letters).

The attacks were generated with the help of tools such as Paros [10] and W3AF[11].

The WAFs where this dataset was used [4,5,6,7] follow the anomaly approach, i.e. the normal behavior of the web application is defined and the behavior apart from that are considered anomalous. Therefore, in this approach only normal traffic is needed for the training phase.

The dataset is divided into three different subsets. One subset for the training phase, which has only normal traffic. And two subsets for the test phase, one with normal traffic and the other one with malicious traffic.

## Authors
- [Debonil Ghosh	[M21AIE225] ](https://www.github.com/debonil)
- [Ravi Shankar Kumar [M21AIE247]](https://www.github.com/rsk-iitj)
- [Saurav Chowdhury [M21AIE256]](https://www.github.com/sauraviitj)
- [Prdeep Tripathy [M21AIE256]](https://www.github.com/sauraviitj)
- [Rakesh Sahoo [M21AIE256]](https://www.github.com/sauraviitj)



## Demo




## Usage





## Results

**Detailed Classifier Accuracy summary**



## Conclusion

