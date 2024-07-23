import numpy as np
import collections
from typing import List

Skill = collections.namedtuple('Skill', ['name', 'description'])

class SayCan:
    def __init__(self, skills: List[Skill]):
        """
        Initialize the SayCan algorithm.

        :param skills: A set of skills Π.
        """
        self.skills = skills

    def run(self, instruction: str, initial_state: int):
        """
        Run the SayCan algorithm.

        :param instruction: High-level instruction i.
        :param initial_state: Initial state s0.
        """
        n = 0
        current_skill = ""
        state = initial_state

        while current_skill != "done":
            combined_scores = []

            for skill in self.skills:
                # Evaluate scoring of LLM
                p_llm = self.llm(instruction, skill.description, current_skill)
                # Evaluate affordance function
                p_affordance = self.affordance_fn(state, skill.description)
                # Combine scores
                p_combined = p_affordance * p_llm
                combined_scores.append((p_combined, skill.name))

            # Select skill with highest combined score
            current_skill = max(combined_scores, key=lambda x: x[0])[1]

            # Execute skill in the environment, updating state
            state = self.execute_skill(current_skill, state)

            n += 1

            print(f"Step {n}: state = {state}, executing skill = {current_skill}")

    def execute_skill(self, skill: str, state: int) -> int:
        """
        Execute the skill in the environment. Update the state based on the skill.

        :param skill: The skill to execute.
        :param state: The current state.
        :return: Updated state after executing the skill.
        """
        # Placeholder for skill execution logic
        if skill == "skill1":
            new_state = state + 1
        elif skill == "skill2":
            new_state = state + 2
        elif skill == "skill3":
            new_state = state + 3
        elif skill == "skill4":
            new_state = state + 4
        elif skill == "done":
            new_state = state
        else:
            new_state = state  # No change if unknown skill
        return new_state

    def llm(self, instruction: str, description: str, current_skill: str) -> float:
        """
        Score the likelihood of the current skill for the given instruction.

        :param instruction: The instruction to compare.
        :param description: The description of the skill to compare.
        :param current_skill: The current skill to execute.
        :return: Likelihood score.
        """
        # TODO: use llm to calculate the score.
        return np.random.rand()

    def affordance_fn(self, state: int, description: str) -> float:
        """
        Quantify the likelihood of success to execute a task from the current state.

        :param state: The current observed state.
        :param description: The description of the skill to compare.
        :return: Affordance score.
        """
        # TODO: add an affordance function/equation.
        return np.random.rand()


if __name__ == "__main__":
    skills = [
        Skill(name="skill1", description="Execute Skill 1"),
        Skill(name="skill2", description="Execute Skill 2"),
        Skill(name="skill3", description="Execute Skill 3"),
        Skill(name="skill4", description="Execute Skill 4"),
        Skill(name="done", description="Done.")
    ]

    saycan = SayCan(skills)
    saycan.run("Do skill 1 after skill 3 and 2.", 0)
