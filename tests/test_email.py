import unittest
from unittest.mock import patch, MagicMock
from src.email_service import handle_email, send_email_securely

class TestEmailService(unittest.TestCase):
    
    @patch('src.email_service.os.environ.get')
    @patch('src.email_service.smtplib.SMTP_SSL')
    def test_send_email_securely_success(self, mock_smtp_ssl, mock_env_get):
        # Setup mocks
        mock_env_get.side_effect = lambda k, d=None: "dummy" if k in ["EMAIL_ADDRESS", "EMAIL_PASSWORD"] else d
        mock_smtp_instance = MagicMock()
        mock_smtp_ssl.return_value.__enter__.return_value = mock_smtp_instance

        # Execute
        result = send_email_securely("recipient@example.com", "Test Subject", "Test Body")

        # Verify
        self.assertTrue(result)
        mock_smtp_instance.login.assert_called_once_with("dummy", "dummy")
        mock_smtp_instance.send_message.assert_called_once()
        
    @patch('src.email_service.os.environ.get')
    def test_send_email_missing_credentials(self, mock_env_get):
        # Setup mocks to return None for credentials
        mock_env_get.return_value = None
        
        # Execute (should fail gracefully)
        result = send_email_securely("recipient@example.com", "Test Subject", "Test Body")
        
        # Verify
        self.assertFalse(result)

    @patch('src.email_service.send_email_securely')
    @patch('src.email_service.listen')
    @patch('src.email_service.speak')
    def test_handle_email_successful_flow(self, mock_speak, mock_listen, mock_send):
        # Simulate user responses: Name -> Subject -> Body -> Yes
        mock_listen.side_effect = ["test", "Project Update", "The project is going well", "yes please"]
        mock_send.return_value = True
        
        handle_email()
        
        # Verify send was called with correct data
        mock_send.assert_called_once_with("testrecipient@example.com", "Project Update", "The project is going well")

    @patch('src.email_service.send_email_securely')
    @patch('src.email_service.listen')
    @patch('src.email_service.speak')
    def test_handle_email_cancelled_flow(self, mock_speak, mock_listen, mock_send):
        # Simulate user responses: Name -> Subject -> Body -> NO
        mock_listen.side_effect = ["test", "Project Update", "The project is going well", "no"]
        
        handle_email()
        
        # Verify send was NEVER called
        mock_send.assert_not_called()

if __name__ == '__main__':
    unittest.main()
