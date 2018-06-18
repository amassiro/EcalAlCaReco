########
# Data
########

#        CRAB task name          DAS name                                 
samples['ZElectron-PromptReco-v1']   = ['/EGamma/Run2018A-ZElectron-PromptReco-v1/RAW-RECO',        ['outputFiles=EcalUncalZElectron.root']]

#config.Data.useParent = True           # Important!



########
# Alternative global configuration
########

config.JobType.psetName = '../step21_RAW2DIGI_RECO_EI_ALCA.py'
config.Data.splitting = 'LumiBased'    # FileBased
config.Data.unitsPerJob   = 10
# config.Data.runRange = '251562-254790'


####config.Data.splitting = 'LumiBased'    # FileBased
#####config.Data.splitting = 'FileBased'    # FileBased
#####config.Data.unitsPerJob   = 1
####config.Data.unitsPerJob   = 3   # 1 is creating 12k jobs ... max from crab is 10k

#config.JobType.psetName = '../reco_RAW2DIGI_RECO_AOD.py'
#config.JobType.maxMemoryMB = 2500    # 2.5 GB







################

config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/amassiro/AlCaRECO/'
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-317391_13TeV_PromptReco_Collisions18_JSON.txt"   
config.General.workArea     = 'crab_projects_Jun18_2018_rawreco_v1'
config.JobType.inputFiles = ['../EBAlign_2018_6May.db','../EEAlign_2018_6May.db']

                                                                                                                                              