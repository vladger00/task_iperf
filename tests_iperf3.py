
class TestSuite():

    def test_iperf3_server_connection(self, server):
        error = server
        print("      > Received from fixture server is: {}".format(error))
        assert ('iperf3: error - unable to start listener for connections: Address already in use' not in error)

    def test_iperf3_client_connection(self, client):
        error = client
        print("      > Received from fixture client is: {}".format(error))
        assert ('iperf3: error - the server is busy running a test. try again later' not in error)




