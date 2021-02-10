import 'reflect-metadata'
import TYPES from './types'
import { container } from 'tsyringe'
import AlgorithmRepository from '@adapters/repository/algorithmRepository'
import EducationRepository from '@adapters/repository/educationRepository'
import FamilyRepository from '@adapters/repository/familyRepository'
import MatchRepository from '@adapters/repository/matchRepository'
import ReligionRepository from '@adapters/repository/religionRepository'
import IAlgorithmRepository from '@useCases/algorithm/iAlgorithmRepository'
import IAgentRepository from '@useCases/multiAgentSystem/iAgentRepository'
import IMatchRepository from '@useCases/match/iMatchRepository'
import IAlgorithmUseCase from '@useCases/algorithm/iAlgorithmUseCase'
import AlgorithmUseCase from '@useCases/algorithm/algorithmUseCase'
import IAgentUseCase from '@useCases/multiAgentSystem/iAgentUseCase'
import EducationUseCase from '@useCases/multiAgentSystem/educationUseCase'
import IMatchUseCase from '@useCases/match/iMatchUseCase'
import FamilyUseCase from '@useCases/multiAgentSystem/familyUseCase'
import MatchUseCase from '@useCases/match/matchUseCase'
import ReligionUseCase from '@useCases/multiAgentSystem/religionUseCase'

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

container.registerSingleton<IAlgorithmUseCase>(
  TYPES.AlgorithmUseCase,
  AlgorithmUseCase
)

container.registerSingleton<IAgentUseCase>(
  TYPES.EducationUseCase,
  EducationUseCase
)

container.registerSingleton<IAgentUseCase>(
  TYPES.FamilyUseCase,
  FamilyUseCase
)

container.registerSingleton<IAgentUseCase>(
  TYPES.ReligionUseCase,
  ReligionUseCase
)

container.registerSingleton<IMatchUseCase>(
  TYPES.MatchUseCase,
  MatchUseCase
)
