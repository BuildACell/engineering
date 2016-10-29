---
layout: post
title:  "Containers"
date:   2016-10-28 13:57:24
categories: containers
---

Containers are membrane-bound vesicles that contain cellular elements (e.g., polymerases, ribosomes, amino acids) in proportions expected in a typical prokaryote, but lack a genome. We hypothesize that the introduction of the biokernel (or any synthetic genome) into a container would recapitulate typical cellular activity.

We are developing two types of containers from E. coli: [Minicells](http://buildacell.io/engineering/minicells/2016/10/28/containers-minicells.html) (strain DS410) and [E-CRISPie cells]() (strain MG1655 + DNAi).

Minicells are small genome-less progeny of E. coli, approximately 10% the volume of E. coli, that bleb off during asymmetric division of E. coli strains that either have a mutation in the min system (DS410) or are overexpressing ftsZ. These minicell containers cease to grow and divide, whereas their parent cells continue to produce clonal progeny as well as additional minicells.

E-CRISPie cells are containers formed by irreparably fragmenting the genome of E. coli using Type I-E CRISPR/Cas3. We have found that fragmenting the native E. coli genome leads to a potentially undesirable activation of the E. coli SOS response and subsequent noodle-like filamentation of the cell as seen in the image above. We are working to downregulate the SOS response and maintain an E-CRISPie container into which a new genome could be transplanted.


[^1]: Footnote one
