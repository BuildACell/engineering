---
layout: post
title:  "Development Kit v0.1: Introduction"
---

Building the biokernel requires three major components: **architecture**, the design for and of an effective engineerable cell, its subsystems, and their means of interaction; **implementation**, fabrication of the design as DNA and its introduction into a container; and **development tools**, the new tooling required for rapid and effective work on the other two. In order to begin the process, we have determined that several key tools are critical to guide design, test implementation and evaluate ideas. Specifically, we want to develop modules to provide core cell capabilities. 

The first version of our development kit comprises three tools:

- A [container](/engineering{% post_url 2016-10-28-containers %}), based on E coli [minicells](/engineering{% post_url 2016-10-28-containers-minicells %}), for testing constructs in a genome-free context.
- A easy-to-use knockdown system based on [CRISPRi](/engineering{% post_url 2016-10-28-crispri-system %}), to target any gene, functional operon, or pathway, so that constructs designed to implement the targeted function can be tested in the context of an otherwise-functional growing cell system.
- [Computational tools](/engineering{% post_url 2016-10-28-organism-breadboard %}) to identify pathways and genes related to a function, design knockdown constructs, and identify components useful for implementing a function from across the domains of life.

Our expected workflow is as follows:

* Select a cellular function for which to design a module. For example, histidine biosynthesis.
* Using computational tools, identify the pathway and the genes or operons corresponding to the function.
* Design knockdown cassettes to eliminate the native pathway function in a test E coli chassis.
* Using computational tools, identify potential components for a replacement design. For example, histidine biosynthesis could be reconstituted using the E coli His operons, equivalent synthesis pathway coding cassettes from other species, or by expression of an active histidine transporter.
* Design and construct the complementation, or saviour module.
* Transform both the CRISPRi and saviour modules into a test cell line, and analyse for effective knockdown and complementation.
* Iterate on module design.
* Test functional modules in genome-free minicells, working toward implementing a complete boot sequence to begin growth and division.

This development kit represents the basic tools to begin exploring the functional design space. We expect that all will grow in power and scope; see our [Roadmap] for details. 