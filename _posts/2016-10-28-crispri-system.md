---
layout: post
title: "CRISPRi Knockdown System"
---

# Introduction

![Blockdiagram]({{ site.url }}/engineering/images/Fig4_CRISPRiBlock.png)

![Partsdiagram]({{ site.url }}/engineering/images/Fig4_CRISPRiParts.png)

In order to rapidly test functional modules in a running cell, we developed a CRISPRi-based knockdown system based on dCas9 (cite) and CRISPathBrick (cite). The system allows for the rapid construction of knockdown cassettes for one or more genes, and testing for both knockdown and complementation.

# Design

# Validation Experiments

## Histidine Knockdown

We constructed a protospacer to knockdown the histidine biosynthetic pathway by targeting the [HisBHAFI operon](http://ecocyc.org/ECOLI/NEW-IMAGE?type=NIL&object=TU0-6650&redirect=T). The CRISPRi construct was transformed into *E. coli* MG1655, which were grown in LB, minimal media, and minimal media supplemented with histidine. Optical density was measured over 36 hours. Points are mean over 12 replicates; error bars are standard error.

![Histidine Knockdown]({{ site.url }}/engineering/images/HisKDExp1.png)

| Sample | Media | KD |
| ------ | ----- | --------------------- |
| LB.NP  | LB    |                       |
| LB.P   | LB    | Y                     |
| Aux.NP | Minimal    | |
| Aux.P  | Minimal    | Y|
| His.NP  | Minimal + His    | |
| His.P  | Minimal + His    | Y|
| His2.NP  | Minimal + His    | |
| His2.P  | Minimal + His    | Y|