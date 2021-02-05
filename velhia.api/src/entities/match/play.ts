import IPlay from "./iPlay"

export default class Play implements IPlay {
  public readonly seq: number
  public readonly player: string
  public readonly time: number
  public readonly position: number

  public constructor(
    _seq: number,
    _player: string,
    _time: number,
    _position: number
  ) {
    this.seq = _seq
    this.player = _player
    this.time = _time
    this.position = _position
    Object.freeze(this)
  }
}