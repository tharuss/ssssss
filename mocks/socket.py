from src.configuration import Configuration
import random

class socket:
    def socket():
        return socket()

    def connect(self, host_port_tuple):
        print(f'Fake socket connected: {host_port_tuple}')

    def send(self, string):
        print(f'Fake socket was sent: {string}')

    def setblocking(self, int):
        print(f'Fake socket set blocking: {int}')

    def recv(self, int):
        return fake_reception();

class fake_reception:

        def decode(fake_reception, encoding):
            log = fake_reception.dont_print
            config = Configuration('mocks/config.txt', log)
            conn = config.get_connection_constants()
            chan = conn['channel'][1:]
            bot = conn['bot_name']
            admin = random.choice(config.get_admins())

            channel_message = f':{chan}!{chan}@{chan}.tmi.twitch.tv PRIVMSG #{chan} :This is the Trivvy Channel Speaking: Be excellent to each other.\r\n'
            user_message = f':happy_lass!happy_lass@happy_lass.tmi.twitch.tv PRIVMSG #{chan} :Woot!'
            user_answer = f':trivvy_lad!trivvy_lad@trivvy_lad.tmi.twitch.tv PRIVMSG #{chan} :The Great Answer 42'
            user_command = f':trivvy_fan!trivvy_fan@trivvy_fan.tmi.twitch.tv PRIVMSG #{chan} :!score'
            admin_command = f':{admin}!{admin}@{admin}.tmi.twitch.tv PRIVMSG #{chan} :!loadconfig'
            self_message = f':{bot}!{bot}@{bot}.tmi.twitch.tv PRIVMSG #{chan} :You shouldn\'t be seeing this message'
            ping_message = 'PING :tmi.twitch.tv\r\n'
            empty_message = ''

            messages = [channel_message, user_message, user_answer, user_command, admin_command, self_message, ping_message, empty_message]

            return random.choice(messages)

        def dont_print(fake_reception, string):
            pass