---
layout: page
title: CRISPRi Based Pathway Knockdown
mainmenu: true
weight: 5
---

## What
A CRISPRi tool for knockdown based module development. 

![Blockdiagram](/engineering/images/Fig4_CRISPRiBlock.png)

![Partsdiagram](/engineering/images/Fig4_CRISPRiParts.png)

## Why
Instead of complete removal, it may be useful to be able to knockdown the function of a part, device, circuit or module in a genome.

## How
Clustered Regularly Interspaced Short Palindromic Repeats Inhibition (CRISPRi) -based system coupled with CRISPathBrick arrays. 

## What Is Success
A versatile platform for knockdown-based development.

---
### Work In Progress

#### Histidine Knockdown

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




