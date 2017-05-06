---
layout: page
title: Organism Breadboard
---

The Organism Breadboard is a computational toolset being developed to interpret dependencies between genes and enable unit-testing of gene function in both existing and forward engineered genomes. The near-term goal is to mine prokaryotic genome information from curated databases like Ecocyc and Kegg and provide ranked lists of all possible candidate protospacers for CRISPRi knockdown (for unit-testing). The current version provides an interface with Ecocyc, extracts a not-yet complete list of E. coli annotations, and generates a [spreadsheet](https://github.com/EndyLab/Gene-Mining-Scripts/blob/master/CRISPRiTargets.csv) consisting of:

1. Promoter ID
2. Promoter orientation
3. Sequence surrounding promoters (specifiable)
4. Genes in each operon (one operon per promoter)
5. Transcription unit ID (one or greater transcription units per promoter)
6. Positive and negative strand protospacer candidates targeting the sequence surrounding promoters

## Current capacities
* 2152 annotated genes from E. coli integrated (out of expected 4377 in E. coli K-12)
* 3841 promoters (operons) from E. coli accounted for
* 7 protospacers identified per promoter region on average (searching from 60 bps upstream to 60 bps downstream of +1)

## Installation
Simply download OrganismBreadBoard.09-a4:
[https://github.com/EndyLab/Gene-Mining-Scripts.git](https://github.com/EndyLab/Gene-Mining-Scripts.git)

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request!
