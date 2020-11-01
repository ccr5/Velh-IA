import 'reflect-metadata'
import { TYPES } from './types'
import { container } from 'tsyringe'
import { IAlgorithmRepository } from '@interfaces/iAlgorithm'
import { AlgorithmRepository } from '@repository/algorithmRepository'
import { EducationRepository } from '@repository/educationRepository'
import { FamilyRepository } from '@repository/familyRepository'
import { ReligionRepository } from '@repository/religionRepository'
import { IMatchRepository } from '@interfaces/iMatch'
import { MatchRepository } from '@repository/matchRepository'
import { IAgentRepository } from '@interfaces/iAgent'

container.registerSingleton<IAlgorithmRepository>(
  TYPES.AlgorithmRepository,
  AlgorithmRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.EducationRepository,
  EducationRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.FamilyRepository,
  FamilyRepository
)

container.registerSingleton<IAgentRepository>(
  TYPES.ReligionRepository,
  ReligionRepository
)

container.registerSingleton<IMatchRepository>(
  TYPES.MatchRepository,
  MatchRepository
)
