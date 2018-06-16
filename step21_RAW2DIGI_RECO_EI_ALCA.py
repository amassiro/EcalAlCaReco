# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step21 --data --eventcontent ALCARECO runUnscheduled --datatier ALCARECO --conditions 101X_dataRun2_Prompt_v10 --step RAW2DIGI,RECO,EI,ALCA:EcalUncalZElectron --nThreads 8 --era Run2_2018
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2018A/EGamma/RAW-RECO/ZElectron-PromptReco-v1/000/316/219/00000/E0B20BFA-C958-E811-B2F5-FA163EE92A5B.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step21 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition
process.ALCARECOStreamEcalUncalZElectron = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            'pathALCARECOEcalUncalZElectron', 
            'pathALCARECOEcalUncalZSCElectron'
        )
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('EcalUncalZElectron')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('EcalUncalZElectron.root'),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices_*_*', 
        'keep recoVertexs_offlinePrimaryVerticesWithBS_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_electronGsfTracks_*_*', 
        'keep *GsfTrack*_uncleanedOnlyElectronGsfTracks_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectron*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronsTmp_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhoton_*_*', 
        'keep recoCaloClusters_hfEMClusters_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_alCaIsolatedElectrons_*_*', 
        'keep recoCaloClusters_cleanedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_hybridSuperClusters_*_*', 
        'keep recoCaloClusters_uncleanedHybridSuperClusters_*_*', 
        'keep recoCaloClusters_multi5x5BasicClustersCleaned_*_*', 
        'keep recoCaloClusters_multi5x5BasicClustersUncleaned_*_*', 
        'keep recoCaloClusters_multi5x5SuperClusters_*_*', 
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoSuperClusters_SCselector_*_*', 
        'keep recoSuperClusters_cleanedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_hfEMClusters_*_*', 
        'keep recoSuperClusters_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_mergedSuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_uncleanedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_uncleanedOnlyCorrectedHybridSuperClusters_*_*', 
        'keep recoSuperClusters_uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_uncleanedOnlyMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersCleaned_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersUncleaned_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*', 
        'keep recoPreshowerCluster*_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerCluster*_uncleanedOnlyMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerCluster*_multi5x5PreshowerClusterShape_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep *EcalRecHit*_reducedEcalRecHitsES_alCaRecHitsES_*', 
        'keep *_ecalDigis_*_*', 
        'keep *EcalTriggerPrimitiveDigi*_ecalDigis_*_*', 
        'keep *_ecalPreshowerDigis_*_*', 
        'keep *_ecalDetIdToBeRecovered_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*', 
        'drop recoCaloClusters_*_*_*', 
        'drop recoSuperClusters_*_*_*', 
        'drop recoPreshowerCluster*_*_*_*', 
        'drop *EcalRecHit*_reducedEcalRecHitsES*_*_*', 
        'keep reco*Clusters_pfElectronTranslator_*_*'
    )
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOEcalUncalZElectron_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '101X_dataRun2_Prompt_v10', '')


#    https://cms-conddb.cern.ch/cmsDbBrowser/diff/Prod/gts/101X_dataRun2_HLT_withPixelLocalReco_TkAlignment/101X_dataRun2_HLT_v7
#            SiPixelGenErrorDBObjectRcd      -       SiPixelGenErrorDBObject_phase1_38T_2018_v4      SiPixelGenErrorDBObject_38T_v2_hlt
#            SiPixelLorentzAngleRcd  -       SiPixelLorentzAngle_phase1_2018_v4      SiPixelLorentzAngle_2009_v1_hlt
#            SiPixelTemplateDBObjectRcd      -       SiPixelTemplateDBObject_phase1_38T_2018_v4      SiPixelTemplateDBObject38Tv2_hlt
#            TrackerAlignmentRcd     -       TrackerAlignment_PCL_byRun_v1_express_315648    TrackerAlignment_PCL_byRun_v0_hlt
        
        
        
process.GlobalTag.toGet = cms.VPSet(
       # new tracker and pixel
       cms.PSet(record = cms.string("SiPixelGenErrorDBObjectRcd"),
       tag = cms.string("SiPixelGenErrorDBObject_phase1_38T_2018_v4"),
       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
       ),
       cms.PSet(record = cms.string("SiPixelLorentzAngleRcd"),
       tag = cms.string("SiPixelLorentzAngle_phase1_2018_v4"),
       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
       ),
       cms.PSet(record = cms.string("SiPixelTemplateDBObjectRcd"),
       tag = cms.string("SiPixelTemplateDBObject_phase1_38T_2018_v4"),
       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
       ),
       cms.PSet(record = cms.string("TrackerAlignmentRcd"),
       tag = cms.string("TrackerAlignment_PCL_byRun_v1_express_315648"),
       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
       ),
       
       # ecal alignment 
       cms.PSet(record = cms.string("EEAlignmentRcd"),
       tag = cms.string("EEAlignment_measured_v05_offline"),
       connect = cms.string("sqlite_file:EEAlign_2018_6May.db")
       ), 
       cms.PSet(record = cms.string("EBAlignmentRcd"),
       tag = cms.string("EBAlignment_measured_v05_offline"),
       connect = cms.string("sqlite_file:EBAlign_2018_6May.db")
       ),
       
       
     )

     
     
# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamEcalUncalZElectronOutPath = cms.EndPath(process.ALCARECOStreamEcalUncalZElectron)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.eventinterpretaion_step,process.pathALCARECOEcalUncalZElectron,process.pathALCARECOEcalUncalZSCElectron,process.endjob_step,process.ALCARECOStreamEcalUncalZElectronOutPath)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
