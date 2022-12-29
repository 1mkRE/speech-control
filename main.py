from speech_txt import *
from time import sleep


running = False
tmp_status = False
voice_record = None

if __name__ == "__main__":
    sp = Speech('Ariane')
    while True:
        sleep(1)
        if running:
            if not tmp_status:
                sp.response_audio('hello how can I help you?')
                tmp_status = True
            print('Running')
            voice_record = sp.get_speech()
            running = sp.response_speech(voice_record, running)
        else:
            if tmp_status:
                sp.response_audio('Bye I am going in sleep mode')
                tmp_status = False
            print('Sleeping')
            voice_record = sp.get_speech()
            running = sp.response_speech(voice_record, running)