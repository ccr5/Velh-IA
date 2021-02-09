import IAlgorithm from '@entities/algorithm/iAlgorithm'

export default interface IAlgorithmRepository {
  getAlgorithm(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined
  ): Promise<IAlgorithm[] | null>
  createAlgorithm(data: IAlgorithm[]): Promise<IAlgorithm[]>
  updateAlgorithm(id: string, data: IAlgorithm): Promise<IAlgorithm | null>
  deleteAlgorithm(id: string): Promise<IAlgorithm | null>
}