---
layout: post
title:  "Minicells"
date:   2016-10-28 17:00:00
categories: minicells
---

Minicells

![minicellpic]({{ site.url }}/engineering/images/Fig2b_Minicells.PNG)

<video id="minicellsmov" width="503" height="492" preload controls>
	<source src="{{ site.url }}/engineering/images/BF.mp4" type = "video/mp4">
</video>


We currently produce minicells from two strains of *E. coli*: [χ1411](http://cgsc.biology.yale.edu/Strain.php?ID=9702) and [DS410](http://cgsc.biology.yale.edu/Strain.php?ID=12920). We wish to estimate three kinds of quantitative information for the minicells: descriptive information, such as cell size and morphology; starting condition, the cellular resources available immediately after the minicell has budded off from the host cell; and total capacity, upper limits on a minicell due to attributes such as size. For example, upon budding a minicell may only have a certain quantity of free amino acids available in the cytosol (starting condition), while its maximum DNA content is constrained by how much DNA can be physically packed within its volume (total capacity). For several variables, we estimate both a hard upper limit, as well as a 'biologically reasonable' limit based on the relevant values for other organisms.	

The full analysis can be downloaded directly from the [github repository](https://github.com/BuildACell/engineering/blob/master/notebooks/minicell-key-numbers.ipynb).

| Attribute | Estimate | Unit |
|:--------- | --------:|:---- |
| *Morphology* |||
| Diameter | $$0.44$$ | $$\si{\um}$$ |
| Surface Area | $$0.55$$ | $$\si{\um}^2$$
| Volume | $$0.039$$ | $$\si{\um}^3$$
||||
| *Atoms* ||| 
| Hydrogen | $$3.2 \times 10^7$$ |   
| Carbon | $$1.8 \times 10^{7}$$ |  
| Oxygen | $$9.2 \times 10^6$$ |  
| Nitrogen | $$4.6 \times 10^6$$ |  
| Total[^rounding] | $$6.5 \times 10^7$$ | 
||||
| *Central Dogma* |||
| DNA capacity | $$150$$--$$1500$$ | kbp 
| Available nucleotides[^estnuc] | $$1 \times 10^6 $$| nt 
| Available amino acids[^totalaa] | $$5.6 \times 10^7$$--$$25 \times 10^7$$| aa 
| RNA synthesis capacity[^trslength] | $$100$$--$$39000$$ | transcripts 
| Protein synthesis capacity[^estprotlen] | $$1.9 \times 10^5$$--$$8.3 \times 10^5$$ | proteins 
||||
| *Macromolecules* |||
| RNA polymerase | $$250$$--$$2500$$ | 
| Ribosomes | $$680$$--$$7200$$ |
||||

[^rounding]: Numbers do not add to total due to rounding.
[^trslength]: Based on a transcript length of 1000 nucleotides. The low estimate is a proportional conversion from order 1000 transcripts in *E. coli*; the high estimate represents maximum transcript capacity if every nucleotide is used for mRNA.
[^estnuc]: Based on total estimated nucleotide content of the minicell.
[^totalaa]: Total amino acid content.
[^estprotlen]: Based on average protein length of 333 amino acids.
