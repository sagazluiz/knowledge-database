### ARQUIVO: Sci-Net: Combining large language models with enterprise knowledge graphs: a perspective on enhanced natural language understanding.pdf

<CONTENT>
<!-- image -->

<!-- image -->

## OPEN ACCESS

EDITED BY Aleksandr Raikov,

National Supercomputer Center, China

REVIEWED BY Stefano Silvestri,

National Research Council (CNR), Italy

*CORRESPONDENCE Luca Mariotti

luca.mariotti@unimore.it

RECEIVED

05 July 2024

ACCEPTED

09 August 2024

PUBLISHED

27 August 2024

## CITATION

Mariotti L, Guidetti V, Mandreoli F, Belli A and Lombardi P ( 2024 ) Combining large language models with enterprise knowledge graphs: a perspective on enhanced natural language understanding. Front. Artif. Intell. 7 : 1460065 . doi: 10 . 3389 /frai. 2024 . 1460065

## COPYRIGHT

© 2024 Mariotti, Guidetti, Mandreoli, Belli and Lombardi. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Combining large language models with enterprise knowledge graphs: a perspective on enhanced natural language understanding

Luca Mariotti 1 *, Veronica Guidetti 1 , Federica Mandreoli 1 , Andrea Belli 2 and Paolo Lombardi 2

1 Department of Physics, Informatics and Mathematics, Università di Modena e Reggio Emilia, Modena, Italy, 2 Expert.ai, Modena, Italy

Knowledge Graphs (KGs) have revolutionized knowledge representation, enabling a graph-structured framework where entities and their interrelations are systematically organized. Since their inception, KGs have significantly enhanced various knowledge-aware applications, including recommendation systems and question-answering systems. Sensigrafo, an enterprise KG developed by Expert.AI, exemplifies this advancement by focusing on Natural Language Understanding through a machine-oriented lexicon representation. Despite the progress, maintaining and enriching KGs remains a challenge, often requiring manual efforts. Recent developments in Large Language Models (LLMs) offer promising solutions for KG enrichment (KGE) by leveraging their ability to understand natural language. In this article, we discuss the state-of-the-art LLM-based techniques for KGE and show the challenges associated with automating and deploying these processes in an industrial setup. We then propose our perspective on overcoming problems associated with data quality and scarcity, economic viability, privacy issues, language evolution, and the need to automate the KGE process while maintaining high accuracy.

## KEYWORDS

LLMS, knowledge graph, relation extraction, knowledge graph enrichment, AI, enterprise AI, carbon footprint, human in the loop

## 1 Introduction

A Knowledge Graph (KG) represents real-world knowledge using a graph structure, where nodes denote entities and edges represent relationships between them (Hogan et al., 2021). Since Google introduced the Knowledge Graph in 2012, KGs have become essential in knowledge representation, enhancing various tasks Companies use them to improve product performance, boosting data representation and transparency in recommendation systems, efficiency in question-answering systems, and accuracy in information retrieval systems (Peng et al., 2023).

This work presents the perspective of Expert.AI, a leading enterprise in Natural Language Understanding (NLU) solutions, centered on meticulously created and curated KGs by expert linguists. While manual curation ensures high precision and data quality, it demands significant human effort, and the rapid evolution of real-world knowledge requires frequent updates to KGs.

frontiersin.org

Recent advancements in Large Language Models (LLMs) suggest potential for partial automation of this process. LLMs, deep learning architectures designed for natural language processing, have demonstrated impressive results in NLU tasks. Their advanced capabilities represent a promising avenue for automating and enhancing Knowledge Graph Enrichment (KGE), refining, and adding new entities and relationships in KGs. By leveraging the implicit knowledge embedded within pre-trained LLMs (PLMs), companies can streamline the identification of new entities and relationships in external corpora, enriching their KGs with minimal manual intervention (Valmeekam et al., 2024).

However, automating KGE from external text in an industrial context is far from straightforward. It is crucial to choose an appropriate methodological framework: various PLM-based KGE techniques require model finetuning, while others rely on prompting. We will discuss the advantages and disadvantages of both approaches. For instance, while finetuning is generally costly and requires large amounts of annotated data, prompting is more cost-effective but poses privacy-related risks.

We will also examine the primary challenges of implementing corporate KGE solutions, categorizing them into four areas: (i) the quality and quantity of public or automatically annotated data, (ii) developing sustainable solutions in terms of computational resources and longevity, (iii) adaptability of PLM-based KGE systems to evolving language and knowledge, and (iv) creating models capable of efficiently learning the KG structure.

We review existing solutions for each issue and identify promising options for automating KGE in industrial settings using PLMs while maintaining high quality. We recommend a hybrid approach that combines PLMs, KG structure understanding, and domain expertise, ensuring privacy compliance. To adapt to evolving LLMs, we suggest treating PLMs as plug-and-play components for versatility and longevity.

This paper is structured as follows: Section 2 presents Expert.AI and its research investment objectives. Section 3 discusses the state-of-the-art in PLM-based KGE. Section 4 provides our perspective on the challenges of deploying these methods in an enterprise environment. Finally, conclusions are drawn in Section 5.

## 2 Sensigrafo: an enterprise KG and its characteristics

Expert.AI, formerly known as Expert System, is a leading AI enterprise specializing in solving complex language challenges. With over 300 natural language solutions, Expert.AI has transformed language-intensive processes across various sectors. Central to Expert.AI's NLU solutions is a collection of large KGs called Sensigrafo s, meticulously built by linguists and domain experts and carefully modified to gain performance in downstream NLU tasks. Each Sensigrafo includes attributes like grammatical role, semantic relation, definition/meaning, domain, and frequency that establish the characteristics of words and concepts (Buzzega et al., 2023). Terms with the same meaning are grouped into syncons, interconnected by millions of logical and linguistic links, organized hierarchically. For example, the English Sensigrafo contains about 440,000 syncons, grouping more than 580,000 words, and 80+ relation types, yielding around 7.1 million links.

In contrast, most collaborative open-source KGs are generated automatically, resulting in numerous triples. DBpedia, for instance, contains about 900 million triples. The number of entity classes varies across KGs, with Wikidata having over 110 million items and 500 million facts, and YAGO encompassing knowledge of more than 67 million entities and 343 million facts (Suchanek et al., 2023). The number of relation types also varies, with Freebase having 1,345 and YAGO holding only 140 (Suchanek et al., 2023). These KGs span diverse domains, primarily derived from text corpora like Wikipedia, aiming to cover extensive real-world knowledge. Conversely, each Sensigrafo is carefully constructed using only information sources from its intended domain, making the information extraction operation much more reliable and accurate.

However, the accuracy of Sensigrafo's information comes at a high maintenance cost. Adding new syncons and relations requires full human supervision, aided by Expert.AI's semantic engine, Cogito. Cogito uses a Sensigrafo to resolve ambiguities related to word meanings and can expand its knowledge through expert input or analyzing tagged content using ML algorithms.

As real-world information grows and the cost of upgrading Sensigrafo increases, Expert.AI plans to integrate symbolic and statistical technologies, combining expert-validated rules with AI methods to automate Sensigrafo updates. This hybrid approach is expected to reduce the costs of developing and maintaining symbolic AI solutions. Nevertheless, any AI solution should be accompanied by a high degree of explainability, robustness, and precision to make enrichment systems transparent and reliable.

To identify the crucial aspects in developing such a solution, we will present state-of-the-art KGE techniques based on PLMs.

## 3 Pretrained LLM for KG management and enrichment

Relation extraction (RE) and named entity recognition (NER) are key challenges in automatic KGE. RE identifies and categorizes relationships between entities in unstructured text, expanding the KG's structure. NER focuses on recognizing, classifying, and linking entities in the text to the knowledge base. These processes are crucial for accurately identifying entities and their interconnections, enhancing KGs. Recent literature highlights two approaches to NER and RE: creating large training sets with handcurated or extensive automatic annotations to fine-tune LLMs, or using precise natural language instructions, replacing domain knowledge with prompt engineering efforts (Levy et al., 2017; Li et al., 2019; Soares et al., 2019; Peng et al., 2020; Agrawal et al., 2022; Wang et al., 2023).

Supervised methods for NER and RE usually include a pretraining stage followed by zero-shot learning (Wang et al., 2022) or the use of specialized architectures and training setups (Yu et al., 2020; Li et al., 2022b). Due to the lack of large annotated corpora, many approaches for RE and NER rely on distant supervision (DS), an automated data labeling technique that aligns knowledge bases with raw corpora to produce annotated data.

Early DS approaches to RE use supervised methods to align positive and negative pair relations for pre-training language models, followed by few-shot learning to extract relations (Soares et al., 2019; Peng et al., 2020). DS methods for NER involve tagging text corpora with external knowledge sources like dictionaries, knowledge bases, or KGs. A common DS method for NER is the teacher-student framework. For example, Liang et al. (2020) proposed a two-stage method: fine-tuning a LLM on DS labels, followed by teacher-student system self-training with pseudo soft labels to improve performance.

While DS is useful when labeled data is scarce or expensive, it can introduce incomplete and inaccurate labels. To address this, recent works have focused on mitigating DS label noise and improving results (Wan et al., 2022). A common method to address DS noise in RE is multi-instance learning (MIL) (Zeng et al., 2015), which groups sentences into bags labeled as positive or negative with respect to a relation, shifting the RE task from single sentences to bags. However, MIL is not data-efficient, leading to recent extensions into contrastive learning setups. These efforts aim to cluster sentences with the same relational triples and separate those with different triples in the semantic embedding space (Chen et al., 2021; Li et al., 2022a).

Recent years have seen a significant increase in work on NER and RE involving prompt engineering. Prompting for NER includes using entity definitions, questions, sentences, and output examples to guide LLMs in understanding entity types and extracting answers (Ashok and Lipton, 2023; Kholodna et al., 2024). For RE, tasks are rephrased as question-answering (Levy et al., 2017), often injecting latent knowledge contained in relation labels into prompt construction (Chen et al., 2022) and iteratively fine-tuning prompts to enhance the model's ability to focus on semantic cues (Son et al., 2022). In general, zero-shot learning methods have been shown to perform better than supervised settings when the amount of training data is scarce.

Choosing between prompt engineering and fine-tuning is challenging. While prompting with large LLMs like GPTs is appealing for handling complex tasks with minimal data annotation, it can underperform in NER compared to finetuned smaller PLMs like BERT derivations, especially with more training data (Gutierrez et al., 2022; Keloth et al., 2024; Pecher et al., 2024; Törnberg, 2024). Large LLMs, such as GPT-3, struggle with specific information extraction tasks, including managing sentences without named entities or relations (Gutierrez et al., 2022). Prompting also faces hallucination issues, often overconfidently labeling negative inputs as entities or relations. Some approaches, such as Wang et al. (2023), address this by enriching prompts and reducing hallucinations via self-verification strategies. Other methods correct inaccurate NER and RE-prompting results through active learning techniques (Wu et al., 2022) or by distilling large PLMs into smaller models for specific tasks (Agrawal et al., 2022).

## 4 Perspective

Summarizing the previous sections, the main challenges for enterprise LLM-based solutions for KGE include:

- Computational resources and longevity: creating tailored PLM-based KGE solutions can be costly and resource-intensive. There is a need for lightweight, sustainable, and durable training pipelines.
- Data quality and benchmarking: collaborative and Enterprise KGs have different structures, causing a mismatch between public benchmark datasets and enterprise use cases.
- Evolving knowledge: robust methods are needed to combine automated novelty detection (new links and nodes for the KG) with high-quality human-curated interventions.
- Lack of adaptive hidden representations: the learning paradigm should shift from classification to representation learning to accommodate novelty and efficiently encode KG features.

In the following sections, we will provide a comprehensive analysis of each of these challenges.

## 4 . 1 Computational resources and longevity of solutions

When developing enterprise-level NLU solutions, it's crucial to consider computational resources and carbon footprint due to the high environmental and economic costs of traditional model training (Patil and Gudivada, 2024). Fully fine-tuning PLMs, while effective for specific tasks, is often costly and inefficient, requiring substantial computational resources and time. These models are tailored for narrow applications, making updates challenging (Razuvayevskaya et al., 2023).

In contrast, in-context learning provides greater flexibility, facilitating adaptation to the rap