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

export {IGeneralData, IPlayersData, ICamp}