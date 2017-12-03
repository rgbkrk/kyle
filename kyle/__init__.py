#!/usr/bin/env python

# -*- coding: utf-8 -*-
'''Kyle
'''

__img__ = """\
l::l;:oxxxxdxxd:........':,..'...',co;.;:;c;.. ......',:cc:;..,';,':oloc,'',,,,,,,;llc..,,,,:odoc;:c;...   ..:';',,,. .'l:',
ol:cloooxkdllo;,'''......:;'',..,;'.:;';:c;:'.....',,,,'::;'';l:;;;,dc:::''''.';,.'ll;...'',;;:loclc'...  ...'...'.. ..';cl;
c;',c:,'ldl,,;'..'',,'.....',,,'''...,,';:...'..;,:o:,,',,'.:l;,;c;'lc,.,,,'.'';:,'':;,,.... ..:lc:,....'....... ........;d:
l:;.;:c;llc;','...............'','.'';...,''....:clx:,;'.'',c;...,,',''.,:,..''',,',::,,'''...;oo:,........     .. ..... .:,
c;cc;:clodddo:,'''..';;,,..  .....''......,,'..,;codc:c,',:;;;;.,:'.....,;,..''''..',,;,''...',;;;,.',,'.....,;;,.....   ...
:;;;coccclcclc;;,,',::;,.  .............'........:oc,.,,;cccoxxc,'.....';c;.......,;:cc:,....','...'''......;looc,,.  ..   .
;'.'cc,';:,.;::c,..  ....  ...  ..   ';......    .;''.',:lcooxxc........,,....':ccccll:,.....','............,codlcl;.     ..
;o;,llc,';;:;:l:,''     ..'',,. .....;;.....     ......:,..'lkx:..   ...,,.',:lllccoo:,.  .,:;:;'..''......';::cccoc,.   ...
,olccol:''...,:;',,....'',,.....  ...,'.....     .. ...,... ,ddl,.   ..',,,;clllll:,.....,:clcc,..,:,..........,';l::.   ...
,cloodl......';;;'',;;,.. .....',''....... ......''.........;;..       ....'''''.......':;;;cc:'.';;,'...'.....'';:,'..   ..
;,;llcl'','.....,;'........;,'',:;,... ......'...'...............           .........'';;,,:c;''......'..'....';,......    .
,,,:;:ll:;'... ...'.        . .....     .....'..,'. ..........'.'...  ...     ..''.......'','......':c:,'','...,;:,'.'..    
''''';cdl:;.'...''.,'...       . ...    .,,,:xc......'',,'''.....,;'..'''..............'...'',,',:::oo:,;coc:c.';lcccc:.    
'...,;;dl:;'........';cc;.        ..     .'.,:;.....;:'.''..... ...',',;;,....':,..'',,,','',,,:loollol;',ldc;'.':oooolc.   
;'..:c:llc;'''''......'.....      .      .'''.,:;'. .'.;;'.....   ..'.,,,,'''..',,,',,;;:::;;,;;;:cllll:;',cc;,',cllcccc..  
,,,.'..;c;.,,''.....''.          ....     .....:,,. ....''..     .''''''..,,,,;c,,;,,;cldxxl;;;;:c:clllc:;;l:;,;:;;;;;:c..  
..,...,c;'';,';,'''.......      .'...,''''. ,'...c'   .....     .',',,,,,..,;;:c;;;;;oxdkKXklc::cc::lolollxOdc,.''..',:c..  
.... .cd:........''.  ...'......;;c,,'..... ...   .       ..   .',,,,,,;::'';:::c:;;;lkkxOXNKkoc:ccc:c:lddkKOo:'.....';c'.. 
......cdc.  .      ......;;,;;,,..','..   .. .....      . 'c.  .,,;;;,,,,::;cooolc::;;:lxxO000xxddddlclkkkO00Od:'.....''..  
....  cdl,.        ...''''.....''.''.'...,;'.        . .. .,. .',;;;;:::;:ldxxk0OkxddxxxxxkOO00KKKK0OO0KK00000ko:'..... . ..
   ...cdc''.';'.   ........  ..  ..  . ..'.'            ...'...';;:cclccloddxkxxxxxxk0KXXXKK00KXWWWMWWWNXKXXXX0dc;..... .''.
.....',::;;,'.',..';::,   .'.''...   ....,,,.          ... ....,;;;;;:cokkO000KXKK000KKKKKKKKKKKXXNNNWNNNXXNNNX0d;...,:;;ll.
 ... .,;''','...;;:..,,.   ....            .,;ll,..  . .   ...,;;;,'.'';clodxxO0KKK000Okxdl:;;::;:::clloodxO0XNKx:...,::cdOk
..... 'd; . ..';;,...'',',oko,.      .,:oxOXWWWNWNKkdlc;.. ..........    ...,:lxOKXKxc;,'.....'',,;;::cc:' 'ccll:'...;:;:;:d
.c,.  .:'.....',,'...  .::ccc::;;:ox0NWMMWWWWWNNXXXNWWWWd. .'.....''''......  ..,;;'..,:::;,''',,:cokOOOKK:.';;'...'cc,',oxc
.,'.  .,'....  ......  .::oxOOKNWMMMMWX0Oxdollc::;;;coxO:..;,''',,,'.........    ..  ckl:,.',,;:cclllx0KXXl 'lokx,;OXk..'co,
.'''...,,,,cc;;'......',;:lkdc:cok0kdl::;;,,,,,,;,,,,;;,' .;,::;;,'...',,'...  'dOkl.:OOOxoodxxkO0XX0OKKOd: l0XNXllkdc......
lc;:. .''........    ......;.  .,:c;......'..''''.'',.... .;'..;:;,,;:::;;,'. 'kKNWWx'dKKK0kdoooodxkOKOddOccXNNXKdxKK;......
Okod;..';'.   .           'x.   'ldo,.'.,,'. ........ .'.  .;',::cloddddool:..ckKNWWWO;kNNNNNXXXXXXXOddOXxlXWNNXKodXd. ..';:
KXKKK0OkOd'.   ..:ldxxxxdllk.  .;odoc;;:ol:.   ....   .;.   ;:,;cloxO00000d,':dOKNWWWWO:dOKXNNNNNNWNKxdxdoKWNNNX0oxK:   .''.
WWWWWWWWWXkc..,o0KXXXXXK0KK0o. .,;c:,..'.'''..... .....:.    ''';;:cllollc,.,;dOKNWNNWNk:;coddxxkkkxxdx0NWWNNNXKOoONl    .'.
WWWMMMMMWWWNx;kOO0000000OOOkOxc. .,;'''..,''.',,'..',,:c. ...,,,;;;::clll;';:;d0KNWWNNWN0xc:ldkO00KKKKKWWNNNNXX0dxNo.    .',
WMMMMMMMMWWNXoloodddddddollllldd.  ..';;,;.....''...,,,;'....,:';;;:::::;';kdcxOKNWWNNWWWNXl,;:cldxk0KNNNNNNXXX0oxX;     .;l
MMMMMMMMMMWNXx;:lcc::::::;:;;:cxc.....'..,.......  .  ....';;:o,;;;;,,,,;.,cccdO0KXNNXXXNXKd,,,;cx0KXNNNXXXXXXXxcxx.     .:d
MMMMMMMMMMWNXk;.':cc:::::::::;:oocclc;.'.......:'.''...''.;;:cdl,;;;,;:l;.....,:loddl:;,,:xkdl;'';lkKXXXXXXXXKKoc:. .. ...lx
WMMMMMMMMMWNX0l,ll;::;;;;;;;;:cxxoloo:,,,'.,,''ol:::::;';:lclccd:,;;;,:;...      ...  .,;:ccooc,..':x0KKKXXXKKOlc:::,,.;,;oo
WWWMMMMMMMWNNKxlcc:;;;;,,;;;:cdkxllo:'',,'';;;;ddcolcccc;,,,:l:dkc;,;;;'.         ....'';;;::::'...'lOKKKKKKK0occclodolddcco
NWWWMMMMMMWWNXKkll:;,;;;;;;::coxxl,;;......'llcddclcclooooc'.,;lkd;,,,,..  .......,:;;;;;:oc:;,'....lOKKKKK0kl:loolodolxx:;:
NNNWWWWWWWWNNXKOOol:;;;;;;:::coddo'......'.,clcxxololodddddxkkkkOOo,,,,'. ...,::cdxlkXOOKKWXKo'....'oOKKK0Okc;:lc:;:cc:lxddc
KXXXXXXNNNXXXXK0X0l;''',,;::clodxkl;;;:cccc:cc:d0OkkO0KK0000K00KKK0c.','.  . .cdxKNNWMN0Oxxc,. ....'oO00Okoc;;::;;,;:::cloxl
O000KKKKKKKKKKK0Od:,,,,,,,,;:odxkkd;;:ccccccc:cdkloddxKXXKKXXKK0Okxc..''.  ..  ..;cc::;...... .l:,.'oO0kd:,';lo,;'',,::::cl:
xxOO000000OOOO000o;;;;;;;:::oO00OOkl:c:;ccc:c::do,..':OXXXXXXXXKKOdc,....  ...  .......';oOx;,k0o:,,lOxl;'',lkk;,'',,:::;::c
OllxOOOOOKKXK0000k:;;;;::::cdO0KKK0x:c;,;:::c::odok00XXXXXXXXX0Okxdcl'     ..'......',cx0XKOdO0Kk;.':l;..';lOKKl.';;':ccoxOo
Xk:;dkkOKXXXXXXXK0xlooddxddx0XXXKKKXkxxxxdocc:'cdkKXXXXXNNNXOl,,,''':c.    .'''..,cokkkO0OOk0KXX0;..,....;dKKKXKklc;';;',;:,
WXd;:dOO0KKKXXXXXXXNNNNNNNNNNXNNNWWWWWWWWWN0d:.ldo0KKKXKKK0k;......        ..'',ldxkkkxkkO000KXXKc......,l0KKXXNNOlc:;'';:, 
WN0l;;d000KKKKKKNWNWWWWWWNWWWNNNWWWWWWWWWWWNXx,;c:lc:::,....                .''':odxxkkO00000KKKXl......cOKKKXNNNxccllll::,.
WWNKx;;codkkkxxOKNWWWWWWWWWMMWWWMMMMWMWMMMWWNK:.                            .''';:clloddxkkkO0KKXo.....,d00KXXNNOlccclooolll
WWNXKd;,',;;;;;lxOKXNNNNNNNWWWWMMMMMWWWWWNNXK0d,''.                          .'.''';,;:;;cokKKKKKl....,ok0KXXNNx:::clooooooo
NNXXK0l,,,,;;;,,;oxxk0KKXXXNNWWWWWWWWNNNNXKK0Kk'...                           .'........'lOXXXKKk,...,dOKKXNNKd;;::ldooooloo
XXKKK0kc;;;;;,,,,l00OOOkO00KKXXXXXXXXXXKKKKKKKKc...                            .''..',',cOXXXXKd,...lOKXXNN0d:;;;:lolloolloo
00000O0Ol,;;;,,,,:OXXKOdc::coodxkkkkOkkO0OO0KKKk:;'..                           ...,ldoodkOkxl;..,lkKXNX0xl:;;;clodlcloolooo
0KKK0OOOkc;;;,,,,oXX0d:;,,,,,',;::::cldxdxO0KKK0dooolc::.                         ...'''...... .,dkOkdoc;,,;;:loodlcooollooo
KXXXXXK00kl::;;:dK0d:;,,,,,,'..,,;::codkO00KKKKKOdoollll.                            . .      ..',,''',,;;;:cloooo;ldoollool
0KKXXXKK00OxdddOXkc;,,,,,;;,,'',;:codO00KKKXXXXK0xoolllo'                                   ..'.'''',,;;:cllloooo::ooooloool
000KKKKK0XWWWWNNOc;;,,,;;;:cccllldkO00KKXXXXXXXKKkooollo'                                ..';;;;;:::ccloolllooool;ldoooloool
kOOOOkxoxXWMMWWN0occcclodxkOKXNNNXXXKKKKKXXXXXKKKOoolcllc,,;:c:,...                    .';cccclccccllllollllllll,:oollllloll
cclc:;,;:dXWWWNNXK00KKXXNNNXNNNWWNNNNNXXXXXKKKKKKxlol:lcllloolllccc.                  .;cccclclccccllloolllllol;'lollloooolc
kdolc;,;;ckXNNNNNNXXXNNNNWNNNNNNNNNNNNNNNXKK00Okdlooclllllllllllcclc;.... ...   ....';:ccccccllcllllllllollllll,coolclloollc
KKK0Ol;;:o0XNNNNNNNNXXNNNNWWWNNNNNNNNNNXKKK0Oxoollolcoooollollll:colllcc:.clc:;::ccccccccccccllllllllloollllll,;oollllllllcc
00KKOccoOKXNNNNNNNNNNNXXNNNNNNNNNNNNXXXKK0Oxdooolcl:collloloollccloolllcc.:oollccllcclccccllllllollllllllllllc'coollllllllcc
kkxdco0XNNXNXXNNNNNNNNNNNNNXXNNNXXXXXK00Okdooollccc:llloollllllcclloollcl.;ooolclllllcccllllllllollcllllllclc''lollllllllccl
cc::ckXWWXNNXXXNNXXNNNNNXNNNXXXXXXXXXKOkkdodololccccoooolcllollclooolloll.,oollcclccllccllcllllllllclllclllc:.,lolllclllc::l\
"""

__title__ = 'kyle'
__version__ = '0.0.3'
__build__ = 0x000003
__author__ = 'Kyle Kelley'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2013 Kyle Kelley'

print(__img__)
