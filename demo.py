"""
Demo script for PyFlowchart DSL generation with code_line parameters.
"""
import sys, os
# 確保優先載入本地 workspace 中的 pyflowchart 而非全域安裝版本
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from pyflowchart.flowchart import Flowchart


def show_flow(code: str, desc: str = ""):
    print(f"=== {desc} ===")
    print("Code:")
    print(code)
    print("Flowchart DSL:")
    print(Flowchart.from_code(code, field="", inner=True,simplify=False, conds_align=True).flowchart())
    print()


if __name__ == "__main__":
    # 範例一：簡單賦值運算
    code1 = "x = 10\ny = x + 5"
    show_flow(code1, "Simple Assignment")

    # 範例二：函式定義與呼叫
    code2 = '''
def foo(a):
    return a * 2
'''  
    show_flow(code2, "Function foo")

    # 範例三：if-else 條件判斷
    code3 = '''
if a > 0:
    b = a
else:
    b = -a
'''
    show_flow(code3, "If-Else Statement")
    # 範例四：迴圈示例
    code4 = '''
for i in range(3):
    print(i)
'''
    show_flow(code4, "Loop Example (Simplify=True)")
    print("Flowchart DSL (Simplify=False):")
    print(Flowchart.from_code(code4, field="", inner=True, simplify=False).flowchart())
    print()

    # 範例五：階乘計算 (包含 input, loop, print)
    code5 = '''
a=int(input())
s=1
for i in range(1,a+1):
    s=s*i
print(s)
'''
    show_flow(code5, "Factorial Calculation")
