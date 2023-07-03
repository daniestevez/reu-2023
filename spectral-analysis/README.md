# Spectral analysis

These flowgraphs demonstrate how to perform spectral analysis in GNU Radio,
using a custom FFT and integration. There are the following flowgraphs:

* `spectral_analysis_sim.grc` shows how to generate a narrowband and a wideband
  test signals and plot their spectrum.

* `spectral_analysis_voyager1.grc` shows how to detect a human made signal: the
  transmission from the Voyager-1 probe at 8.4 GHz. It uses a recording done
  with GBT. It can be found in the file `vgr1_blc23_guppi_59046_80036_DIAG_VOYAGER-1_0011.cs8`
  in
  [this Google drive folder](https://drive.google.com/drive/folders/1N5DtsxAtVz0p5Wgq45v-QkF6tVzV84TP?usp=sharing).

* `spectral_analysis_w3oh.grc` shows how to analyze the spectrum of the OH
  line (1665.4 MHz) of the maser W3OH. It uses a recording done with the Allen Telescope Array.
  It can be found in [this Zenodo dataset](https://zenodo.org/record/6711078).
