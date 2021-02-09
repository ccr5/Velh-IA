import 'reflect-metadata'
import TYPES from './types'
import { container } from 'tsyringe'
import AlgorithmRepository from 'src/adapters/repository/algorithmRepository'
import EducationRepository from 'src/adapters/repository/educationRepository'
import FamilyRepository from 'src/adapters/repository/familyRepository'
import MatchRepository from 'src/adapters/repository/matchRepository'
import ReligionRepository from 'src/adapters/repository/religionRepository'
import IAlgorithmRepository from '@useCases/algorithm/iAlgorithmRepository'
import IAgentRepository from '@useCases/multiAgentSystem/iAgentRepository'
import IMatchRepository from '@useCases/match/iMatchRepository'
import IAlgorithmUseCase from 'src/useCases/algorithm/iAlgorithmUseCase'
import AlgorithmUseCase from 'src/useCases/algorithm/algorithmUseCase'
import IAgentUseCase from 'src/useCases/multiAgentSystem/iAgentUseCase'
import EducationUseCase from 'src/useCases/multiAgentSystem/educationUseCase'
import IMatchUseCase from 'src/useCases/match/iMatchUseCase'
import FamilyUseCase from 'src/useCases/multiAgentSystem/familyUseCase'
import MatchUseCase from 'src/useCases/match/matchUseCase'
import ReligionUseCase from 'src/useCases/multiAgentSystem/religionUseCase'

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
