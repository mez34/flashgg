import FWCore.ParameterSet.Config as cms

flashggPhotons = cms.EDProducer('FlashggPhotonProducer',
                                photonTag = cms.InputTag('slimmedPhotons'),
                                pfCandidatesTag = cms.InputTag("packedPFCandidates"),
                                reducedBarrelRecHitCollection = cms.InputTag('reducedEgamma','reducedEBRecHits'),
                                reducedEndcapRecHitCollection = cms.InputTag('reducedEgamma','reducedEERecHits'),
                                reducedPreshowerRecHitCollection = cms.InputTag('reducedEgamma','reducedESRecHits'),
                                
                                vertexTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                vertexCandidateMapTag = cms.InputTag("flashggVertexMapNonUnique"),
                                rhoFixedGridCollection = cms.InputTag('fixedGridRhoAll'),
                                
                                photonIdMVAweightfile_EB = cms.FileInPath("flashgg/MicroAOD/data/MVAweights_Spring15_25ns_barrel.xml"),
                                photonIdMVAweightfile_EE = cms.FileInPath("flashgg/MicroAOD/data/MVAweights_Spring15_25ns_endcap.xml"),

                                useNonZsLazyTools = cms.bool(True),
                                recomputeNonZsClusterShapes = cms.bool(False),
                                addRechitFlags = cms.bool(True),
                                doOverlapRemovalForIsolation = cms.bool(True),
                                useVtx0ForNeutralIso = cms.bool(True),
                                extraCaloIsolations = cms.VPSet(),
                                extraIsolations = cms.VPSet(),

                                genPhotonTag = cms.InputTag("flashggGenPhotonsExtra"),
                                maxGenDeltaR = cms.double(0.1),
                                copyExtraGenInfo = cms.bool(True),

				convTag = cms.InputTag('reducedEgamma','reducedConversions'),
				beamSpotTag = cms.InputTag('offlineBeamSpot'),
				elecLabel = cms.string("slimmedElectrons")
                              )
