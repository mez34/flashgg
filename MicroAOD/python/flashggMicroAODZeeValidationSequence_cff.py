import FWCore.ParameterSet.Config as cms

from flashgg.MicroAOD.flashggMicroAODSequence_cff import *
from flashgg.MicroAOD.flashggZeeDiPhotons_cfi import flashggZeeDiPhotons

flashggMicroAODZeeValidationSequence = cms.Sequence(flashggMicroAODSequence)
flashggMicroAODZeeValidationSequence.remove(flashggElectrons)
flashggMicroAODZeeValidationSequence.remove(flashggPreselectedDiPhotons)
flashggMicroAODZeeValidationSequence.remove(flashggJets)
flashggMicroAODZeeValidationSequence += flashggZeeDiPhotons
