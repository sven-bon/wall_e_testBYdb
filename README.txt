Last login: Wed Apr 13 09:29:42 on console
bwa081:~ sven$ cd ~/.ssh
bwa081:.ssh sven$ ls
key_backup	known_hosts
bwa081:.ssh sven$ cd
bwa081:~ sven$ cd ~
bwa081:~ sven$ ls
Desktop			Movies			Sites
Documents		Music			gitflow
Downloads		Pictures		发送注册信息
Library			Public
bwa081:~ sven$ ssh-add ~/.ssh/key_backup/id_rsa
Enter passphrase for /Users/sven/.ssh/key_backup/id_rsa: 
Bad passphrase, try again for /Users/sven/.ssh/key_backup/id_rsa: 
Bad passphrase, try again for /Users/sven/.ssh/key_backup/id_rsa: 
Bad passphrase, try again for /Users/sven/.ssh/key_backup/id_rsa: 
Bad passphrase, try again for /Users/sven/.ssh/key_backup/id_rsa: 
Identity added: /Users/sven/.ssh/key_backup/id_rsa (/Users/sven/.ssh/key_backup/id_rsa)
bwa081:~ sven$ cd ~ 
bwa081:~ sven$ ls
Desktop			Movies			Sites
Documents		Music			gitflow
Downloads		Pictures		发送注册信息
Library			Public
bwa081:~ sven$ public
-bash: public: command not found
bwa081:~ sven$ cd public
bwa081:public sven$ la
-bash: la: command not found
bwa081:public sven$ ls
Drop Box				github
OOo_3.2.1_MacOS_x86_install_en-US.dmg	workspace
eclipse
bwa081:public sven$ cd github
bwa081:github sven$ ls
test
bwa081:github sven$ cd test
bwa081:test sven$ ls
wall_e_testBYdb
bwa081:test sven$ cd wall_e_testBYdb
bwa081:wall_e_testBYdb sven$ ls
README		application.py	result2db.py
bwa081:wall_e_testBYdb sven$ git push origin develop
fatal: remote error: 
  You can't push to git://github.com/sven-bon/wall_e_testBYdb.git
  Use git@github.com:sven-bon/wall_e_testBYdb.git
bwa081:wall_e_testBYdb sven$ cd .
bwa081:wall_e_testBYdb sven$ cd ..
bwa081:test sven$ cd ..
bwa081:github sven$ git clone git@github.com:sven-bon/wall_e_testBYdb.git
Cloning into wall_e_testBYdb...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (6/6), done.
bwa081:github sven$ nano

  GNU nano 2.0.6                New Buffer                            Modified  

README


















                        [ XOFF ignored, mumble mumble ]
^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Page ^K Cut Text  ^C Cur Pos
^X Exit      ^J Justify   ^W Where Is  ^V Next Page ^U UnCut Text^T To Spell
