import IAlgorithm from './iAlgorithm'

export default class Algorithm implements IAlgorithm{
  public readonly birth: Date
  public readonly matchs: number
  public readonly victories: number
  public readonly defeats: number
  public readonly draw: number

  public constructor (
    _birth: Date,
    _matchs: number,
    _victories: number,
    _defeats: number,
    _draw: number
  ) {
    this.birth = _birth
    this.matchs = _matchs
    this.victories = _victories
    this.defeats = _defeats
    this.draw = _draw
    Object.freeze(this)
  }
}