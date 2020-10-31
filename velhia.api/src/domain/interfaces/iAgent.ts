import { Document } from 'mongoose'
import { IMemory } from '@interfaces/iMemory'

interface IAgent extends Document {
  progenitor: string,
  birth: Date,
  becomeLeader: Date,
  death: Date,
  life: number,
  memory: IMemory[],
  matchsAsLearner: number,
  matchsAsLeader: number,
  victories: number,
  defeats: number,
  draw: number
}

interface IAgentRepository {
  getAllAgent(): Promise<IAgent[] | null>
  getOneAgent(id: string): Promise<IAgent | null>
  getLastAgent(limit: number): Promise<IAgent[] | null>
  createAgent(data: IAgent[]): Promise<IAgent[]>
  updateAgent(id: string, data: IAgent): Promise<IAgent | null>
  deleteAgent(id: string): Promise<IAgent | null>
}

export { IAgent, IAgentRepository }
