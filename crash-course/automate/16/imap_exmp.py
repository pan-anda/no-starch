import imapclient, pyzmail, pprint
imapObj = imapclient.IMAPClient('imap.163.com', use_uid=True)
il = imapObj.login('panpanda5759@163.com', 'KZKSZZUVKIGFTRKY')
print(il)
pprint.pprint(imapObj.list_folders())    #查看文件夹列表
imapObj.select_folder('INBOX', readonly = True)
#UIDs = imapObj.search(['SINCE 29-jan-2022'])
#print(UIDs)












