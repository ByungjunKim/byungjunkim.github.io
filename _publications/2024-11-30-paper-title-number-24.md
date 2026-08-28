---
title: "Design and Implementation of a Subword-based Morphological Analyzer for Modern Sino-Korean Mixed Texts<br>(근대 국한문혼용체 자료 서브워드 기반 형태소 분석기의 설계와 적용)"
collection: publications
permalink: /publication/2024-11-30-paper-title-number-24
excerpt: "This study proposes the design and implementation of a subword-based morphological analyzer for automated analysis of modern Sino-Korean mixed texts. Current large-scale modern literature databases are difficult to process effectively with existing morphological analyzers due to their characteristics of mixed Sino-Korean characters and archaic Korean."
date: 2024-11-30
venue: 'Korean Journal of Digital Humanities'
# paperurl: 'http://byungjunkim.github.io/files/paper17.pdf'
citation: "Kim, B. (2024). Design and Implementation of a Subword-based Morphological Analyzer for Modern Sino-Korean Mixed Texts. <i>Korean Journal of Digital Humanities</i>, 1(2), 68-76, https://doi.org/10.23287/KJDH.2024.1.2.5"

---
[Online link](https://doi.org/10.23287/KJDH.2024.1.2.5)  
[Github](https://github.com/ByungjunKim/ModernKoreanSubword)    
[Download paper here](http://byungjunkim.github.io/files/paper24.pdf)


## Abstract
This study proposes the design and implementation of a subword-based morphological analyzer for automated analysis of modern Sino-Korean mixed texts. Current large-scale modern literature databases are difficult to process effectively with existing morphological analyzers due to their characteristics of mixed Sino-Korean characters and archaic Korean. To address this issue, we present a new approach using the sw_tokenizer of the kiwipiepy library based on subword tokenization. We implemented three models with different vocab sizes (32000, 48000, 64000) using approximately 2.3 million newspaper and magazine articles (about 771.5 million syllables) from 1890-1940 as training data. The experimental results show that larger vocab sizes better preserve the semantic units of compound Sino-Korean characters, and researchers can select appropriate analysis units according to their research purposes. This study contributes to digital humanities research by providing a practical tool for automated analysis of modern Sino-Korean mixed texts and suggests new directions for future research in this field.

## 초록
본 연구는 근대 국한문혼용체 자료의 자동화된 분석을 위한 서브워드 기반 형태소 분석기를 설계하고 적용하는 방법을 제안한다. 현재 구축된 대규모 근대 문헌 데이터베이스는 한자어와 옛한글이 혼재된 특성으로 인해 현존하는 형태소 분석기로는 효과적인 처리가 어렵다. 이러한 문제를 해결하기 위해 본 연구에서는 kiwipiepy 라이브러리의 sw_tokenizer를 활용하여 서브워드 토큰화 기반의 새로운 접근법을 제시한다. 1890-1940년대의 신문 및 잡지 자료 약 230만 건(약 7억 7천만 음절)을 학습 데이터로 활용하여 세 가지 다른 vocab_size(32000, 48000, 64000)를 적용한 모델을 구현하고 그 성능을 비교하였다. 실험 결과, vocab_size가 커질수록 복합 한자어의 의미 단위가 더 잘 보존되는 것을 확인하였으며, 연구 목적에 따라 적절한 분석 단위를 선택할 수 있음을 보였다. 본 연구는 근대 국한문혼용체 자료의 자동화된 분석을 위한 실용적인 도구를 제시함으로써 디지털 인문학 연구의 새로운 방향을 제시했다는 의의가 있다.