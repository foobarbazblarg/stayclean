#!/usr/bin/env python3
from flask import Flask
from flask import Response
from io import StringIO
# encoding=utf8
import sys
import importlib

importlib.reload(sys)
# sys.setdefaultencoding('utf8')

# Edit Me!
shadowbanned_accounts_string = 'cawmander, imadering, AnUglyWorld, terpyman710, lokimarkus, ZnerWill, caust1z, ScarletOverLord6767, TrevTrevv99, pattycake_v2, wolfgangbeast, OldCodger39, lamperstamp, joshyblob019, lust_addicts, Unlucky_Chad, XXTHEXXGERMANXX, fatkc, lmaonglplsstfurn, rex2oo9, Houston_PD2, peanutbutterapple12, The_memester_77, StudMuffin2002, DirtyDarrenDawson, fallopiantubediver69, sqooterboi570, virgo8001, theboss357, Moiorban, JamesDeensaan, samgeta_fusion1, EquivalentBarnacle6, Dre2timez, sweetreuzel, Water_Bottle05, ariadnesparkle, Boethiah18, Balkanka, awwfuckmybeer, Stinkypinkywinky69, Capusotes, mysteryman_2, the_ghost_of_, dwaynebravo_09, LEEVO11, chao-L77, CaptaNMorGaN-n-MoLly, Tricky-Calendar-9715, rune-scimmy, Electrical_End9713, BewgleShmoots, spongemaster647, Ven555, damesdior, KakiBakuku, Ninjaclumsythee, realsmalleybiggs, Ikopg_, Rare_Illustrator_447, dicktuneup, jr_jedgar, fatemabsl, banhunded, Angelothebaws, Coca4Me, _playlister, beyondreason1980, AndreParkz, Slurtee, seth_process, IWokeUpDeadInside, geo_699, Trainer_Red99, GromOwner, WitcherLord, akashicrecords888, MrTrumpeteer711, poopyhead133457, TheFakeTravisScott, Thedankmemelord76, Scam9160, toobythedragontamer, gattri581, Hattrickhaggy910, CommentNub, hiddenfromothers, CytokineDan, xPipokidx, Courtesybog3, throwawayman1212lol, Ibukiibuki24, salseroruiz, folyamirock, moskayjoh, 998104D, casdomdomcas232423, JeffD52, n1gaton1, forgottenlikefirefox, cant_dodge_rodge, WatchDog_Dog, ghabro, _Golden_Experience_, footballhd720p, shakenmanchild, theawesomevincent, SkinnyWhitePimp420, paxauror, coringa131830, kentuckyfriedcotton, The_Garlic, citosil, ToastedWaffCakes, JustPORNmovies, beatmyneat, RoitheOG, DawnOfBliss, porntocum, drmahesharjun, No-Gas5016, NervousShower, throwwyAF, Outrageous-Fan-2228, Master_Glass_5297, crhisram14, vforvendetta87, CartographerLow4082, OkHippo1430, n3wc0mer, MyDogLovesCorn, womandatory, FattoiletsWorld, RootLevelUser, RootLinuxUser, Strong-Sugar8829, 4BetterM1nd, WatermelonMan921, KundalinirRZA, Thardeserts, ImportantReward8742, Standard_Foot_8011, Depresseur, Johnfrost76, BloopBloopBloop54, mercerguy, StopWarm6115, frog_666_, No_Fap_is_My_Life, ailuj_akire_, csobod, LivingFree87, HorrorFearless2758'
shadowbanned_spam_accounts_string = '100fnc'
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
    stringio = StringIO()
    stringio.write('<html>\n<head>\n</head>\n\n')

    stringio.write(f'<h3>Non-spam (total: {len(shadowbanned_accounts)})</h3>\n')
    for shadowbanned_account in shadowbanned_accounts:
        if shadowbanned_accounts.count(shadowbanned_account) > 1:
            stringio.write('(one of multiple) - ')
        stringio.write('<a href="https://www.reddit.com/u/{0}" target="_blank">{0}</a>'.format(shadowbanned_account))
        stringio.write("<br>\n")
    stringio.write('\n\n')
    stringio.write(f'<h3>Spam (total: {len(shadowbanned_spam_accounts)})</h3>\n')
    for shadowbanned_account in shadowbanned_spam_accounts:
        if shadowbanned_spam_accounts.count(shadowbanned_account) > 1:
            stringio.write('(one of multiple) - ')
        stringio.write('<a href="https://www.reddit.com/u/{0}" target="_blank">{0}</a>'.format(shadowbanned_account))
        stringio.write("<br>\n")
    stringio.write('</html>')
    pageString = stringio.getvalue()
    stringio.close()
    return Response(pageString, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=flaskport)

