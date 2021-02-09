import TYPES from '@external/container/types'
import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'
import IAlgorithm from '@entities/algorithm/iAlgorithm'
import IMatch from '@entities/match/iMatch'
import IAgent from '@entities/multiAgentSystem/iAgent'
import IAlgorithmUseCase from '@useCases/algorithm/iAlgorithmUseCase'
import IMatchUseCase from '@useCases/match/iMatchUseCase'
import IAgentUseCase from '@useCases/multiAgentSystem/iAgentUseCase'
import { IGeneralData, IPlayersData, ICamp, IMAS } from '@adapters/interfaces/iWeb'

@injectable()
export class WebController {
  private matchUseCase: IMatchUseCase
  private algorithmUseCase: IAlgorithmUseCase
  private familyUseCase: IAgentUseCase
  private educationUseCase: IAgentUseCase
  private religionUseCase: IAgentUseCase

  constructor(
    @inject(TYPES.MatchUseCase) _matchUseCase: IMatchUseCase,
    @inject(TYPES.AlgorithmUseCase) _algorithmUseCase: IAlgorithmUseCase,
    @inject(TYPES.FamilyUseCase) _familyUseCase: IAgentUseCase,
    @inject(TYPES.EducationUseCase) _educationUseCase: IAgentUseCase,
    @inject(TYPES.ReligionUseCase) _religionUseCase: IAgentUseCase
  ) {
    this.matchUseCase = _matchUseCase
    this.algorithmUseCase = _algorithmUseCase
    this.familyUseCase = _familyUseCase
    this.educationUseCase = _educationUseCase
    this.religionUseCase = _religionUseCase
  }

  /**
   * return general datas to fill website home screen
   * @param {Request} req request
   * @param {Response} res response
   * @example getGeneralData()
   * @returns {Promise<Response | void>} IAgent[] | 404 
   */
  async getGeneralData (req: Request, res: Response): Promise<Response | void> {
    try {
      const mac: IMatch[] | null = await this.matchUseCase.getMatch(undefined, undefined, undefined, undefined, undefined)
      const sa: IAlgorithm[] | null = await this.algorithmUseCase.getAlgorithm(undefined, undefined, undefined, '0', '1')

      if (mac == null) { return res.sendStatus(404) }
      if (sa == null) { return res.sendStatus(404) }

      const ret: IGeneralData = {
        begin: mac[0].begin,
        nMatchs: mac.length,
        nDraws: sa[0].draw
      }

      return res.send(ret)

    } catch (error) {
      res.sendStatus(400)
    }
  }

  /**
   * return statistical algorithms datas to fill website home screen
   * @param {Request} req request
   * @param {Response} res response
   * @example getSAData()
   * @returns {Promise<Response | void>} IAgent[] | 404 
   */
  async getSAData (req: Request, res: Response): Promise<Response | void> {
    try {
      const sa: IAlgorithm[] | null = await this.algorithmUseCase.getAlgorithm(undefined, undefined, undefined, '0', '1' )
      if (sa == null) { return res.sendStatus(404) }
      const wins: number = sa[0].victories
      const percent: number = sa[0].victories / (sa[0].victories + sa[0].draw + sa[0].defeats)
      const ret: IPlayersData = { wins: wins, percent: percent }
      return res.send(ret)

    } catch (error) {
      res.sendStatus(400)
    }
  }

  /**
   * return multi agent system datas to fill website home screen
   * @param {Request} req request
   * @param {Response} res response
   * @example getMASData()
   * @returns {Promise<Response | void>} IAgent[] | 404 
   */
  async getMASData (req: Request, res: Response): Promise<Response | void> {
    try {
      const family: IAgent[] | null = await this.familyUseCase.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')

      if (family == null) { return res.sendStatus(404) }
      const wins: number = family[1].victories
      const percent: number = family[1].victories / family[1].memory.length
      const ret: IPlayersData = { wins: wins, percent: percent }
      return res.send(ret)

    } catch (error) {
      res.sendStatus(400)
    }
  }

  /**
   * return lastest match plays to fill website home screen
   * @param {Request} req request
   * @param {Response} res response
   * @example getCampData()
   * @returns {Promise<Response | void>} IAgent[] | 404 
   */
  async getCampData (req: Request, res: Response): Promise<Response | void> {
    try {
      const match: IMatch[] | null = await this.matchUseCase.getMatch(undefined, undefined, 'createdAt:desc', '0', '1')
      if (match == null) { return res.sendStatus(404) }
      let game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

      match[0].plays.forEach(play => {
        if (play.player == 'MAS') {
          game[play.position] = 0
        } else {
          game[play.position] = 1
        }
      })

      const ret: ICamp = {
        C1: { L1: game[6], L2: game[3], L3: game[0] },
        C2: { L1: game[7], L2: game[4], L3: game[1] },
        C3: { L1: game[8], L2: game[5], L3: game[2] }
      }

      return res.send(ret)

    } catch (error) {
      res.sendStatus(400)
    }
  }

  /**
   * return lastest MAS to fill website home screen
   * @param {Request} req request
   * @param {Response} res response
   * @example getMAS()
   * @returns {Promise<Response | void>} 
   */ 
  async getMAS (req: Request, res: Response): Promise<Response | void> {
    try {
      const family: IAgent[] | null = await this.familyUseCase.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')
      const familyMemories: IAgent[] | null = await this.familyUseCase.getAgent(undefined, undefined, undefined, undefined, undefined)
      const education: IAgent[] | null = await this.educationUseCase.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')
      const educationMemories: IAgent[] | null = await this.educationUseCase.getAgent(undefined, undefined, undefined, undefined, undefined)
      const religion: IAgent[] | null = await this.religionUseCase.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')
      const religionMemories: IAgent[] | null = await this.religionUseCase.getAgent(undefined, undefined, undefined, undefined, undefined)

      if (family == null || education == null || religion == null) { return res.sendStatus(404) }
      if (familyMemories == null || educationMemories == null || religionMemories == null) { return res.sendStatus(404) }

      const ret: IMAS = {
        family: {
          institution: 'family',
          generation: `${familyMemories.length - 1}º`,
          progenitor: family[1].progenitor,
          life: family[1].life,
          memories: family[1].memory.length,
          matchAsLearner: family[1].matchsAsLearner,
          matchAsLeader: family[1].matchsAsLeader,
          victories: family[1].victories,
          defeats: family[1].defeats,
          draws: family[1].draw
        },
        education: {
          institution: 'education',
          generation: `${educationMemories.length - 1}º`,
          progenitor: education[1].progenitor,
          life: education[1].life,
          memories: education[1].memory.length,
          matchAsLearner: education[1].matchsAsLearner,
          matchAsLeader: education[1].matchsAsLeader,
          victories: education[1].victories,
          defeats: education[1].defeats,
          draws: education[1].draw
        },
        religion: {
          institution: 'religion',
          generation: `${religionMemories.length - 1}º`,
          progenitor: religion[1].progenitor,
          life: religion[1].life,
          memories: religion[1].memory.length,
          matchAsLearner: religion[1].matchsAsLearner,
          matchAsLeader: religion[1].matchsAsLeader,
          victories: religion[1].victories,
          defeats: religion[1].defeats,
          draws: religion[1].draw
        }
      }

      return res.send(ret)

    } catch (error) {
      res.sendStatus(400)
    }
  }
}
