import inspect
import pyflowchart.flowchart as fc_mod
from pyflowchart.flowchart import Flowchart

print("pyflowchart module file:", fc_mod.__file__)
print("Flowchart class loaded from:", inspect.getfile(Flowchart))
