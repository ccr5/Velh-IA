import IChoices from "./iChoice"

export default class Choices implements IChoices {
  public readonly dateRequest: Date
  public readonly gameStatus: Array<number>
  public readonly timeToAct: number
  public readonly action: number

  public constructor(
    _dateRequest: Date,
    _gameStatus: Array<number>,
    _timeToAct: number,
    _action: number
  ) {
    this.dateRequest = _dateRequest
    this.gameStatus = _gameStatus
    this.timeToAct = _timeToAct
    this.action = _action
    Object.freeze(this)
  }
}
