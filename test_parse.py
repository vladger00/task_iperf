import pytest
import parser

class TestSuite():

    @pytest.mark.parametrize("test_value", parser.get_test_values('iperf3.txt'))
    def test_transfer(self, test_value):
        assert test_value['Transfer'] > 4.8 and test_value['Bitrate'] > 40.2

