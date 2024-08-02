#!/usr/bin/env python
# coding=utf-8
# ============================================================

"""
leetcode problems工具
"""
import os.path
from pathlib import Path
from typing import Optional


def create_problem_source_code(problem_id: int, sub_dir: Optional[str] = None):
    dir_path = Path(__file__).parent.parent / 'problems'
    if sub_dir:
        dir_path = dir_path / sub_dir
    filepath = str(dir_path / f'{problem_id:0>5}.py')
    if not os.path.exists(filepath):
        os.makedirs(dir_path, exist_ok=True)
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
