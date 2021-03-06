
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'ExtraDimensionsLED:LambdaT = 100000',
            'ExtraDimensionsLED:ffbar2llbar = on',
            'ExtraDimensionsLED:gg2llbar = on',
            'ExtraDimensionsLED:NegInt = 0',
            'ExtraDimensionsLED:CutOffmode = 0',
            'PhaseSpace:mHatMin = 800',
            'PhaseSpace:mHatMax = 1300',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
                                    )
    )
)
