import { TYPES } from '@config/container/types'
import { IAgent, IAgentRepository } from '@interfaces/iAgent'
import { IAlgorithm, IAlgorithmRepository } from '@interfaces/iAlgorithm'
import { IMatch, IMatchRepository } from '@interfaces/iMatch'
import { ICamp, IGeneralData, IPlayersData } from '@interfaces/iWeb'
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
  async getGeneralData(req: Request, res: Response): Promise<Response | void> {
    try {
      const mac: IMatch[] | null = await this.matchRepository.getAllMatch()
      const religion: IAgent[] | null = await this.religionRepository.getLastAgent(2)

      if (mac == null) { return res.sendStatus(404) }
      if (religion == null) { return res.sendStatus(404) }

      const ret: IGeneralData = {
        begin: mac[0].begin,
        nMatchs: mac.length,
        nDraws: religion[1].draw
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
  async getSAData(req: Request, res: Response): Promise<Response | void> {
    try {
      const sa: IAlgorithm[] | null = await this.algorithmRepository.getLastAlgorithm(1)
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
  async getMASData(req: Request, res: Response): Promise<Response | void> {
    try {
      const family: IAgent[] | null = await this.familyRepository.getLastAgent(2)

      if (family == null) { return res.sendStatus(404) }
      const wins: number = family[0].victories
      const percent: number = family[0].victories / family[0].memory.length
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
  async getCampData(req: Request, res: Response): Promise<Response | void> {
    try {
      const match: IMatch[] | null = await this.matchRepository.getLastMatch(2)
      if (match == null) { return res.sendStatus(404) }
      let game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

      match[1].plays.forEach(play => {
        if (play.player == 'MAS') {
          game[play.position] = 0
        } else {
          game[play.position] = 1
        }
      })

      const ret: ICamp ={
        C1: { L1: game[6], L2: game[3], L3: game[0] },
        C2: { L1: game[7], L2: game[4], L3: game[1] },
        C3: { L1: game[8], L2: game[5], L3: game[2] }
      }

      res.send(ret)

    } catch (error) {
      res.sendStatus(400).send(error)
    }
  }
}
