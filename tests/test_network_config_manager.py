from network_config_manager import NetworkConfigManager

class TestNetworkConfigManager:
    def setup_method(self, method):
        self.config_manager = NetworkConfigManager()
        self.config_manager.connect()  

        self.config_manager.update_hostname("1")
        self.config_manager.update_interface_state("up")
        self.config_manager.update_response_prefix("Standard Response")

    def teardown_method(self, method):
        self.config_manager.disconnect()


    def test_show_hostname_default(self):
        result = self.config_manager.show_hostname()
        assert result == "hostname: 1", f"Förväntade 'hostname: 1', men fick {result}"

    def test_update_hostname(self):
        new_value = "100"
        self.config_manager.update_hostname(new_value)
        result = self.config_manager.show_hostname()
        assert result == "hostname: 100", f"Förväntade 'hostname: 100', men fick {result}"   
        
    def test_show_interface_state_default(self):
        result = self.config_manager.show_interface_state()
        assert result == "interface_state: up", f"Förväntade 'interface_state: up', men fick {result}"

    def test_update_interface_state(self):
        new_value = "down"
        self.config_manager.update_interface_state(new_value)
        result = self.config_manager.show_interface_state()
        assert result == "interface_state: down", f"Förväntade 'interface_state: down', men fick {result}"

    def test_show_response_prefix_default(self):
        result = self.config_manager.show_response_prefix() 
        assert result == "response_prefix: Standard Response", f"Förväntade 'response_prefix: Standard Response', men fick {result}"

    def test_update_response_prefix(self):
        new_value = "Abnormal Response"
        self.config_manager.update_response_prefix(new_value)
        result = self.config_manager.show_response_prefix()
        assert result == "response_prefix: Abnormal Response", f"Förväntade 'response_prefix: Abnormal Response', men fick {result}"

