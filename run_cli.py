#!/usr/bin/env python3
"""CLI wrapper for grok_register_ttk.py — stubs tkinter so GUI mode isn't required."""
import sys
import os

# Change to script directory so config.json is found
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Stub tkinter
class _Fake:
    def __init__(self, *a, **kw): pass
    def __getattr__(self, n): return _Fake()
    def __call__(self, *a, **kw): return _Fake()

_fake_mod = _Fake()
_tk_names = 'NORMAL DISABLED ACTIVE END INSERT LEFT RIGHT TOP BOTTOM X Y BOTH HORIZONTAL VERTICAL WORD CHAR CENTER W E S N EW NS SINGLE BROWSE EXTENDED SUNKEN RAISED GROOVE RIDGE FLAT SOLID'.split()
sys.modules['tkinter'] = _fake_mod
for n in _tk_names:
    setattr(_fake_mod, n, n)
sys.modules['tkinter.ttk'] = _Fake()
sys.modules['tkinter.messagebox'] = _Fake()
sys.modules['tkinter.scrolledtext'] = _Fake()

import grok_register_ttk as mod
mod.main()
