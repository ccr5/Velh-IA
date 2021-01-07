import { TYPES } from '@config/container/types'
import { IAgent, IAgentRepository } from '@interfaces/iAgent'
import { IAlgorithm, IAlgorithmRepository } from '@interfaces/iAlgorithm'
import { IMatch, IMatchRepository } from '@interfaces/iMatch'
import { ICamp, IGeneralData, IPlayersData, IMAS } from '@interfaces/iWeb'
import { Request, Response } from 'express'
import { inject, injectable } from 'tsyringe'

@injectable()
export class WebController {
  private matchRepository: IMatchRepository
  private algorithmRepository: IAlgorithmRepository
  private familyRepository: IAgentRepository
  private educationRepository: IAgentRepository
  private religionRepository: IAgentRepository

  constructor(
    @inject(TYPES.MatchRepository) matchRepository: IMatchRepository,
    @inject(TYPES.AlgorithmRepository) algorithmRepository: IAlgorithmRepository,
    @inject(TYPES.FamilyRepository) familyRepository: IAgentRepository,
    @inject(TYPES.EducationRepository) educationRepository: IAgentRepository,
    @inject(TYPES.ReligionRepository) religionRepository: IAgentRepository
  ) {
    this.matchRepository = matchRepository
    this.algorithmRepository = algorithmRepository
    this.familyRepository = familyRepository
    this.educationRepository = educationRepository
    this.religionRepository = religionRepository
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
      const mac: IMatch[] | null = await this.matchRepository.getMatch(undefined, undefined, undefined, undefined, undefined)
      const sa: IAlgorithm[] | null = await this.algorithmRepository.getAlgorithm(undefined, undefined, undefined, '0', '1')

      if (mac == null) { return res.sendStatus(404) }
      if (sa == null) { return res.sendStatus(404) }

      const ret: IGeneralData = {
        begin: mac[0].begin,
        nMatchs: mac.length,
        nDraws: sa[0].draw
      }

      res.send(ret)

    } catch (error) {
      res.sendStatus(400).send(error)
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
      const sa: IAlgorithm[] | null = await this.algorithmRepository.getAlgorithm(undefined, undefined, undefined, '0', '1' )
      if (sa == null) { return res.sendStatus(404) }
      const wins: number = sa[0].victories
      const percent: number = sa[0].victories / (sa[0].victories + sa[0].draw + sa[0].defeats)
      const ret: IPlayersData = { wins: wins, percent: percent }
      res.send(ret)

    } catch (error) {
      res.sendStatus(400).send(error)
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
      const family: IAgent[] | null = await this.familyRepository.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')

      if (family == null) { return res.sendStatus(404) }
      const wins: number = family[1].victories
      const percent: number = family[1].victories / family[1].memory.length
      const ret: IPlayersData = { wins: wins, percent: percent }
      res.send(ret)

    } catch (error) {
      res.sendStatus(400).send(error)
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
      const match: IMatch[] | null = await this.matchRepository.getMatch(undefined, undefined, 'createdAt:desc', '0', '1')
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

      res.send(ret)

    } catch (error) {
      res.sendStatus(400).send(error)
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
      const family: IAgent[] | null = await this.familyRepository.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')
      const familyMemories: IAgent[] | null = await this.familyRepository.getAgent(undefined, undefined, undefined, undefined, undefined)
      const education: IAgent[] | null = await this.educationRepository.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')
      const educationMemories: IAgent[] | null = await this.educationRepository.getAgent(undefined, undefined, undefined, undefined, undefined)
      const religion: IAgent[] | null = await this.religionRepository.getAgent(undefined, undefined, 'createdAt:desc', '0', '2')
      const religionMemories: IAgent[] | null = await this.religionRepository.getAgent(undefined, undefined, undefined, undefined, undefined)

      if (family == null || education == null || religion == null) { return res.sendStatus(404) }
      if (familyMemories == null || educationMemories == null || religionMemories == null) { return res.sendStatus(404) }

      const ret: IMAS = {
        family: {
          institution: 'family',
          id: family[1].id,
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
          id: education[1].id,
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
          id: religion[1].id,
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

      res.send(ret)

    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
