# Ensembl REST API — Genomic Variant Annotation Tool

## Overview

This project was created as a personal development piece to improve my understanding of APIs in the context of genomic medicine.

Application Programming Interfaces (APIs) operate via a client sending a request to a server, and the server returning requested data. This is extremely useful in bioinformatics where there are multiple online databases that contain large amounts of genomic data that cannot simply be copied or downloaded locally.

APIs operate on CRUD (Create, Read, Update, Delete) methods. Requests and responses are typically handled using JSON, which means the server can process the request regardless of what language the backend was built on.

---

## Ensembl REST API

Ensembl uses a REST API — a simple, lightweight method of transferring data over HTTP. The Ensembl REST API provides programmatic access to one of the most comprehensive genomic databases available, covering variant annotation, gene lookup, phenotype associations, and more.

Full documentation: https://rest.ensembl.org

---

## The `query_ensembl` Function

All requests are handled through a single reusable function — `query_ensembl(ext, on)` — rather than writing separate functions for each endpoint. This keeps the code clean and means any new Ensembl extension can be added without restructuring the codebase.

### Parameters

| Parameter | Description |
|-----------|-------------|
| `ext` | The Ensembl API extension (endpoint). Determines what type of data is being requested. |
| `on` | The identifier being queried — e.g. a variant in HGVS notation, a gene ID, or a transcript ID. This will vary depending on the extension used. |

### Supported Extensions

| Variable | Endpoint | Description |
|----------|----------|-------------|
| `lookup` | `lookup/id/` | Find species and database information for a single identifier such as a gene, transcript, or protein. |
| `VEP` | `vep/human/hgvs/` | Fetch variant consequences based on HGVS notation. Returns transcript-level consequences, pathogenicity scores, and colocated variant data. |
| `phenotype` | `/phenotype/gene/human/` | Return phenotype annotations associated with a given gene

---

## Features

### VEP Variant Annotation
Queries the Ensembl Variant Effect Predictor (VEP) with additional plugins enabled:

- **CADD** — Combined Annotation Dependent Depletion score, a measure of variant deleteriousness
- **Conservation** — Evolutionary conservation score at the variant position
- **AlphaMissense** — Deep learning-based missense pathogenicity prediction
- **REVEL** — Rare Exome Variant Ensemble Learner score

The function optionally filters results to the **canonical transcript** only — the single Ensembl-designated representative transcript for a gene — avoiding the noise of duplicate scores across all overlapping transcripts.

### Phenotype Lookup
Returns all phenotype associations for a given gene. Supports **case-insensitive keyword filtering** on the description field, so results can be narrowed to a specific disease or condition without needing an exact match.

---

## Dependencies

```
requests
pprint - highly recommend using this as Ensembl returns nested JSON data that can be hard to read
```

## Usage Examples
I used the gene HNF1A as an example to test this function.

```python
# Gene lookup
gene = query_ensembl(lookup, "ENSG00000135100")

# VEP variant annotation (with canonical transcript filtering)
variant = query_ensembl(VEP, "ENST00000257555:c.544C>T")

# Phenotype lookup (with keyword filtering)
phenotypes = query_ensembl(phenotype, "ENSG00000135100")
```

---

## What I Learned

- How to authenticate and interact with a public REST API using the `requests` library
- How to parse and navigate deeply nested JSON structures using  `.get()`, and list comprehensions
- How genomic databases structure variant data — separating top-level variant fields, colocated variant data, and per-transcript consequences
- Why filtering to the canonical transcript matters clinically, and how Ensembl flags it in the response
- How to write a single flexible function that handles multiple endpoints cleanly rather than duplicating logic
- The difference between gene-level and variant-level phenotype data, and the limitations of each

---