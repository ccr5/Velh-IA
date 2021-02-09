import { winner } from "@shared/enums/winners";
import { status } from "@shared/enums/status";
import IMultiAgentSystem from "./iMultiAgentSystem";
import IPlay from "./iPlay";
import IPlayer from "./iPlayer";

export default interface IMatch {
  begin: Date,
  end?: Date,
  time: number,
  sa: IPlayer,
  mas: IMultiAgentSystem
  plays: IPlay[],
  status: status,
  winner?: winner
}