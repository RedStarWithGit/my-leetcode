#!/usr/bin/env python
# coding=utf-8
# ============================================================

"""
leetcode problems工具
"""
import os.path
from pathlib import Path
from typing import Optional


def create_problem_source_code(
        problem_id: int,
        sub_dir: Optional[str] = 'common',
        page_size: int = 100
):
    dir_path = Path(__file__).parent.parent / 'problems'
    if sub_dir:
        dir_path = dir_path / sub_dir
    if page_size:
        start = problem_id // page_size * page_size
        end = start + page_size
        dir_path = dir_path / f"_{start:0>5}_{end:0>5}"

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

from typing import List


class Solution:
    pass
    

if __name__ == '__main__':
    solution = Solution

    for idx, (case_input, case_output) in enumerate([
        
    ]):
        print(f'case {idx}: {case_input}')
        print(f'\tpredict: {case_output}')
        print(f'\toutput: {solution()}')
""")
    else:
        print(f'file with problem id {problem_id} exists: {filepath}', )


if __name__ == '__main__':
    create_problem_source_code(124)
