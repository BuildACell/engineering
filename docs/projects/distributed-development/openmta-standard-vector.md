---
layout: page
title: OpenMTA Standard Vector
---

# Introduction

As we synthesize genes for distribution under the [OpenMTA](http://openmta.org/), we will need an easy, effective and open-source means to distribute them. We have designed the first version of a standardized shipping vector for OpenMTA licensed genes, which will also be synthesized from scratch. The vector allows for straightforward and high efficiency cloning, easy expression of payload genes, and facilitates storage and shipping without a cold chain.

# Feature List
* Storage in B.subtilis spores
* Orthogonal antibiotic resistance marker from the "big 5"
* ColE1 origin
* Negative screening on insert using color
* T7 expression system
* Compatible with GoldenGate cloning
* Compatible with BioBrick assembly
* Standard sequencing primer binding sites
* Transcriptional isolation

# Design

## Design Criteria
The design of the Open MTA shipping plasmid takes into account a number of considerations:
* Free for open source distribution, unencumbered by patents or non-open material transfer agreements (MTAs).
* Useful for broad distribution among biology practitioners including academic labs, industry, DIYbio and community labs, and individuals.
  * Cheap and easy to produce in quantity and store for later distribution.
  * Cheap and easy to ship.
* Make downstream use of distributed constructs as easy and effective as possible:
  * Support a variety of standard methods for cloning, extracting and using constructs.
  * Particular focus on lower-cost and higher-throughput technologies.
* Make received DNA immediately useful:
  * Fast sub-cloning.
  * Easy basic expression of coding constructs.

## Core Plasmid
### ColE1 origin of replication
For the vast majority of parts, the ColE1 origin works well. Since it has extremely wide adoption, users should be able to use pre-existing protocols with these plasmids. If it is truly required that a lower copy plasmid be available for toxic parts that can't be transcriptionally isolated, one can be synthesized for that purpose.

### *Bacillus subtilis* origin of replication
This portion of the plasmid codes for a theta origin of replication in *Bacillus subtilis*[^1].  This theta replication plasmid is stable unlike typical rolling cycle replication plasmids, however, it requires a replication protein. This replication protein, called repA, will be coded for on the main *B. subtilis* genome.

### Gentamicin resistance
The plasmid confers gentamicin resistance for selection, allowing for co-transformation with plasmids which use the "big 5" (ampicillin, kanamycin, chloramphenicol, tetracycline, spectinomycin). This orthogonality ensures efficient marker switching for GoldenGate in a way that is compatible with all current marker systems. The antibiotic is inexpensive and works in both gram-positive and gram-negative bacteria, facilitating both normal cloning workflows and *B. subtilis* distribution.

Resistance is conferred by the AAC(3)-I enzyme[^2], as this enzyme has limited cross resistance and is not part of the APH family of resistance enzymes, which are all closely related. To get proper expression in both gram-positive and gram-negative cells, the apramycin promoter was taken from the pCRISPomyces-2 plasmid[^3].

### Standard sequencing primer binding sites
Flanking the gene payload site are the M13-forward and M13-reverse primer-binding sequences. This allows PCR and sequencing of assembled or received vectors using primers that are in general already available within laboratories. A number of DNA sequencing providers already stock these primers, increasing ease of sequencing.

## Assembly and Cloning
### Negative screening mechanism
We provide negative screening for successful cloning using green fluorescent protein[^4], a strong tac promoter, and a strong RBS. Successful cloning into the payload site by one of the supported assembly mechanisms will be indicated by a loss of fluorescence in the colony. The patent has expired[^5].

### Gene integration for distribution
The plasmid supports easy integration of gene coding sequences for distribution and expression, using Golden Gate assembly. Digestion of the plasmid with the restriction enzyme BtgZI produces

### MoClo compatible gene excise for subcloning
Digestion of the plasmid with BsaI frees the gene payload with MoClo level zero-compatible overhangs, corresponding to the signal peptide—coding sequence pair: AATG-CDS-GCTT. The excised linear DNA runs from the start codon of the gene with one additional leader nucleotide (a ATG) to seven nucleotides downstream of the stop codon (NNN TGA aga gctt). This allows a fully functioning CDS to be immediately assembled into an expression vector, while also supporting assembly into a fusion protein or purification construct (see [x]), at the cost of introducing a seven-nucleotide scar in the 3' UTR.

### SapI gene excise for assembly into fusion and purification constructs
Digestion of the plasmid with SapI eliminates the 3' UTR of the payload gene, leaving a three-nucleotide overhang aligned on the final amino acid-coding codon (NNN NNN). This facilitates enzymatic assembly of the coding sequence with 3' protein components, such as linkers, fusions, and purification tags. This assembly can proceed inside the standard vector, by inserting a new 3' coding sequence, or by cloning the coding sequence into a new vector using a multi-enzyme digest with BsaI (5' MoClo adapter) and SapI (3' codon overhang).

### BioBricks compatible restriction sites
The gene payload site is flanked by BioBrick RFC10 standard prefix and suffix sequences. This facilitates integration of pre-existing BioBricks-compatible parts, as well as extraction of a payload gene for assembly into a compatible plasmid. At this time we do not require parts shipping in the standard vector to meet full RFC 10 specifications (excluding illegal restriction sites, for instace). Rather, RFC 10 compatibility may be provided as a option for a given gene.

## Expression System
### T7 expression
Although the standard vector is primarily designed for distribution, gene payloads are flanked by the T7 promoter and terminator to allow easy expression of a gene construct upon receipt. The plasmid can be purified and transformed into a production strain containing T7 polymerase, and the gene of interest will be expressed.

We have two competing designs for the 5' T7 promoter / RBS construct:
* Simple: one selected RBS which works in general, but which may not work for a number of specific genes due to 5' secondary structure formation.
* RBS-free: the vector excludes a ribosome binding site, and we expect that an RBS compatible with a specific gene will be included upon insertion into the vector either through a multi-segment Golden Gate assembly, or by synthesizing a compatible 5' UTR alongside the coding gene sequence.
* Bi-cistronic design (BCD): the expression construct contains a 5' BCD[^6]. Every inserted gene is expressed at the same nominal level.

# Open Design Questions

* 5' expression design (see above)
* 3' cloning design: is the SapI / BsaI hybrid system the best choice?
* Should full RFC 10 compliance be required for payload genes? We could required it an more significantly constrain sequences, or just make it an option: for shipping pre-existing RFC 10 parts, for instance.
* Screening marker: what colorimetric, fluorescent, or other marker do we want to use to identify correctly assembled vector constructs?
  * BioBricks FFP collection JuniperGFP
  * Now out-of-patent original GFP
  * Some chromoprotein
  * Something else.
* Do we have the right antibiotic resistance?

Any and all feedback will be taken into consideration!

# Map

![pOpenMTA Plasmid Map](https://github.com/BuildACell/engineering/blob/master/distributed-development/openmta-vectors/pOpenMTA v1 map.png?raw=true)
# Use

Please see the [Assembly Strategy](/engineering/project/distributed-development/openmta-assembly-strategy.html)

## References
[^1]: "The replicative polymerases PolC and DnaE are required for theta replication of the Bacillus subtilis plasmid pBS72", http://www.microbiologyresearch.org/docserver/fulltext/micro/152/5/1471.pdf

[^2]: "Molecular genetics of aminoglycoside resistance genes and familial relationships of the aminoglycoside-modifying enzymes." https://www.ncbi.nlm.nih.gov/pubmed/8385262

[^3]: "pCRISPomyces-2", https://www.addgene.org/61737/

[^4]: "GFP", http://www.uniprot.org/uniprot/P42212

[^5]: "Green fluorescent protein" https://www.google.com/patents/US6146826

[^6]: Mutalik, Vivek K., et al. "Precise and reliable gene expression via standard transcription and translation initiation elements." Nature methods 10.4 (2013): 354-360. https://www.nature.com/nmeth/journal/v10/n4/full/nmeth.2404.html
