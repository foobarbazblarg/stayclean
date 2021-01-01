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
shadowbanned_accounts_string = '_playlister, Coca4Me, shadowsuprising, YoursTrulyXxxxxx, jossandjane, 2002alice2002, SanJorgeTenorio, jonethai500, itstheyear3030, OFSavagedoll247, haiduc97, AdFunny1032, Dark_Writor, Kratz177, Anxious-Half-4844, wewe_wowo, josh23green, Angelothebaws, Exen44, Juicystarfruit625, Landencook, INTPcruise, minoblocker, Drippydiana, TiTiNichole10, craigfootball, Tomatensooos, ajahdisishzhzhsieudj, xFrenchies, christopherjasonsuse, Milfcameras, YamExternal964, Michellebelle9, banhunded, hotbaby96, RubyRed70, kysnicxlle, Ahmet2020, nachosexxx, ConstantlyHornyHehe, Freakysxcontent, PurgeHer_1makePornos, DevelopmentOdd2585, onlysearcher, Spermatozorro, fatemabsl, Ok_Big8944, spoydark, giulialoise, mouaadhfofa90, nthn108, chookle3pur, 4BetterM1nd, amararosewales, jr_jedgar, ENKKIN, hotgirlray, AdmirableChocolate11, NaughtyMan2, mentaurapp, Tall-Award, latosharamirez5AR, juciygirl420, MayaAmour, Oompaaah, MrBlackPotato, kyanet19, CharitableLinkBot, Nervous-Ad-7350, isame4, Major_Bar_6343, ErszebetBathory_96, BoysWannaSeeMyBody, Machoudibrahim03, FrozenCheekSlayer, dicktuneup, Rare_Illustrator_447, Daniellaftv23, willden123, margot1216, Philly_x, Quiet_Ad_8636, dolliexox, Upbeat-Complex2555, KatyaLovel, Heirleking, michael32123, adultscarein, italianlee1462, Ikopg_, haiti817, TamaoSerizawa512, Auger_Jaern, toxicamimosa_1000, Analtranna, Kurprdlak, Equivalent_Ad_5145, Squirrel_Chance, hekatesh, s1rny, Flirtyfeetxo, TheCreoleBarbie, JamesDeensaan, Joepeace1, realsmalleybiggs, RFireOG, Lilsarahhh-23, Key_Ad6494, Asteriaaajadeeexoxo, Anonimus2837, Luulmamiii, losmejorespacketones, tannsophal999, officiallyscarlettxo, poraz24, mothprooftitan1, Ninjaclumsythee, octogonsigma, PMSEND_ME_NUDES, Strange_Data_1612, KakiBakuku, anonwook, Trumpet_Player5, mermaidBR, XxTRAPxX20, Johnino19, looktoo321, KitKat261, damesdior, Ven555, f1_shado, Suitable-Sherbert522, Low_Bluebird_5142, Litherdal, FernandoMendes777666, Orion0012000, DevilisiousDoll, MarcixRomana, Perfect-Job-5444, Brilliant-Trainer-77, No-Clerk9037, Happy-Computer6646, kuroangel1420, Orion0012000, MEGAPLUG_2020, maddiesugar20, victoriaonly75, rosiebug_, FlightSoggy3536, faissalmetalsi, Pfghrd43, zxqf, AddressOver2407, mrsmc90kx6, milek102, SirThatsMyTaco, MiSaRi91, Tricky-Calendar-9715, Federal_Park6545, cubelove80, DarkAny3615e, Victorenred, djbodlak, Orion0012000, Altcoin-Magazine, schaakbord7, Realistic-Address-55, antichristisme, Ladf942, spongemaster647, WildRockyOffocial, LilaFrey, emmi509, Ilenina, LuLaa96, FullRun9610, analxporn, Far-Holiday-4525, pussycatdawllz, ballikgndocme'
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

