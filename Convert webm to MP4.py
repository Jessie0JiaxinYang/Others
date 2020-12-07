# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:48:34 2020

@author: jiaxi
"""
# convert from webm to mp4
# http://www.gerongcun.xyz/blog/2020/7f326749/


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
ffm.convert_webm_mp4_subprocess(r'C:\Users\jiaxi\test.webm', r'C:\Users\jiaxi\test1.mp4')

ffm.convert_webm_mp4_module(r'D:\videos\Research Community\2020 1204\Original\Not MP4\26Efficient Exact Verification of Binarized Neural Networks.webm', r'D:\videos\Research Community\2020 1204\Original\Not MP4\test.mp4')
