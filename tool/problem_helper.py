#!/usr/bin/env python
# coding=utf-8
# ============================================================

"""
leetcode problems工具
"""
import os.path
from pathlib import Path


def create_problem_source_code(problem_id: int):
    filepath = str(Path(__file__).parent.parent / 'problems' / f'{problem_id:0>5}.py')
    if not os.path.exists(filepath):
        with open(filepath, mode='w', encoding='utf-8') as f:
            f.write(
                """#!/usr/bin/env python
# coding=utf-8
# ============================================================
# 
# ============================================================


class Solution:
    pass
    

if __name__ == '__main__':
    solution = Solution

    for idx, (i, o) in enumerate([
        
    ]):
        print(f'case {idx}: {i}')
        print(f'\tpredict: {o}')
        
""")
    else:
        print(f'file with problem id {problem_id} exists: {filepath}', )


if __name__ == '__main__':
    create_problem_source_code(124)
