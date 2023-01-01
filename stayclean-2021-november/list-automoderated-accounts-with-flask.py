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
shadowbanned_accounts_string = 'shadowbanneduser, Gyaiahagegei, unmaskingliars, fightingbetterworld, Anzbev70, freemason138, cawmander, ayush9861, ReyisLeia, christianmommyof3, shanana29, imadering, Tezos_2018, Noansense, oooogler, ooooogler, oooooogler, ooooooogler, HavenWaldo, not_oooogler, not_ooooogler, defnotoooogler, oooogs, ooooogs, nopenotoooogler, nopenotoooogler1, seriouslynotoooogler, TheRealAlphaOooogler, fraserUIB, CheetoB, zking22, Putoelquelolea0019, FinickyMaestro, Jamesthejew00, Goodfreeze, user-290, Kuastuza, erotico38, skiborants, minecraftcoolkid21, TheDop69, AnUglyWorld, terpyman710, Javell_mcgee89, Birdman113, lokimarkus, redbunny1089, ZnerWill, ewffu23, Richkidbilly, caust1z, i_likewaffles23, _Mother__Fucker_, CoffeeCrisp_, Proudsou74, pumpingpiggy, ScarletOverLord6767, kylenaruto, JonPom420, ThePlasmaDoctor, TrevTrevv99, danknugger1234567891, giova756, dnugg11, pattycake_v2, wolfgangbeast, TheTeslaKing, Summit_f13, maxdean1999, OldCodger39, michael8197, DontThrowawayRecycop, TheForeskinFiddler, willfly4gas, lamperstamp, ProshooterYT, Tim198469, deadshot200004, aankuri, joshyblob019, emote-man, lust_addicts, epicstinkymoonkeyheh, MaDoGger69, Unlucky_Chad, XXTHEXXGERMANXX, fatkc, dontyesnt, lmaonglplsstfurn, rex2oo9, cum_dumbster2, Aloneandafraid16, Houston_PD2, impracticalstonerlll, peanutbutterapple12, The_memester_77, Fergstar95, thehooknosejew, bigsweetit564, StudMuffin2002, DirtyDarrenDawson, fallopiantubediver69, sqooterboi570, virgo8001, theboss357, Moiorban, hey_covid_19, JamesDeensaan, iprobablyhateyou420, samgeta_fusion1, EquivalentBarnacle6, Dre2timez, sweetreuzel, Water_Bottle05, ariadnesparkle, Boethiah18, Balkanka, awwfuckmybeer, Stinkypinkywinky69, Capusotes, mysteryman_2, the_ghost_of_, dwaynebravo_09, Thorsidekick, LEEVO11, chao-L77, CaptaNMorGaN-n-MoLly, Tricky-Calendar-9715, rune-scimmy, Electrical_End9713, BewgleShmoots, spongemaster647, Ven555, damesdior, KakiBakuku, Ninjaclumsythee, realsmalleybiggs, haiti817, Ikopg_, Rare_Illustrator_447, dicktuneup, jr_jedgar, fatemabsl, banhunded, Angelothebaws, Coca4Me, _playlister, beyondreason1980, Shamefreeporn, AndreParkz, Slurtee, seth_process, IWokeUpDeadInside, geo_699, Trainer_Red99, GromOwner, WitcherLord, akashicrecords888, MrTrumpeteer711, poopyhead133457, TheFakeTravisScott, Thedankmemelord76, Scam9160, toobythedragontamer, gattri581, Hattrickhaggy910, CommentNub, hiddenfromothers, CytokineDan, xPipokidx, Courtesybog3, lostboysinner, throwawayman1212lol, cewinharhar, Ibukiibuki24, salseroruiz, folyamirock, moskayjoh, 998104D, biglongweteyes, casdomdomcas232423, JeffD52, n1gaton1, forgottenlikefirefox, cant_dodge_rodge, WatchDog_Dog, ghabro, SlothLol07, willthethrill92701, _Golden_Experience_, footballhd720p, shakenmanchild, alfaaniket, theawesomevincent, SkinnyWhitePimp420, paxauror, coringa131830, kentuckyfriedcotton, The_Garlic, citosil, ToastedWaffCakes, JustPORNmovies, beatmyneat, RoitheOG'
shadowbanned_spam_accounts_string = ''
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

