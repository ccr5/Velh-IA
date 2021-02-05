import { environmentReaction } from "src/shared/enums/environmentReaction"
import Choices from "./choice"
import IMemory from "./iMemory"

export default class Memory implements IMemory {
  public readonly matchId: string
  public readonly isLearner: boolean
  public choices: Choices[]
  public environmentReaction: environmentReaction

  public constructor (
    _matchId: string,
    _isLearner: boolean,
    _choices: Choices[],
    _environmentReaction: environmentReaction
  ) {
    this.matchId = _matchId
    this.isLearner = _isLearner
    this.choices = _choices
    this.environmentReaction = _environmentReaction
    Object.freeze(this)
  }
}
