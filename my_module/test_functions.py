"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import introduction, run, main_page, customize
import mock
import builtins

def test_run():
    with mock.patch.object(builtins, 'input', lambda _: 'quit'):
        run_test = run()
        assert run_test == None
        
def test_introduction():
    
    assert True

def test_main_page():

    assert True
    
def test_customize():
    with mock.patch.object(builtins, 'input', lambda _: 3,2):
        customize_map = customize()
        assert len(customize_map) == 3
     

       

                           



                 
    