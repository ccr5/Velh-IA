from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.agent.agent_dto import agent_to_entity, agent_to_adapter


def convert_mas(mas: MultiAgentSystemAdapter, to: str) -> MultiAgentSystemAdapter:

    if to == 'agent':
        return MultiAgentSystemAdapter(
            create_object(
                [
                    ('char', mas['char']),
                    ('family_leader', agent_to_entity(
                        mas['family_leader'])),
                    ('family_learner', agent_to_entity(
                        mas['family_learner'])),
                    ('education_leader', agent_to_entity(
                        mas['education_leader'])),
                    ('education_learner', agent_to_entity(
                        mas['education_learner'])),
                    ('religion_leader', agent_to_entity(
                        mas['religion_leader'])),
                    ('religion_learner', agent_to_entity(
                        mas['religion_learner']))
                ], 7
            )
        )
    else:
        return MultiAgentSystemAdapter(
            create_object(
                [
                    ('char', mas['char']),
                    ('family_leader', agent_to_adapter(
                        mas['family_leader'])),
                    ('family_learner', agent_to_adapter(
                        mas['family_learner'])),
                    ('education_leader', agent_to_adapter(
                        mas['education_leader'])),
                    ('education_learner', agent_to_adapter(
                        mas['education_learner'])),
                    ('religion_leader', agent_to_adapter(
                        mas['religion_leader'])),
                    ('religion_learner', agent_to_adapter(
                        mas['religion_learner']))
                ], 7
            )
        )
