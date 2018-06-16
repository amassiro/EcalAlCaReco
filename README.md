# EcalAlCaReco

Private rereco:

    cmsDriver.py step21 --mc --eventcontent AODSIM,ALCARECO runUnscheduled --datatier AODSIM,ALCARECO   \
            --conditions 100X_upgrade2018_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI,ALCA:EcalUncalZElectron  \
            --nThreads 8 --era Run2_2018
            
    cmsDriver.py step21 --data --eventcontent ALCARECO runUnscheduled --datatier ALCARECO   \
            --conditions 101X_dataRun2_Prompt_v10 --step RAW2DIGI,RECO,EI,ALCA:EcalUncalZElectron  \
            --nThreads 8 --era Run2_2018

    cmsRun step21_RAW2DIGI_RECO_EI_ALCA.py
    
            /EGamma/Run2018A-ZElectron-PromptReco-v1/RAW-RECO


