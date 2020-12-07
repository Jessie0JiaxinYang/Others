

import subprocess
import ffmpeg

class FFMConvertor:
    
    def convert_webm_mp4_subprocess(self, input_file, output_file):
        try:
            command = 'ffmpeg -i ' + input_file +' '+ output_file
            subprocess.run(command)
        except:print('Some Exception')
        
    def convert_webm_mp4_module(self, input_file, output_file):
        try:
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file)
            ffmpeg.run(stream)
        except:print('Some Exception')

ffm = FFMConvertor()
ffm.convert_webm_mp4_subprocess(r'*.webm', r'*.mp4')

# ffm.convert_webm_mp4_module(r*.webm', r'*.mp4')
