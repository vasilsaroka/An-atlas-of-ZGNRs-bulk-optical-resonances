21/05/2019: In this folder I recalculated the optical absorption spectra for zigzag graphene nanoribbons with my averaged fit
and using increased number of k-points for the energy band structures: NumberOfkpoints=1000.

frequencey energy range is reduced to 8 eV from 9 eV.
delta-function broadening is set to be 0.03 eV
number of point in the absorption spectrum = 2000 instead of 1600.

I expect that the quality of the output plots will increase and the number of spurious peaks will reduce.

The code with which I recalculated the Kataura plots for ribbons uses tbparameters variable while in the 
source file the variable is called avtbparameters. This means my previous calculations most probably used the wrong tight-
binding parameters. I need to check this. Perhaps, that is why the correlation and alignment maps significantly changed.

Note: Indeed the previous two runs for zigzag ribbons on 19 May used the TB parameter of the Reich2003 model, although 
I was sure that I was using the averaged fitted parameter 
