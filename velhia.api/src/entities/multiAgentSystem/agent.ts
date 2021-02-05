import IAgent from "./iAgent"
import Memory from "./memory"

export default class Agent implements IAgent{
  public readonly progenitor: string
  public readonly birth: Date
  public becomeLeader?: Date
  public death?: Date
  public life: number
  public memory: Memory[]
  public matchsAsLearner: number
  public matchsAsLeader: number
  public victories: number
  public defeats: number
  public draw: number

  public constructor (
    _progenitor: string,
    _birth: Date,
    _becomeLeader: Date,
    _death: Date,
    _life: number,
    _memory: Memory[],
    _matchsAsLearner: number,
    _matchsAsLeader: number,
    _victories: number,
    _defeats: number,
    _draw: number
  ) {
    this.progenitor = _progenitor
    this.birth = _birth
    this.becomeLeader = _becomeLeader
    this.death = _death
    this.life = _life
    this.memory = _memory
    this.matchsAsLearner = _matchsAsLearner
    this.matchsAsLeader = _matchsAsLeader
    this.victories = _victories
    this.defeats = _defeats
    this.draw = _draw
    Object.freeze(this)
  }
}