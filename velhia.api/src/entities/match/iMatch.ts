import { winner } from "@shared/enums/winners";
import { status } from "@shared/enums/status";
import IPlay from "./iPlay";
import IPlayer from "./iPlayer";
import IMultAgentSystem from "./iMultAgentSystem"

export default interface IMatch {
  begin: Date,
  end?: Date,
  time: number,
  sa: IPlayer,
  mas: IMultAgentSystem,
  plays: IPlay[],
  status: status,
  winner?: winner
}