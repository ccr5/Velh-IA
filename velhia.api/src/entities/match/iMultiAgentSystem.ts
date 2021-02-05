import IPlayer from "./iPlayer";

export default interface IMultiAgentSystem {
  family: IPlayer[],
  religion: IPlayer[],
  education: IPlayer[]
}