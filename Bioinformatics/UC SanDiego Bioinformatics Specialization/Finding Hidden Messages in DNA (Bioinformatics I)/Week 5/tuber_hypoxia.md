
# Project: Hypoxia Transcription Sites
![Placeholder Image 1](8436_lores.jpg "At a magnification of 13172x, this scanning electron micrograph (SEM) depicted a number of Gram-positive Mycobacterium tuberculosis bacteria.")

## Table of Contents
1. [Introduction](#introduction)
2. [Aim of the Project](#aim-of-the-project)
3. [Scope](#scope)
4. [Problem Statement](#problem-statement)
5. [Methodology](#methodology)
6. [Data Collection](#data-collection)
7. [Analysis](#analysis)
8. [Conclusion](#conclusion)
9. [References](#references)

## Introduction
**Mycobacterium tuberculosis (MTB)** can persist in a latent state in humans for many years before causing disease. Latency has been found to be linked to hypoxia (lack  of oxygen) in the host. We suspect that genes that are activated in  hypoxia are regulated by a common transcription factor. We have access to the upstream sequences of MTB genes upregulated in hypoxia, and our objective is to identify the motif representing the binding site for the transcription factor that regulates these genes.

## Aim of the Project
The aim of this project is to investigate the effects of climate change on biodiversity in a specific region. We will analyze historical climate data and biodiversity indicators to assess trends and identify potential correlations.

## Scope
This project will focus on a selected geographical area known for its rich biodiversity. We will examine changes in temperature, precipitation patterns, and other climatic factors over the past few decades. Additionally, we will assess the impact of these changes on species abundance, distribution, and habitat suitability.

## Problem Statement
Climate change poses a significant threat to biodiversity, leading to shifts in ecosystems, loss of habitat, and decline in species populations. By studying the relationship between climate variables and biodiversity indicators, we aim to gain insights into the drivers of ecological change and inform conservation efforts.

## Methodology
1. Data collection: Gather historical climate data from reliable sources such as meteorological stations and satellite observations. Obtain biodiversity data from field surveys, research databases, and species distribution models.
2. Analysis: 
3. Modeling: Develop predictive models to project future climate scenarios and their impact on biodiversity. Assess the vulnerability of species and ecosystems to climate change.
4. Interpretation: Interpret the findings in the context of existing scientific literature and theoretical frameworks. Discuss implications for conservation policy and management strategies.

## Data Collection
- Climate data: Monthly temperature, precipitation, humidity, and other climatic variables.
- Biodiversity data: Species richness, abundance, distribution maps, habitat characteristics.

## Analysis
### Upstream 250 bp regions: 
The dataset "upstream250.txt" underwent analysis with a minimum and maximum motif length set at 20, facilitating the visualization of motif occurrences within each sequence contained in the file. The graphical representation below illustrates the motif derived from the analysis. A consensus sequence comprises a string of nucleotide or protein characters, augmented by "degenerate characters" that indicate a subset of potential characters. These degenerate characters function as "wild cards," with 'N', for instance, representing any character in the sequence.

![AGGGSCGWARGTCCYCAABB](AGGGSCGWARGTCCYCAABB.png "Consensus motif from upstream250 with motif of length 20")

Motif occurrences were observed at multiple positions along the DNA sequences, with a predominant trend indicating their prevalence beyond the 114th position, predominantly favoring the right side of the DNA sequence. Selected instances of motif positions are visually depicted below for reference.

![meme-motif-locations250](meme-motif-locations250.svg "Motif locations in upstream250")


The dataset was reanalyzed with a minimum motif length of 6 and a maximum of 20 to investigate the influence of motif size on the identification of binding site locations. 

![HAGGGVCRDAAGTCCYYARY](HAGGGVCRDAAGTCCYYARY.png "Consensus motif from upstream250 with motif of length 6/20")

Motif occurrences were observed to be consistently located downstream, as anticipated, with sequences predominantly found towards the right of the sequence. Notably, the motif size appeared to have minimal impact on this observed pattern.

![meme-motif-locations250620](meme-motif-locations250620.svg "Motif locations in upstream250")

### Comparing motif logs from the same datasets with different critera
An analysis was conducted on the 250 bp upstream regions of a sequence, generating two motif logos. One logo was generated with a fixed motif size of 20, while for the other logo, the motif size was allowed to vary within a range of 6 to 20, inclusive. Surprisingly, both analyses yielded motifs of size 20. Upon juxtaposing the logos a striking similarity was observed.

To elucidate the disparities between these strings, we can consult the table:

| Symbol | Meaning              | Mnemonic                                |
|--------|----------------------|-----------------------------------------|
| R      | A, G                 | puRine                                  |
| Y      | C, T                 | pYrimidine                              |
| W      | A, T                 | Weak (weaker basepairs, fewer hydrogen bonds) |
| S      | G, C                 | Strong (stronger basepairs, more hydrogen bonds) |
| K      | G or T               | Keto (both have a keto group)           |
| M      | A or C               | aMine (both have an amine group)        |
| B      | C, G, T              | not A (B comes after A)                 |
| D      | A, G, T              | not C (D comes after C)                 |
| H      | A, C, T              | not G (H comes after G)                 |
| V      | A, C, G              | not T or U (V comes after T and U)      |
| N      | A, C, G, T           | aNy base                                |


**AGGGSCGWARGTCCYCAABB**
![AGGGSCGWARGTCCYCAABB](AGGGSCGWARGTCCYCAABB.png "Consensus motif from upstream250 with motif of length 20") 

**HAGGGVCRDAAGTCCYYARY**
![HAGGGVCRDAAGTCCYYARY](HAGGGVCRDAAGTCCYYARY.png "Consensus motif from upstream250 with motif of length 6/20")

### Comparing motif logos from different upstream sections of the sequence

**TMCGCCCMHKCVANGRRGAY**
![TMCGCCCMHKCVANGRRGAY](TMCGCCCMHKCVANGRRGAY_25.png "Consensus motif from upstream25 with motif of length 20") 

**CVRYTRGGGACYDWMGBCCC**
![AGGGSCGWARGTCCYCAABB](CVRYTRGGGACYDWMGBCCC_100.png "Consensus motif from upstream100 with motif of length 20") 

**GBTRGGGMCNRAMGTCCCCN**
![GBTRGGGMCNRAMGTCCCCN](GBTRGGGMCNRAMGTCCCCN_1000.png "Consensus motif from upstream1000 with motif of length 20") 

## Conclusion
There are several conclusions we can come to based on the study.

## References
- https://www.coursera.org/learn/dna-analysis/peer/NLcAJ/bioinformatics-application-challenge
- 8436_lores.jpg from https://www.cdc.gov/vaccines/vpd/tb/public/photos.html
- Timothy L. Bailey and Charles Elkan, "Fitting a mixture model by expectation maximization to discover motifs in biopolymers", Proceedings of the Second International Conference on Intelligent Systems for Molecular Biology, pp. 28-36, AAAI Press, Menlo Park, California, 1994. [full text]

## Images
Insert images related to the project here:

![Placeholder Image 1](image1.jpg "Description of Image 1")
![Placeholder Image 2](image2.png "Description of Image 2")
