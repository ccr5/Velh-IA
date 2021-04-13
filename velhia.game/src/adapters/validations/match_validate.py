from typing import NoReturn, List
from adapters.controllers.match_controller import check_win
from entities.match.match import Match
from shared.types.game_status import GameStatus
from shared.errors.validation.validation_error import ValidationError
from shared.errors.validation.match.match_pendent_error import CurrentyMatchIsNotPendent
from shared.errors.validation.match.match_status_error import PreviousMatchHasInvalidStatus
from shared.errors.validation.match.currenty_match_id_error import CurrentyMatchIdIsDifferent
from shared.errors.validation.match.previous_match_id_error import PreviousMatchIdIsDifferent
from shared.errors.validation.match.currenty_match_game_error import CurrentMatchGameIsDifferent
from shared.errors.validation.match.previous_match_game_error import PreviousMatchGameIsDifferent


def check_match_status(match: Match, match_type: str, status: List[str]) -> NoReturn:

    if 'WINNER' in status and match['status'] == 'WINNER' and match['winner'] in ['SA', 'MAS'] and match_type == 'previous':
        pass
    elif 'DRAW' in status and match['status'] == 'DRAW' and len(match['plays']) == 9 and match_type == 'previous':
        pass
    elif 'PENDENT' in status and match['status'] == 'PENDENT' and match_type == 'current':
        pass
    else:
        raise SystemError
