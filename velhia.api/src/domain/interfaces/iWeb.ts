interface IGeneralData {
  begin: Date,
  nMatchs: number,
  nDraws: number
}

interface IPlayersData {
  wins: number,
  percent: number
}

interface ICamp {
  C1: {
    L1: number,
    L2: number,
    L3: number
  },
  C2: {
    L1: number,
    L2: number,
    L3: number
  },
  C3: {
    L1: number,
    L2: number,
    L3: number
  }
}

interface IResume {
  institution: string,
  id: string,
  generation: string,
  progenitor: string,
  life: number,
  memories: number,
  matchAsLearner: number,
  matchAsLeader: number,
  victories: number,
  defeats: number,
  draws: number
}

interface IMAS {
  family: IResume,
  education: IResume,
  religion: IResume
}

export {IGeneralData, IPlayersData, ICamp, IMAS}