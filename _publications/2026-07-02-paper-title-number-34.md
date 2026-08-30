---
title: "GOLEMcoref: A Multilingual Coreference Dataset of Fiction"
collection: publications
permalink: /publication/2026-07-02-paper-title-number-34
excerpt: "We present a multilingual coreference dataset of 827k tokens of fiction in 7 languages: Bahasa Indonesia, Chinese, Dutch, English, Italian, Korean, and Spanish."
date: 2026-07-02
venue: 'Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026, Volume 2: Short Papers)'
# paperurl: 'http://byungjunkim.github.io/files/paper34.pdf'
citation: "van Cranenburgh, A., Yang, X., Alvanita, Di Domenico, C. N., Ferragud, M., Graciotti, A., Ion, A. G., <b>Kim, B.</b>, Park, S., Visser Solissa, N., Zhou, X., & Pianzola, F. (2026). GOLEMcoref: A Multilingual Coreference Dataset of Fiction. <i>Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)</i>, 472-480."


---
[Online link](https://aclanthology.org/2026.acl-short.39/)  
[Github](https://github.com/GOLEM-lab/GOLEMcoref)  
[Download paper here](http://byungjunkim.github.io/files/paper34.pdf)


## Abstract
We present a multilingual coreference dataset of 827k tokens of fiction in 7 languages: Bahasa Indonesia, Chinese, Dutch, English, Italian, Korean, and Spanish. The dataset includes full stories of diverse lengths, ranging from 500 to 17k words. We discuss our annotation scheme focusing on characters and language-specific challenges we encountered. Finally we present evaluation results of a neural coreference system trained on our dataset. We show that jointly training a system across all languages provides a strong improvement over monolingually trained models. The dataset is available under a creative commons license in CoNLL-2012 and CorefUD format at [https://github.com/GOLEM-lab/GOLEMcoref/](https://github.com/GOLEM-lab/GOLEMcoref/).

### Table 1: Dataset statistics

Token counts include punctuation and zero anaphora.

|  | Chinese | Dutch | English | Indonesian | Italian | Korean | Spanish | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Tokens | 104,772 | 119,989 | 134,348 | 132,719 | 120,058 | 90,031 | 125,086 | **827,003** |
| Sentences | 3,907 | 9,953 | 8,836 | 10,901 | 6,148 | 9,686 | 6,221 | **55,652** |
| Zero anaphora | 68 | 0 | 36 | 4,939 | 5,831 | 39 | 4,703 | **15,616** |
| Split antecedents | 208 | 670 | 436 | 163 | 231 | 320 | 403 | **2,431** |
| Mentions | 8,188 | 16,427 | 18,511 | 19,368 | 14,491 | 9,975 | 15,722 | **102,682** |
| Entities | 570 | 913 | 741 | 684 | 552 | 667 | 816 | **4,943** |
| tokens / sent | 26.8 | 12.1 | 15.2 | 12.2 | 19.5 | 9.3 | 20.1 | **14.9** |
| mentions / tokens | 0.078 | 0.137 | 0.138 | 0.146 | 0.121 | 0.111 | 0.126 | **0.124** |
| mentions / entities | 14.36 | 17.99 | 24.98 | 28.32 | 26.25 | 14.96 | 19.27 | **20.77** |
