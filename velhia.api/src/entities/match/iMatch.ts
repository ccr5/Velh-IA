import { winner } from "@shared/enums/winners";
import { status } from "@shared/enums/status";
import IPlay from "./iPlay";
import IPlayer from "./iPlayer";

export default interface IMatch {
  begin: Date,
  end?: Date,
  time: number,
  sa: IPlayer,
  mas: IPlayer[]
  plays: IPlay[],
  status: status,
  winner?: winner
}