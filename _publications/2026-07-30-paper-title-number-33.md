---
title: "KNoTE: A TEI Encoded XML Dataset of Modern Korean Novels"
collection: publications
permalink: /publication/2026-07-30-paper-title-number-33
excerpt: "KNoTE (Korean Novel TEI Encoded) is an open XML dataset of 33 modern Korean novels (1906–1954) by 22 authors, encoded according to the TEI P5 Guidelines."
date: 2026-07-30
venue: 'Journal of Open Humanities Data'
# paperurl: 'http://byungjunkim.github.io/files/paper33.pdf'
citation: "Kim, G., Park, S., Ji, H., Lee, H., Lee, B., Jeong, C., & <b>Kim, B.</b> (2026). KNoTE: A TEI Encoded XML Dataset of Modern Korean Novels. <i>Journal of Open Humanities Data</i>, 12, 102."


---
[Online link](https://doi.org/10.5334/johd.590)  
[Dataset](https://doi.org/10.5281/zenodo.18679321)  
[Github](https://github.com/AKS-DHLAB/KNoTE)  
[Download paper here](http://byungjunkim.github.io/files/paper33.pdf)


## Abstract
KNoTE (Korean Novel TEI Encoded) is an open XML dataset of 33 modern Korean novels (1906–1954) by 22 authors, encoded according to the TEI P5 Guidelines. Source texts were collected from Korean Wikisource and semi-automatically encoded using a large language model via prompt engineering, followed by multi-layered manual validation by seven annotators. The markup captures named entities, character ontologies, direct speech, Hanja annotations, and period-specific metadata including political ideologies, colonial-era place names, and social class markers. As the first TEI-conformant corpus of modern Korean literature, the dataset supports computational literary analysis, NLP model fine-tuning, and cross-corpus interoperability.

## TEI Elements and Attributes
*Table 1. TEI elements and attributes used in the KNoTE dataset.*

| Category | Element | Key attributes | Function |
|---|---|---|---|
| **TEI Header** | `titleStmt` | — | Title, author, encoder credits |
| | `respStmt` | — | Encoder/reviewer attribution |
| | `sourceDesc/bibl` | `type` | Source provenance |
| | `encodingDesc` | — | Encoding standard (TEI ALL) |
| | `revisionDesc/change` | `when`, `who` | Encoding/review dates |
| **Characters** | `listPerson` | — | Character registry |
| | `person` | `xml:id` | Individual character |
| | `personGrp` | `xml:id` | Collective character group |
| | `persName` | `xml:lang` | Name in Korean or Hanja |
| **Entities** | `persName` | `ref` | Named character mention |
| | `rs` | `ref`, `type` | Pronoun/epithet reference |
| | `placeName` | — | Place name |
| | `orgName` | — | Organisation name |
| | `date` | `when`, `type` | Date reference |
| | `time` | `when`, `type` | Time-of-day reference |
| **Speech** | `said` | `who`, `aloud`, `direct`, `mode` | Direct speech, thought, or monologue |
| **Language** | `foreign` | `xml:lang="zh"`, `xml:lang="ja"` | Hanja preservation and Japanese in Hangul |
| **Structure** | `div` | `type`, `n` | Chapter/section division |
| | `p` | — | Paragraph |
| | `head` | — | Chapter title |

A complete inventory of all TEI elements and attributes in the corpus is provided in the repository ([`KNoTE_TEI_tags_full.md`](https://github.com/AKS-DHLAB/KNoTE)) and the Zenodo record.
