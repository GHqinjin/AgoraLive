#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os

def main():
    keystore = ""
    password = ""
    alias = ""
    bugly = ""

    if "keystore" in os.environ:
        keystore = os.environ["keystore"]

    if "password" in os.environ:
        password = os.environ["password"]

    if "alias" in os.environ:
        alias = os.environ["alias"]

    if "bugly" in os.environ:
        alias = os.environ["alias"]

    f1 = open("./app/build.gradle", 'r+')
    content = f1.read()
    contentNew = re.sub(r'azure_keystore_file', keystore, content)
    contentNew = re.sub(r'azureKeystorePassword', password, contentNew)
    contentNew = re.sub(r'azure_keystore_alias', alias, contentNew)
    f1.seek(0)
    f1.write(contentNew)
    f1.truncate()

    f2 = open("./app/src/main/res/values/strings.xml", 'r+')
    content = f2.read();
    contentNew = re.sub(r'<string name="bugly_app_id"></string>', '<string name="bugly_app_id">' + bugly + '</string>', content)
    f2.seek(0)
    f1.write(contentNew)
    f2.truncate()


if __name__ == "__main__":
    main()