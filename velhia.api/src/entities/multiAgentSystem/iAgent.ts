import IMemory from "./iMemory";

export default interface IAgent {
  progenitor: string,
  birth: Date,
  becomeLeader?: Date,
  death?: Date,
  life: number,
  memory: IMemory[],
  matchsAsLearner: number,
  matchsAsLeader: number,
  victories: number,
  defeats: number,
  draw: number
}