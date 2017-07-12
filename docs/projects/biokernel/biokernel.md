---
layout: page
permalink: /biokernel/
weight: 5
---

<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<p style="text-align:center;"><img src="/engineering/images/Biokernel.png"></p>

<div class="container">

  <div class="panel-group" id="accordion">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse1">What is the biokernel?</a>
        </h4>
      </div>
      <div id="collapse1" class="panel-collapse collapse">
        <div class="panel-body">The biokernel is a set of genes and biomolecules defined at single-molecule resolution that when organized appropriately lead to a functioning, computationally-simulatable cell. It will possess the core components and functions necessary for an organism, and be developed in a manner amenable to the distributed construction of arbitrary organisms of desired function. For such a goal to be achieved, we believe the biokernel will require: a set of genes encoding a cell in which all biomolecules that are produced are accounted for, an operational understanding of the functionality of each biomolecule, and a comprehensive model of their abundancies and positions over time.
</div>
      </div>
    </div>
	
	
   <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse2">What is the strategy for developing the biokernel?</a>
        </h4>
      </div>
      <div id="collapse2" class="panel-collapse collapse">
        <div class="panel-body">
				<p style="text-align:center;"><img src="/engineering/images/Approach.png" width = "700"></p>
				
        <p> Construction of a semi-synthetic cell, or the design of a synthetic genome encoding and operating within single-molecule resolution defined biomolecules derived from natural organisms, is the most technically approachable path towards the goal of a simulatable cell. </p>
				
        <p style="text-align:center;"><img src="/engineering/images/in vitro.png" width = "850"></p>
				<p> The prototyping platform to validate modules involves the design of chosen genes encoding the production of biomolecules to perform functions, building and integrating those genetic constructs and reconstituted cytosol, and testing them in a defined background while taking the requisite measurements to inform the next design cycle. </p>	
		</div>
      </div>
    </div>
	
	
	    <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse3">How can the biokernel be collaboratively developed?</a>
        </h4>
      </div>
      <div id="collapse3" class="panel-collapse collapse">
        <div class="panel-body">
		<p>Once separate groups have made the decision to collaborate, the transaction cost for working together can be minimized through two benchmarks.</p>
		<p style="text-align:center;"><img src="/engineering/images/Distribution.png" width = "500"></p>
		<p><strong>Distributed development: </strong>The forward engineering of an entire genome provides opportunity for modularization and distributed development across multiple individuals and labs.</p>
		<p style="text-align:center;"><img src="/engineering/images/Standards.png" width = "500"></p>
		<p><strong>Standardization and Reproducibility: </strong>The testing of designs within the background of an ensemble of defined molecular components that is also accessible promotes communication and reproducibility of results for communal development.</p>
		</div>
      </div>
    </div>
	
	    <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse4">What is PURE?</a>
        </h4>
      </div>
      <div id="collapse4" class="panel-collapse collapse">
        <div class="panel-body">
		<p>PURE is a reconstituted expression system (mostly from E. coli) developed by <a href="http://www.nature.com/nbt/journal/v19/n8/full/nbt0801_751.html">Ueda et al. in 2001</a>. It contains all the purified components required to generate a polypeptide sequence from a DNA template. Its composition provides a <strong>defined</strong> background to drive consistent expression and can be used as the fundamental basis for building out into a simulatable cell.</p>
		<p style="text-align:center;"><img src="/engineering/images/PUREdata.png" width = "400"></p>
		</div>
      </div>
    </div>
	
        <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" data-parent="#accordion" href="#collapse5">What are the advantages of building out from PURE?</a>
        </h4>
      </div>
      <div id="collapse5" class="panel-collapse collapse">
        <div class="panel-body">
        <p>There are four distinct advantages for using PURE to build a cell.</p>
        <p style="text-align:center;"><img src="/engineering/images/One.png" width = "600"></p>
       	<p>Constructs can be measured and prototyped on the same time order of the biochemical reactions taking place (no need to wait for cells to grow!).</p>
        <p style="text-align:center;"><img src="/engineering/images/Two.png" width = "600"></p>
        <p>The reconstituted cytosol can be defined to your choosing allowing for measuring perturbations and changes that occur through tuning of the collections of biomolecules.</p>
		<p style="text-align:center;"><img src="/engineering/images/Three.png" width = "600"></p>
        <p>Collections of genes can be measured to confirm that the biomolecules expressed do indeed perform their predicted function.</p>
		<p style="text-align:center;"><img src="/engineering/images/Four.png" width = "600"></p>
        <p>If the molecule to perform a specific biochemical function is unknown, then systematic screens can be used to discover genes that perform unknown functions.</p>
        
        <p>The major drawback of PURE (aside from cost) is that what you prototype in PURE has a risk of not working in another in vitro or in vivo context. Thus it is highly advisable to build out of the same context to test within - build out a cell from defined reconstituted biomolecules expressing a synthetic genome.</p>
        
        </div>
      </div>
    </div>
	
	
	
  </div> 
</div>
    
</body>
</html>
