n =  24554082244423576690279633247865769176171558470735704642013748456293986193768290232671815437132451174934519049784696027147781044695306925702057388654404061134243359186055889332417446146289789929503311347508856172482634852836123428376583619524965874497204667755767688503035506095489672593674965956038947918754161997820726040674864658744822975386315296832923061518481651545615396827420722325276534476848101960733475080768574205931138886447888957784368331413187068740663339419123762654261526051955619178483106487893708893917779677273100451964193513643587668371074516605372011468635189674135998949600383546855684675027489
e =  65537
c =  6989948518232384864776638814859831591901837611907564903634405279896177437836827945714748614888983988728637485614070870977180774832773899224982914219277551793975090942823743973796811784289974047801705426989528230917131553686987581588091533315187245746656484375900794753350613814764158557562323887200250573252180097909170473172195491291928129134980077422551100499336853912674636732929441216424149814296320827970989924149481811607226528197449647871111226798077417180876925544299697444446643855793213707552379877215861130808560692690231253480548958307798400899147718220394516058861876909981592273632212374753442396382822

d = 1785675652489484099866625219547495904829038087131470929199044461315809007854706383953994786918884048035991647560234437834959151802011378629807868402588942976844311309651656706051056662861977585604375693061105133360907548987191491448667845699504523835207433924461880683682959267121865752026017320250028695992655851462487112558508335629527434524159578362894834755516384098754276986466722254997719811154564444862004477733023964344810084134554812087896823698060594556299357881509322147331428184535043671737865691756584143724813124256017858804886372514187982328602595109583194368610294480604421697058921714316076575120217

# Decryption
m = pow(c,d,n)
print 'flag :', str(hex(int(m)))[2:-1].decode('hex')