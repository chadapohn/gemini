import os.path
from collections import OrderedDict

from gemini import iupac
from gemini.config import read_gemini_config

def test_iupac():
    obs = [iupac.lookup("C"),iupac.lookup("G"),iupac.lookup("R")]
    exp = [["C"],["G"],["A", "G"]]
    assert obs == exp
