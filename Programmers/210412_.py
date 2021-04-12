import re


def solution(skill, skill_trees):
    return sum(1 for s in skill_trees if skill.startswith(''.join(re.compile(r'['+skill+']').findall(s))))
