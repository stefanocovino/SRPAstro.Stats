""" Utility functions and classes for SRP

Context : SRP
Module  : Stats.py
Version : 1.0.2
Author  : Stefano Covino
Date    : 18/11/2021
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : input is a list of (x,sigmax)

History : (19/02/2012) First version.
        : (27/03/2013) Homogenous output in case of single output.
        : (18/11/2021) Minor correction.
"""


import numpy


def GenGaussSet (vl, evl, ntrial=100):
    if evl != 0.0:
        return numpy.random.normal(vl,evl,ntrial)
    else:
        return numpy.array([vl])
