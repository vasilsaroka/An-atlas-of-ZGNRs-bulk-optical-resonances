# An-atlas-of-ZGNRs-bulk-optical-resonances


This is Mathematica and partially Python code to reproduce Figures of the paper "2N+4-rule and an atlas of bulk optical resonances of zigzag graphene nanoribbons".


<h2>Requirements</h2>
<ul>
<li>OS: The code was tested on Windows 7 and 10.</li>
<li>Mathematica 10.4 11.3 or 12.</li>
<li>Packages <a href="https://library.wolfram.com/infocenter/MathSource/9355/">MaTeX</a>  by Szabolcs Horvát and <a href="https://library.wolfram.com/infocenter/Demos/5599/">CustomTicks</a> by Mark A. Caprio  are required in Mathematica.</li>
<li>Python 3.7.1</li>
<li>Packages numpy, scipy, matplotlib, re, os and datetime are required in the python script Figure1.py.</li>
</ul>

<h2>Installation guide</h2>
<div>The code does not require any specific installation other then configuration of Mathematica and Python. However, compilation to C code is used in Mathematica to speed up optical absorption spectra calculations. See <a href="https://sites.google.com/site/sarokavasil/wolfram-mathematica">how to make Mathematica working with C compiler on Windows</a>.</div>

<div>To use this code:</div>

<ul>
  <li>Copy the repository to a separate folder on your PC.</li>
  <li>Run code from the code directories Mathematica and python.</li>
</ul>

<h2>Demo</h2>
<ul>
<li>Tight-binding calculations can be repeated in the Mathematica notebook in Sections 'Fitting TB model' and 'Optical absorption calculations in TB model'</li>
<li>The output shall appear in the test directory and will be the same as what can be found in raw data directory</li>
<li>Expected run time can be found in the output files in raw  data directory</li>
</ul>

<h2>Instructions for use</h2>
<div>For Figure reproduction this code uses precalculated data from raw data directory of the repository.</div>
<ul>
<li>Copy the repository to a separate folder on your computer.</li>
<li>Navigate to the code-Mathematica and open Mathemaitca notebook `2N+4-rule and an atlas of bulk optical resonances of zigzag graphene nanoribbons.nb'</li>
<li>In Evaluation tab click `Evaluate Initialization Cells'</li>
<li>Find the required section for a Figure reproduction, open the section and evaluate each cell of the Section. The output figure must appear in the `test' folder of the parent directory.</li>
</ul>

<h2>License</h2>
<div>GNU Lesser General Public License v3.0</div>
