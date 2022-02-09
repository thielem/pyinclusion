import unittest
import numpy as np
import pandas as pd
import pytest
from py_inclusion.core import gen_graph


def gen_test_df():
    num_sub = 1
    pid_col = np.random.choice(1000, num_sub, replace=False)
    calibration = np.random.rand(num_sub) < .9
    summary = np.random.rand(num_sub) < .9
    duration = np.random.rand(num_sub) < .9

    test_df = pd.DataFrame({'pid': pid_col,
                            'calibration': calibration,
                            'summary': summary,
                            'duration': duration})
    return test_df


class TestSimple(unittest.TestCase):

    def test_simple_df(self):
        test_df = gen_test_df()
        gen_graph(test_df)

    def test_simple_df_1(self):
        test_df = gen_test_df()
        gen_graph(test_df, start_node_text="My subjects")

    def test_simple_df_2(self):
        test_df = gen_test_df()
        gen_graph(test_df, end_node_text="My subjects")

    def test_simple_df_all(self):
        test_df = gen_test_df()
        condtion_text = ["calibration", "summary", "duration"]
        exclusion_text = ["calibration", "summary", "duration"]
        gen_graph(test_df,  start_node_text="My subjects",
                  end_node_text="My subjects", condition_text=condtion_text,
                  exclusion_text=exclusion_text)

    @pytest.mark.xfail(reason="Mismatched label length")
    def test_mismatch_label_len(self):
        test_df = gen_test_df()
        condtion_text = ["calibration", "summary", "duration"]
        exclusion_text = ["calibration", "summary"]
        gen_graph(test_df,  start_node_text="My subjects",
                  end_node_text="My subjects", condition_text=condtion_text,
                  exclusion_text=exclusion_text)


if __name__ == '__main__':
    unittest.main()
