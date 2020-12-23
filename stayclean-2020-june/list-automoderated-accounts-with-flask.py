#!/usr/bin/env python

import subprocess
import praw
from hashlib import sha1
from flask import Flask
from flask import Response
from flask import request
from cStringIO import StringIO
from base64 import b64encode
from base64 import b64decode
from ConfigParser import ConfigParser
import OAuth2Util
import os
import markdown
import bleach
# encoding=utf8
import sys
from participantCollection import ParticipantCollection

reload(sys)
sys.setdefaultencoding('utf8')

# Edit Me!
shadowbanned_accounts_string = '[ wolfgangbeast, TheTeslaKing, TheNorthAmerican, Summit_f13, maxdean1999, OldCodger39, chefgypo, michael8197, DontThrowawayRecycop, TheForeskinFiddler, willfly4gas, lamperstamp, ProshooterYT, Tim198469, TGxRedPlayer, deadshot200004, aankuri, joshyblob019, emote-man, lust_addicts, epicstinkymoonkeyheh, MaDoGger69, Unlucky_Chad, kaszasza, XXTHEXXGERMANXX, fatkc, throwawayhusbnd, whathisbastardid, SheIsRadFem, cornisnotamuffin, Positivityneededhere, signedwtbd, gives_clues, logician01, dontyesnt, lmaonglplsstfurn, weboomin, rex2oo9, cum_dumbster2, Aloneandafraid16, Houston_PD2, impracticalstonerlll, peanutbutterapple12, The_memester_77, Fergstar95, pinkcashmera, thehooknosejew, BubberkinsXO, bigsweetit564, StudMuffin2002, DirtyDarrenDawson, Pfr03252001, Adawritesrules, thin_diick_ryan, Ugandan-Knucklez, NonnyTheThot, fallopiantubediver69, sqooterboi570, virgo8001, theboss357, Moiorban, hey_covid_19 ]'
shadowbanned_spam_accounts_string = '[ DistinctRing6, AnyEstablishment3, Murky-Geologist, BroadBlackberry1, alfaaniket, Your_wildest_dream, theawesomevincent, I_Have_n0_Life2006, lewis1999199, KingPahsaTheRobloxer, ravecat320, alfaaniket, Doomsayer1996, Forward_Resolution, rpgnukester, ja_heritage, XXXLilMomma, LittlePornycom, famtasygirlxxx, shakenmanchild, karlooo21, BroadBlackberry1, ExoticNature5, ILoveYou_22, 7-inch-d, iggy0101, Miss_Wang, footballhd720p, mxqayyum, PurpleLily19-, babielove21, Dantas22, dblthrowaway, oladayo2016, broken_mistake, dumbfuckjuice1, Tripl3tasXxX, warkittnnn, Flimsy_Recording, Subject-Piano, 0ShadyBaby0, piercedruby, Silly-Salt, lilbabyava22, mustardgoochbiscuit, Mars_Pornhub, lola_2020, karol211, megapornclub, Global-Tradition, AgGe190, JegueTube, yianex12g, memes0fficial, DrRichard_369, _Golden_Experience_, willthethrill92701, LogicalClothes1, awkneedshelp, yuyu28g, SlothLol07, Billyjones09234, Sanxxxl, HikaidoTransBoy, Kiara-kinky, at360, yusemo12, shar745, Erylla, Anonutopia, Rare_Character, AbbeySilver, NoahChap, GreenClient3, 870Killakellz, Averageboy102, Kovan2910, latrepz, ghabro, ZeusssReborn, Hotboy002, jilhubboy, Salemvonxxx, Willing-Product, Rough-Resident, newsreaderforyou, isextoysofficial, mffj, avstartube, WatchDog_Dog, porntube2020, NolanVan69, Afromania2149, JadedStandard, Re_L_, Hauntingbald, cant_dodge_rodge, fattnisseverdeen, clickboom2020, Hornyguy73, adam77955, Cap-Rk, MKBandara, RevolutionaryWish8, ojosgolosos, East_Armadillo, LovYoung, cute_mona, UsuganiIchiwa, X_Forex, FamousDurian7, lostboysinner, Adamwithineve, Bobhovedsen, Checkmate791, Mandiiibee, athcrypto, IcyInitial3, Marcher165, kc092316, forgottenlikefirefox ]'
shadowbanned_accounts = shadowbanned_accounts_string.split()
shadowbanned_accounts = [acct.replace(",", "") for acct in shadowbanned_accounts]
shadowbanned_accounts.reverse()
shadowbanned_spam_accounts = shadowbanned_spam_accounts_string.split()
shadowbanned_spam_accounts = [acct.replace(",", "") for acct in shadowbanned_spam_accounts]
shadowbanned_spam_accounts.reverse()

flaskport = 7000

app = Flask(__name__)
app.debug = True


@app.route('/listautomoderatedaccounts.html')
def listautomoderatedaccounts():
    global commentHashesAndComments
    commentHashesAndComments = {}
    stringio = StringIO()
    stringio.write('<html>\n<head>\n</head>\n\n')

    stringio.write('<h3>Non-spam (total: {0})</h3>\n'.format(len(shadowbanned_accounts)))
    for shadowbanned_account in shadowbanned_accounts:
        stringio.write('<a href="https://www.reddit.com/u/{0}" target="_blank">{0}</a>'.format(shadowbanned_account))
        stringio.write("<br>\n")
    stringio.write('\n\n')
    stringio.write('<h3>Spam (total: {0})</h3>\n'.format(len(shadowbanned_spam_accounts)))
    for shadowbanned_account in shadowbanned_spam_accounts:
        stringio.write('<a href="https://www.reddit.com/u/{0}" target="_blank">{0}</a>'.format(shadowbanned_account))
        stringio.write("<br>\n")
    stringio.write('</html>')
    pageString = stringio.getvalue()
    stringio.close()
    return Response(pageString, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

