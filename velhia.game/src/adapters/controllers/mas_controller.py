import random as r
from datetime import datetime
from typing import Callable
from usecases.agent.agent_use_cases import remember, memorize, learn
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from shared.types.game_status import GameStatus
from shared.errors.multi_agent_system.play_error import MASPlayError


def play_mas(mas: MultiAgentSystemAdapter, game_status: GameStatus):
    """
    Choose a position to play
    :param match: `Match` a Match obj
    :param game_status: game status
    """

    def get_valid_position(fn: Callable) -> int:

        position: int = fn()
        if game_status[position] == -1:
            return position
        else:
            return get_valid_position(fn)

    family_start = datetime.now()
    family_position: int = get_valid_position(
        remember(mas['family_leader'], game_status)
    )
    family_end = datetime.now()

    education_start = datetime.now()
    education_position: int = get_valid_position(
        remember(mas['education_leader'], game_status)
    )
    education_end = datetime.now()

    religion_start = datetime.now()
    religion_position: int = get_valid_position(
        remember(mas['religion_leader'], game_status)
    )
    religion_end = datetime.now()

    if family_position == education_position == religion_position:
        family_leader.memorize(
            match, game_status, family_start, family_end, family_position)
        family_learner.learn(match, game_status, family_position)

        education_leader.memorize(
            match, game_status, education_start, education_end, education_position)
        education_learner.learn(
            match, game_status, education_position)

        religion_leader.memorize(
            match, game_status, religion_start, religion_end, religion_position)
        religion_learner.learn(
            match, game_status, religion_position)

        return education_position

    elif family_position == education_position:
        family_leader.memorize(
            match, game_status, family_start, family_end, family_position)
        family_learner.learn(match, game_status, family_position)

        education_leader.memorize(
            match, game_status, education_start, education_end, education_position)
        education_learner.learn(
            match, game_status, education_position)

        return family_position

    elif family_position == religion_position:
        family_leader.memorize(
            match, game_status, family_start, family_end, family_position)
        family_learner.learn(match, game_status, family_position)

        religion_leader.memorize(
            match, game_status, religion_start, religion_end, religion_position)
        religion_learner.learn(
            match, game_status, religion_position)

        return religion_position

    elif education_position == religion_position:
        religion_leader.memorize(
            match, game_status, religion_start, religion_end, religion_position)
        religion_learner.learn(match, game_status, religion_position)

        education_leader.memorize(
            match, game_status, education_start, education_end, education_position)
        education_learner.learn(
            match, game_status, education_position)

        return education_position

    else:
        position = r.choice(
            [family_position, education_position, religion_position])

        if position == family_position:
            family_leader.memorize(
                match, game_status, family_start, family_end, family_position)
            family_learner.learn(match, game_status, family_position)

        elif position == education_position:
            education_leader.memorize(
                match, game_status, education_start, education_end, education_position)
            education_learner.learn(
                match, game_status, education_position)

        elif position == religion_position:
            religion_leader.memorize(
                match, game_status, religion_start, religion_end, religion_position)
            religion_learner.learn(
                match, game_status, religion_position)
        else:
            raise MASPlayError

        return position
