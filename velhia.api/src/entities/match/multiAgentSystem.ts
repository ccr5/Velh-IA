import IMultiAgentSystem from "./iMultiAgentSystem";
import Player from "./player";

export default class MultiAgentSystem implements IMultiAgentSystem{
  public readonly religion: Player[]
  public readonly education: Player[]
  public readonly family: Player[]

  public constructor (
    _family: Player[],
    _religion: Player[],
    _education: Player[]
  ) {
    this.family = _family
    this.religion = _religion
    this.education = _education
    Object.freeze(this)
  }
  
}