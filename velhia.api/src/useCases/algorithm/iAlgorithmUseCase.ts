import Algorithm from 'src/entities/algorithm/algorithm'

export default interface IAlgorithmUseCase {
  getAlgorithm(
    filters:string | undefined, 
    fields: string | undefined, 
    sort: string | undefined, 
    offset: string | undefined, 
    limit: string | undefined
  ): Promise<Algorithm[] | null>
  createAlgorithm(data: Algorithm[]): Promise<Algorithm[]>
  updateAlgorithm(id: string, data: Algorithm): Promise<Algorithm | null>
  deleteAlgorithm(id: string): Promise<Algorithm | null>
}