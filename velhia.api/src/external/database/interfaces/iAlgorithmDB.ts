import IAlgorithm from "@entities/algorithm/iAlgorithm";
import { Document } from 'mongoose'

export default interface IAlgorithmDB extends IAlgorithm, Document{

} 