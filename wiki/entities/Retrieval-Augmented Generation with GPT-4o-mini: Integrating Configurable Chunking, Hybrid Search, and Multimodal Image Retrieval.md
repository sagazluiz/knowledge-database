### ARQUIVO: Retrieval-Augmented Generation with GPT-4o-mini: Integrating Configurable Chunking, Hybrid Search, and Multimodal Image Retrieval.pdf

<CONTENT>
## Retrieval-Augmented Generation with GPT-4o-mini: Integrating Configurable Chunking, Hybrid Search, and Multimodal Image Retrieval

## Chun Wei Loo

Faculty of Computing and Information Technology,

Tunku Abdul Rahman University of Management and Technology Kuala Lumpur, Malaysia loocw-wp21@student.tarc.edu.my

Huen Thong Chong Faculty of Computing and Information Technology, Tunku Abdul Rahman University of Management and Technology Kuala Lumpur, Malaysia chonght-wp21@student.tarc.edu.my

## Zi Qian Leong

Faculty of Computing and Information Technology,

Tunku Abdul Rahman University of Management and Technology Kuala Lumpur, Malaysia leongzq-wm22@student.tarc.edu.my

## Yong Poh Yu

Centre For Business Incubation and

Entrepreneurial Ventures, Tunku Abdul Rahman University of Management and Technology Kuala Lumpur, Malaysia yuyp@tarc.edu.my

Abstract -Retrieval-augmented generation (RAG) systems significantly enhance the capabilities of large language models (LLMs) by grounding responses in external knowledge. We implemented a RAG system utilizing the GPT-4o-mini model to advance knowledge base management, configurable document processing, and multimodal information retrieval. We constructed a modular knowledge base framework that supports creation, configuration, and granular management of diverse information sources, including text in formats of TXT, PDF, CSV, and extracted visual data. The key feature of the developed framework is the user-configurable document chunking process, allowing optimization of text segmentation through adjustable parameters (chunk size, overlap, custom separators) before ingestion. The framework employs ChromaDB as its vector store, implementing a hybrid search that combines dense vector-based semantic similarity with traditional keyword matching, offering configurable weighting and relevance thresholds. Furthermore, we introduce automated image extraction from PDF documents into knowledge ingestion. Extracted images are indexed with associated metadata and rudimentary captions. In the query process, relevant images are retrieved alongside pertinent text chunks, providing richer, multimodal context to the GPT-4o-mini model. The developed framework highlights the design and implementation details of the components, demonstrating a flexible and efficient construction of RAG systems capable of leveraging both textual and visual information from managed knowledge bases.

Keywords-retrieval-augmented generation (RAG), knowledge base management, configurable chunking, multimodal rag, image retrieval

## I. INTRODUCTION

Large language models (LLMs) have capabilities in understanding and generating human-like text. However, their knowledge is often limited due to their training data cutoff, leading to potential inaccuracies or 'hallucinations' when faced with queries requiring up-to-date or specialized information. Retrieval-augmented generation (RAG) mitigates such limitations by dynamically grounding LLM responses in relevant information retrieved from external knowledge sources [1]. RAG enhances the factual accuracy, relevance, and trustworthiness of generated content [2].

Despite the advantages of RAG, standard RAG systems often employ static document processing techniques, particularly for chunking, the process of segmenting documents into manageable pieces for retrieval. However, the optimal chunking strategy significantly impacts retrieval performance and is largely dependent on document structure and content [3]. Its one-size-fits-all approach leads to suboptimal retrieval, where context is fragmented or irrelevant information dilutes the context provided to the LLM [3]. Providing end-users or system administrators with control over these parameters during the ingestion phase is also overlooked.

Many knowledge sources, such as technical manuals, reports, or academic documents, are stored as PDFs, containing rich multimodal information, including text, tables, and images. Therefore, conventional RAG systems focus on textual data, ignoring other visual elements that provide critical context [4]. Therefore, integrating information from different modalities effectively remains a significant challenge in RAG development [5].

In this study, we designed and implemented a practical, multimodal RAG system to address these challenges, utilizing the efficient GPT-4o-mini model. The developed flexible knowledge base (KB) management system allows the creation and organization of diverse document sources (TXT, PDF, CSV) via dedicated application programming interfaces. Its novel workflow enables user-configurable document chunking before vectorization, allowing users to specify parameters, including chunk size, overlap, and separators, through an API call to optimize ingestion for specific documents. Its integrated modules automate image extraction from PDF documents during ingestion, coupled with a retrieval mechanism to incorporate relevant visual context (via captions) into the LLM prompt. The developed system with ChromaDB for vector storage has hybrid search capabilities and a FastAPI backend for system management and interaction.

Document Ingestion

Document Upload API

Document Store

Vector Store

Metadata

The remainder of this article is organized as follows. Section II reviews related works in configurable chunking and multimodal RAG. Section III details the system architecture and methodologies for KB management, chunking configuration, image handling, vector storage, and multimodal retrieval. Section IV presents demonstration examples of the system's core functionalities. Section V discusses observations and limitations, and Section VI concludes the paper with future work directions.

Image Index

## II. RELATED WORK

## A. Chunking Strategies in RAG

The developed system segments documents into chunks, significantly enhancing RAG performance [3]. Common approaches include fixed-size, sentence-based, or recursive character splitting [3,6], while we considered the impact of different chunk sizes and overlaps [7,8]. Previous systems apply a predefined strategy during ingestion. Recently, adaptive chunking has been applied based on document content [9], but it lacks mechanisms for direct user configuration before processing specific documents. The developed system exposes chunking parameters (size, overlap, and separators) through an API, allowing users to tailor the process for individual documents after uploading but before vectorization, offering explicit control based on perceived document characteristics or downstream needs.

## B. Vector Storage and Retrieval

Vector databases, such as ChromaDB, Pinecone, and Weaviate, are commonly employed in RAG systems to store embeddings and perform similarity searches [10]. While semantic search using dense vectors is a standard [1], combining it with traditional keyword search (hybrid search) improves retrieval robustness, especially for queries containing specific entities or jargon [11]. ChromaDB aligns with current practices, but we enhanced the system's ability by leveraging hybrid search strategies provided by the underlying VectorDB class methods (get\_similar\_semantic, get\_similar\_keyword), configured via API settings, offering flexibility in the retrieval phase.

## C. Multimodal RAG and Image Integration

Extending RAG beyond text to incorporate multiple modalities has been extensively researched [4,5]. Related methods involve using sophisticated multimodal embedding models or dedicated vision-language models to process images and generate textual descriptions or embeddings [5,12]. Researchers have focused on web data or paired image-text datasets [4]. We focused on a specific, practical challenge: leveraging images embedded within PDF documents, which are common in enterprise or academic knowledge bases. Therefore, we implemented an automated extraction process using a PDF parsing library (PyMuPDF) during text ingestion, storing the actual images alongside extracted metadata and basic captions. This differs from approaches requiring preexisting image-text pairs or relying solely on complex end-to-end multimodal models. We then used these extracted elements (textual captions) to provide relevant visual context signals within the prompt for a primarily text-based LLM (GPT-4o-mini).

## D. KB Management

Effective management of the knowledge sources underpinning RAG is crucial for maintainability and relevance [2]. Frameworks exist for organizing and updating knowledge bases. The developed system emphasizes a database-backed management layer (SQLite) coupled with a FastAPI interface, providing programmatic control over creating knowledge bases, uploading documents, managing their processing status (including the 'Pending Configuration' state for chunking), and associating them with specific chatbot instances.

## III. SYSTEM DESIGN AND METHODOLOGY

The architecture and components of the developed RAG system were designed for flexibility in knowledge ingestion and multimodal context retrieval. The system leverages a FastAPI backend, SQLite for metadata management, ChromaDB for vector storage, and integrates PDF image extraction capabilities. Its workflow is depicted in Fig. 1.

Fig. 1. Workflow of developed system.

<!-- image -->

## A. KB and Document Management

The foundation of the system is a modular KB structure managed by a dedicated API. Each KB is associated with a specific chatbot instance and acts as a container for related documents.

- KB creation: Users create KBs via the /api/knowledgebase/create/{chatbot\_id} endpoint, providing a name and description. KB metadata (name, description, associated chatbot, document/chunk counts) is stored in a Knowledge table in SQLite.
- Document upload: Documents (TXT, PDF, CSV) are uploaded to a specific KB using /api/knowledgebase/upload/{knowledge\_id}. When uploaded, the document metadata (filename, type, size, KB association) is recorded in the Document SQLite table,

but the document status is set to 'Pending Configuration'. The physical file is stored in a structured directory (output\_files/{user\_id}/{chatbot\_id}/{knowledge\_id}). This decouples the initial upload from the potentially resource-intensive processing and chunking step.

## B. Configurable Chunking Workflow

A key feature of the developed system is the ability to configure chunking parameters after upload but before processing and vectorization.

- Configuration and processing trigger: The api/document/configure-and-process endpoint takes a doc\_id (document tagged as 'Pending Configuration') and user-defined chunking parameters: chunk\_size (target character count), chunk\_overlap (character overlap between chunks), and optionally separators (list of strings for splitting).
- Chunking implementation: The system uses RecursiveCharacterTextSplitter. The user-provided parameters are directly passed to the splitter instance to tailor the segmentation based on the document's nature (e.g., smaller chunks for dense text, larger for narrative content). The Document status is updated to 'Processing'.
- Metadata enrichment: During chunking, chunks are assigned unique IDs (chunk-{uuid}), and keywords are extracted using TfidfVectorizer and added to the chunk's metadata with token count (using tiktoken).

## C. Image Extraction and Indexing

To handle multimodal information within PDFs, an image extraction module (ImageExtractor) is integrated into the document processing workflow triggered by /api/document/configure-and-process.

- Extraction process: If the processed document is a PDF, the system uses the PyMuPDF library (fitz) to iterate through pages and identify image objects (page.get\_images()).
- Image saving: Each extracted image (above a minimal size threshold to filter decorative elements) is saved as a separate file (e.g., PNG, JPG) into a dedicated subdirectory: output\_files/…/images/{doc\_id}/{image\_filename}.
- Metadata indexing: For each document containing images, a JSON file ({doc\_id}\_image\_index.json) is created in the image subdirectory. This index stores metadata for each extracted image, including its filename, page number, bounding box coordinates, and a rudimentary caption automatically generated by extracting nearby text from the PDF page. This index is crucial for later retrieval.

## D. Vector Storage and Hybrid Retrieval

Processed text chunks are vectorized and stored using ChromaDB, managed by the VectorDB class.

- Embedding: Text of each chunk is embedded by OpenAI's text-embedding-3-large model via chromadb.utils.embedding\_functions.OpenAIEmbeddingFunction.
- Storage: Embeddings along with metadata (including chunk\_id, doc\_id, knowledge\_id, keywords, source\_file, token\_count) are added to a ChromaDB collection specific to the chatbot\_id. We use cosine similarity as the distance metric.
- Hybrid retrieval capability: The VectorDB class provides methods for both semantic similarity search (get\_similar\_semantic, using ChromaDB's native query) and keyword-based search (get\_similar\_keyword, using Jaccard similarity on TF-IDF keywords). The main query logic (in Debug.retrieve\_data &amp; /vectorsearch/retrieve) combines results from these methods based on the configured search\_weight ('Semantic', 'Keyword', or 'Mixed'), implementing the hybrid strategy. The final set of chunks is filtered based on the knowledge\_relevance score threshold.

## E. Multimodal Retrieval and Prompting

When a user query is submitted (/query/submit), the system performs multimodal retrieval.

- Text chunk retrieval: Relevant text chunks are retrieved from ChromaDB using the strategy outlined in III-D.
- Image retrieval: The ImageRetriever class identifies the doc\_ids present in the retrieved text chunks. It then loads the corresponding image\_index.json files and calculates a relevance score between the user query and each image's stored caption (\_calculate\_image\_relevance). The metadata of the top-scoring images (up to a limit) are selected.
- Prompt construction: The construct\_rag\_prompt method formats the final prompt for the LLM (
</CONTENT>