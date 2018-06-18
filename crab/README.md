Submit AlcaReco production over crab
----

See details in:

    https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial#CRAB_configuration_parameters
    https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

check if I have writing permissions:

    source /cvmfs/cms.cern.ch/crab3/crab.sh
    crab checkwrite --site=T2_CH_CERN
    crab checkwrite --site=T2_CH_CERN  --lfn=/store/user/amassiro/ECAL/
    crab checkwrite --site=T2_CH_CERN  --lfn=/store/group/dpg_ecal/alca_ecalcalib/amassiro/

    
Multicrab

    voms-proxy-init --voms cms
    myproxy-init -v
    source /cvmfs/cms.cern.ch/crab3/crab.sh
    
    python multicrab.py   samples/samples_data2018.py

    python multicrab.py crab_projects_Jun18_2018_rawreco_v1 status
    python multicrab.py crab_projects_Jun18_2018_rawreco_v1 resubmit
