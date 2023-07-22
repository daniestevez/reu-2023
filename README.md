# Breakthrough Listen REU 2023 GNU Radio materials


This repository contains miscellanous materials used on the GNU Radio tutorials
of the Breakthrough Listen Research Experience for Undergraduates summer
program. The material was elaborated in the context of the collaboration between
GNU Radio and SETI Institute.

## Outline

The material is organized in the following folders:

* Session 1. `introduction-slides`. some introductory slides for the tutorials.

* Session 1. `audio`. A simple example showing how to generate and display audio
  (soundcard) signals with GNU Radio.

* Session 1. `rtl-sdr`. A simple example showing how to receive signals with the
  RTL-SDR in GNU Radio.

* Session 2. `spectral-analysis`. Shows how to simulate narrowband and wideband
  signals and how to do custom spectral analysis with FFTs. Includes real world
  example applications with a spectral line (W3OH maser) and a spacecraft
  (Voyager-1) recording.

* Session 3. `scripting`. Shows how to control a flowgraph using Parameter
  blocks by running it from the command line or from Python. As a demo, there is
  an "observation" with an RTL-SDR scanning different frequencies and producing
  IQ and waterfall data.

* Session 4. `doppler`. Shows how to do a simulation of a signal having constant
  Doppler drift using a sawtooth Signal Source, how to do Doppler simulations
  with the Doppler Correction block and data from Astropy or HORIZONS, and how
  to measure frequency very accurately by using a PLL to measure phase.

## Previous years

This is the list of materials used in previous years:

* [2022](https://github.com/daniestevez/reu-2022)

* [2021](https://github.com/daniestevez/reu-2021)
