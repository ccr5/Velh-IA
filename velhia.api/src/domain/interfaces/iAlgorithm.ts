import { Document } from 'mongoose'
import { IMemory } from '@interfaces/iMemory'

interface IAlgorithm extends Document {
  birth: Date,
  memory: IMemory[]
  matchs: number,
  victories: number,
  defeats: number,
  draw: number
}

interface IAlgorithmRepository {
  getAllAlgorithm(): Promise<IAlgorithm[] | null>
  getOneAlgorithm(id: string): Promise<IAlgorithm | null>
  getLastAlgorithm(limit: number): Promise<IAlgorithm[] | null>
  createAlgorithm(data: IAlgorithm[]): Promise<IAlgorithm[]>
  updateAlgorithm(id: string, data: IAlgorithm): Promise<IAlgorithm | null>
  deleteAlgorithm(id: string): Promise<IAlgorithm | null>
}

export { IAlgorithm, IAlgorithmRepository }
