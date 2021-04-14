import re


def solution(skill, skill_trees):
    return sum(skill.startswith(''.join(re.compile(r'['+skill+']').findall(s))) for s in skill_trees)
