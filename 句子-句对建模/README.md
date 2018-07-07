**目录**
---
<!-- TOC -->

- [句子、句对建模](#句子句对建模)
- [文献阅读](#文献阅读)

<!-- /TOC -->

## 句子、句对建模

- **句子建模**是在**词向量**的基础上生成“**句向量**”（**Sentence Embedding**）的模型。

  然后利用句向量表示不同句子之间的关系。
- **句对建模**则是在句向量的基础上，直接生成两个句子之间的关系，相当于一个小型的端到端模型。

## 文献阅读

- [Wuwei Lan & Wei Xu, 2018](../papers/Neural-Network-Models-for-Paraphrase-Identification,-Semantic-Textual-Similarity,-Natural-Language-Inference,-and-Question-Answering.pdf)
  - 本文复现了经典的句对模型，并测试了它们在不同任务上的表现。
  - 推荐文章：[深度学习模型复现难？看看这篇句子对模型的复现论文](https://zhuanlan.zhihu.com/p/38256345) - 知乎