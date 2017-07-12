---
layout: page
title: BioKernel
weight: 5
---

# Introduction

<img class="biokernel-figure" src="/engineering/images/BioKernel.png">

The BioKernel is a set of genes and biomolecules defined at single-molecule resolution that when organized appropriately lead to a functioning, modellable, and understandable cell. It will possess the core components and functions necessary for an organism, and be developed in a manner amenable to the distributed construction of arbitrary organisms of desired function. For such a goal to be achieved, we believe the BioKernel will require a set of genes encoding a cell in which all biomolecules that are produced are accounted for, an operational understanding of the functionality of each biomolecule, and a comprehensive model of their abundances and locations and interactions over time.

# Contents

* [What is the strategy for developing the BioKernel?](#what-is-the-strategy-for-developing-the-biokernel)
* [How can the biokernel be collaboratively developed?](#how-can-the-biokernel-be-collaboratively-developed)
* [What is PURE?](#what-is-pure)
* [What are the advantages of building out from PURE?](#what-are-the-advantages-of-building-out-from-pure)
* [What is the first module being developed?](#what-is-the-first-module-being-developed)
* [What are the tools necessary to build out the biokernel?](#what-are-the-tools-necessary-to-build-out-the-biokernel)
* [How can I learn more?/How can I contribute?](http://buildacell-invite.herokuapp.com/)

# What is the strategy for developing the biokernel?

<img class="biokernel-figure" src="/engineering/images/Approach.png">


 Construction of a semi-synthetic cell, or the design of a synthetic genome encoding and operating within single-molecule resolution defined biomolecules derived from natural organisms, is the most technically approachable path towards the goal of a understandable cell.


<img class="biokernel-figure" src="/engineering/images/in vitro.png">

 The prototyping platform to validate modules involves the design of chosen genes encoding the production of biomolecules to perform functions, building and integrating those genetic constructs and reconstituted cytosol, and testing them in a defined background while taking the requisite measurements to inform the next design cycle.


# How can the biokernel be collaboratively developed?

Once separate groups have made the decision to collaborate, the transaction cost for working together can be minimized through two benchmarks.

<img class="biokernel-figure" src="/engineering/images/Distribution.png">

<strong>Distributed Development: </strong>The forward engineering of an entire genome provides opportunity for modularization and distributed development across multiple individuals and labs.

<img class="biokernel-figure" src="/engineering/images/Standards.png">

<strong>Standardization and Reproducibility: </strong>The testing of designs within the background of an ensemble of defined molecular components that is also accessible promotes communication and reproducibility of results for communal development.


# What is PURE?

PURE is a reconstituted expression system (mostly from E. coli) developed by <a href="http://www.nature.com/nbt/journal/v19/n8/full/nbt0801_751.html">Ueda et al. in 2001</a>. It contains all the purified components required to generate a polypeptide sequence from a DNA template. Its composition provides a <strong>defined</strong> background to drive consistent expression and can be used as the fundamental basis for building out into a understandable cell.

<img class="biokernel-figure" src="/engineering/images/PUREdata.png">


# What are the advantages of building out from PURE?

There are four distinct advantages for using PURE to build a cell.

<img class="biokernel-figure" src="/engineering/images/One.png">

Constructs can be measured and prototyped on the same time order of the biochemical reactions taking place (no need to wait for cells to grow!).

<img class="biokernel-figure" src="/engineering/images/Two.png">

The reconstituted cytosol can be defined to your choosing enabling quantification of perturbations and changes that occur through tuning of the collections of biomolecules.

<img class="biokernel-figure" src="/engineering/images/Three.png">

Collections of genes can be measured to confirm that the biomolecules expressed perform their predicted function.

<img class="biokernel-figure" src="/engineering/images/Four.png">

If the molecule to perform a specific biochemical function is unknown, then systematic screens can be used to discover genes that perform unknown functions.


The major drawback of PURE (aside from cost) is that what you prototype in PURE has a risk of not working in another in vitro or in vivo context. Thus it is highly advisable to build out of the same context as the testbed - build out a cell from defined reconstituted biomolecules expressing a synthetic genome.


# What is the first module being developed?

Several different functional modules will be required to build up a cell, including growth, division, and replication of its genome.

<img class="biokernel-figure" src="/engineering/images/CDog.png">

One fundamental aspect is for the cell to internally replicate and regenerate all of the components necessary for gene expression. Stated differently, what is the DNA that when expressed in an expression system remakes said expression system? Working through a way to re-create a defined purified reconstituted expression is a tractable approach for answering this question.

<img class="biokernel-figure" src="/engineering/images/CDogGenes.png">

The genes necessary to form a regenerative central dogma can be categorized in four ways: 1) Enzymes encoded by 1 or a few genes (RNAP, tRNA synthetases, translation factors) 2) Genes required for tRNA biogenesis 3) Genes required for ribosome biogenesis 4) Genes required to facilitate expression of all the above (chaperones, assembly factors).

Our belief is that successfully building out central dogma would be a key hallmark for the realization of building a molecularly defined cell. Achieving this would also greatly augment the ability for workers on synthetic cells to improve their own design and open the possibility of other cellular functions to be pursued.


# What are the tools necessary to build out the biokernel?

The following are a set of tools that are essential to engineering a molecularly defined understandable cell. All these tools are/will be made available to anyone who wishes to use them for purposes of collaboration or using for their own work.

<img class="biokernel-figure" src="/engineering/images/DevKit.png">

Join the [Build-A-Cell Slack](http://buildacell-invite.herokuapp.com/)
