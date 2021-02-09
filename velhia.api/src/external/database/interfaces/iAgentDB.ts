import IAlgorithm from "src/entities/algorithm/iAlgorithm";
import { Document } from 'mongoose'
import IAgent from "@entities/multiAgentSystem/iAgent";

export default interface iAgentDB extends IAgent, Document {

}