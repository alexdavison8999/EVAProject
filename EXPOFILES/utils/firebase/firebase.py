import firebase_admin
import firebase_admin.messaging
from firebase_admin import credentials
from google.oauth2.service_account import Credentials 
from google.auth.transport.requests import Request

from constants.auth import *

class FirebaseApp:
    def __init__(self):
        self.cred = credentials.Certificate(CERT_PATH)
        self.default_app = firebase_admin.initialize_app()
        self.messaging = firebase_admin.messaging
        self.scopes = ['https://www.googleapis.com/auth/firebase.messaging']

        # TOKEN IS A PER DEVICE REGISTRATION
        # When you load the mobile app, the home screen will display your appllication ID,
        # this will soon be changed so that you input this into the EVA, and then your device is registered to the EVA device 
        self.token = 'dPsQDsY6Qvqsyi76XvlT3C:APA91bGjZfUq7VpRoi7ZeUvt03Nq9gUmTYIJKYsN3zPfQYIh7m0DnbF8gt8fu-TFQY7tuCp7jBGJJllv87QGPEHHTgYBf7KQZ2GC5OmgBacVAG8E8nmTBnDLgoBWqTr2NXW4Esb0iwgq'
        self.headers = {
            'Authorization': 'Bearer ' + self._get_access_token(),
            'Content-Type': 'application/json; UTF-8',
        }
        
        return

    def _get_access_token(self):
        """Retrieve a valid access token that can be used to authorize requests.

        :return: Access token.
        """
        service_data_path = CERT_PATH

        credentials: Credentials = Credentials.from_service_account_file(
            filename=service_data_path, scopes=self.scopes)
        request = Request()
        credentials.refresh(request)
        print(credentials.token)
        return credentials.token

    def send_notification(self, title: str, body: str, data):
        """
        Accepts title and body strings, and will push it to a device, 
        with an optional data field to send a payload 
        """

        if data:
            new_notif = self.messaging.Message(
                headers=self.headers,
                token=self.token,
                notification={
                    'title': title,
                    'body': body,
                },
                data=data,
                android={ # TODO: This must be an androidConfig Instance!
                    "direct_boot_ok": True,
                },
            )
        else:
            new_notif = self.messaging.Message(
                token=self.token,
                notification={
                    'title': title,
                    'body': body,
                },
                android={
                    "direct_boot_ok": True,
                },
            )

        response = self.messaging.send(new_notif)

        # Response should be a message ID string
        print('Notificaation: ', response)

        return


    def send_message(self, data):
        """
        Accepts a dictionary of strings, and will send it to a device
        """
        new_message = self.messaging.Message(
            token=self.token,
            data=data
        )

        response = self.messaging.send(new_message)

        # Response should be a message ID string
        print('Message: ', response)

        return

    