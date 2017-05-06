---
layout: post
title: "A regulatory scheme for a synthetic cell."
date: "2017-01-27 16:16:43 -0800"
---

Been trying to decide what aspect of Build a cell I'd most like to focus my PhD on. My current thinking is:

# Defined and extensible regulatory systems for synthetic genomes.
The fundamental question I’m asking is what does the regulatory framework look like for Build a Cell. How do we control expression of functional modules, and how do we define and control the relationships between them. The question was partially inspired by Yan 2010, the paper that compared the E. coli regulatory network to the linux call stack. I would expect to do a survey of what we know about existing regulatory mechanisms in prokaryotic and eukaryotic organisms, followed by what is possible with engineered synthetic regulation (for example, using CRISPR/dCas9 to regulate cassettes). The final output would comprise an engineer able and understandable design for regulation of all the components in the genome, validated against a set of modules we’ve developed. I could anticipate this including computational design tools for building a regulatory topology, compiling it down to DNA, as well as modelling the output. It could also include a module design spec (a-la BBF all-stars) to specify functional modules and insulate them so that they can be integrated into the regulatory system without unpredictable effects.

Spoke to Drew today and collected some thoughts:
* Need a way to test and optimise designs; preferably select for them
* Best next step is to identify multiple axes of control in living systems. For example, volatile--non-volatile (require active maintenance), and essential--non-essential (required for life). Once these axes are determined we can identify test-case modules that occupy each quadrant of the grid and determine what regulatory systems are required for them. The needs-finding for how the regulatory system will behave will come from the design and construction of these modules.
* We also want to take the opportunity to identify which components of natural regulatory schemes facilitate which 'characteristic timescales' of life: immediate functionality; adaptation or learning over the life of the organism; and evolution.
