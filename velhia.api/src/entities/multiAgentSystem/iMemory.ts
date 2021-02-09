import { environmentReaction } from "@shared/enums/environmentReaction";
import IChoices from "./iChoice";

export default interface IMemory {
  matchId: string,
  isLearner: boolean,
  choices: IChoices[],
  environmentReaction: environmentReaction
}