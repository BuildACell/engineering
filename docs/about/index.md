---
layout: page
title: About
permalink: /about/
mainmenu: true
weight: 1
published: true
---


We are building a cell, but we are not alone. Researchers around the world are actively working on projects with similar goals, albeit different approaches. There are groups working to build cells from the bottom-up, chemically synthesizing the constituent parts and combining them in such a way that my elucidate the fundamental physical mechanisms that result in a self-assembling cellular system. Other groups are working to construct a minimal genome by iteratively removing genes from a host genome until they have reached a subset of essential genes for growth and replication. The Build-A-Cell project combines the best parts of both approaches in an open and distributed way.  
 
![Motivations for project](/engineering/images/Figure1-Approaches.png)

**Top-down approach**: Starting from entire existing genomes, genes are systematically removed and the genome is refactored until a cell with 
some minimal subset of components is created. The goal is to progressively obtain a deeper understanding of cells by characterizing essential 
components that remain. While this method could quickly provide an engineering platform, maximum potential knowledge gained is limited by a 
lack of first-principles design exploration.

**Bottom-up approach**: Starting from first principles, atoms or small groups of atoms (molecules) are put together in an intentional manner 
to create a protocell. The goal is to create a cellular recipe of well-characterized, essential components. While this method would likely 
lead to the most powerful understanding of cells, current technologies do not provide sufficient engineering capabilities and are slow to 
scale.

**Build a cell approach**: A top-down approach is taken to obtain a genome-less container while a bottom-up approach is taken to design 
lineage-agnostic genomes. Combining the two paradigms enables the design and understanding of genomes from first-principles without 
simultaneous concern for the remaining cellular components needed to instantiate the genome. Inspired by the [Unix Philosophy](/engineering/about/unix-philosophy/), we aim to build an open and understandable platform for cell engineering.
