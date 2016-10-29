---
layout: post
title:  "CRISPRi Knockdown System"
date:   2016-10-28 13:57:24
categories: devtools crispri
---

# Introduction
In order to rapidly test functional modules in a running cell, we developed a CRISPRi-based knockdown system based on dCas9 (cite) and CRISPathBrick (cite). The system allows for the rapid construction of knockdown cassettes for one or more genes, and testing for both knockdown and complementation.

# Validation Experiments

## Histidine Knockdown

We constructed a protospacer to knockdown the histidine biosynthetic pathway by targeting the [HisBHAFI operon](http://ecocyc.org/ECOLI/NEW-IMAGE?type=NIL&object=TU0-6650&redirect=T). The CRISPRi construct was transformed into *E. coli* MG1655, which were grown in LB, minimal media, and minimal media supplemented with histidine. Optical density was measured over 36 hours.

![Histidine Knockdown]({{ site.url + site.baseurl }}/images/HisKDExp1.png)

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