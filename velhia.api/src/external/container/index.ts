import 'reflect-metadata'
import TYPES from './types'
import { container } from 'tsyringe'
import AlgorithmRepository from '@adapters/repository/algorithmRepository'
import IAlgorithmRepository from '@useCases/algorithm/iAlgorithmRepository'
import IAlgorithmUseCase from '@useCases/algorithm/iAlgorithmUseCase'
import AlgorithmUseCase from '@useCases/algorithm/algorithmUseCase'
import MatchRepository from '@adapters/repository/matchRepository'
import IMatchRepository from '@useCases/match/iMatchRepository'
import IMatchUseCase from '@useCases/match/iMatchUseCase'
import MatchUseCase from '@useCases/match/matchUseCase'

container.registerSingleton<IAlgorithmRepository>(
  TYPES.AlgorithmRepository,
  AlgorithmRepository
)

container.registerSingleton<IMatchRepository>(
  TYPES.MatchRepository,
  MatchRepository
)

container.registerSingleton<IAlgorithmUseCase>(
  TYPES.AlgorithmUseCase,
  AlgorithmUseCase
)

container.registerSingleton<IMatchUseCase>(
  TYPES.MatchUseCase,
  MatchUseCase
)
