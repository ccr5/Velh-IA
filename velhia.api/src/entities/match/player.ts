import { symbolEnvironment } from "src/shared/enums/symbols";
import IPlayer from "./iPlayer";

export default class Player implements IPlayer {
  public readonly playerId: string
  public readonly symbol: symbolEnvironment

  public constructor(
    _playerId: string,
    _symbol: symbolEnvironment
  ) {
    this.playerId = _playerId
    this.symbol = _symbol
    Object.freeze(this)
  }
}