import 'reflect-metadata'
import { TYPES } from './types'
import { container } from 'tsyringe'

import { IAgentRepository } from '@interfaces/v1/iAgent'
import { IAlgorithmRepository } from '@interfaces/v1/iAlgorithm'
import { IMatchRepository } from '@interfaces/v1/iMatch'

import { AlgorithmRepository } from '@repository/v1/algorithmRepository'
import { EducationRepository } from '@repository/v1/educationRepository'
import { FamilyRepository } from '@repository/v1/familyRepository'
import { ReligionRepository } from '@repository/v1/religionRepository'
import { MatchRepository } from '@repository/v1/matchRepository'

import { AlgorithmTestRepository } from '@repository/v1/algorithmTestRepository'
import { EducationTestRepository } from '@repository/v1/educationTestRepository'
import { FamilyTestRepository } from '@repository/v1/familyTestRepository'
import { MatchTestRepository } from '@repository/v1/matchTestRepository'
import { ReligionTestRepository } from '@repository/v1/religionTestRepository'

container.registerSingleton<IAlgorithmRepository>(
  TYPES.AlgorithmRepository,
  AlgorithmRepository
)

container.registerSingleton<IAlgorithmRepository>(
  TYPES.AlgorithmTestRepository,
  AlgorithmTestRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.EducationRepository,
  EducationRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.EducationTestRepository,
  EducationTestRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.FamilyRepository,
  FamilyRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.FamilyTestRepository,
  FamilyTestRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.ReligionRepository,
  ReligionRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.ReligionTestRepository,
  ReligionTestRepository
)

container.registerSingleton<IMatchRepository>(
  TYPES.MatchRepository,
  MatchRepository
)

container.registerSingleton<IMatchRepository>(
  TYPES.MatchTestRepository,
  MatchTestRepository
)
