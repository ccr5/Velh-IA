import json
from typing import NoReturn
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.agent.agent_database import update_agent
from usecases.database.database_types import DatabaseRepositoryType
from shared.errors.handler.mas.update_mas_error import UpdateMASError


def update_mas(family: DatabaseRepositoryType,
               religion: DatabaseRepositoryType,
               education: DatabaseRepositoryType,
               mas: MultiAgentSystemAdapter) -> NoReturn:
    """
    Update all multi agent system
    :param vlh: `Velhia` Velhia obj
    :param mas: `Multi Agent System` Multi Agent System obj 
    """

    try:

        update_agent(family, mas['family_leader'])
        update_agent(family, mas['family_learner'])
        update_agent(religion, mas['religion_leader'])
        update_agent(religion, mas['religion_learner'])
        update_agent(education, mas['education_leader'])
        update_agent(education, mas['education_learner'])

    except:
        raise UpdateMASError
