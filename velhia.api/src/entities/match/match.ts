import { status } from "src/shared/enums/status";
import { winner } from "src/shared/enums/winners";
import Player from "./player";
import Play from "./play";
import MultiAgentSystem from "./multiAgentSystem";
import IMatch from "./iMatch";

export default class Match implements IMatch {
  public readonly begin: Date
  public end?: Date
  public time: number
  public readonly sa: Player
  public readonly mas: MultiAgentSystem
  public plays: Play[]
  public status: status
  public winner?: winner

  public constructor (
    _begin: Date,
    _end: Date,
    _time: number,
    _sa: Player,
    _mas: MultiAgentSystem,
    _plays: Play[],
    _status: status,
    _winner?: winner
  ) {
    this.begin = _begin
    this.end = _end
    this.time = _time
    this.sa = _sa
    this.mas = _mas
    this.plays = _plays
    this.status = _status
    this.winner = _winner
    Object.freeze(this)
  }
}