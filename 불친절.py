import discord

client = discord.Client()

f = open('통합 문서2.txt', 'r')


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("질문 딱대")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!거다이맥스 팬텀"):
        await message.channel.send("``거다이맥스 팬텀의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 괴력몬"):
        await message.channel.send("``거다이맥스 괴력몬의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 킹크랩"):
        await message.channel.send("``거다이맥스 킹크랩의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 리자몽"):
        await message.channel.send("``거다이맥스 리자몽의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 버터플"):
        await message.channel.send("``거다이맥스 버터플의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 라프라스"):
        await message.channel.send("``거다이맥스 라프라스의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 잠만보"):
        await message.channel.send("``거다이맥스 잠만보의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 더스트나"):
        await message.channel.send("``거다이맥스 더스트나의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 아머까오"):
        await message.channel.send("``거다이맥스 아머까오의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 이올브"):
        await message.channel.send("``거다이맥스 이올브의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 갈가부기"):
        await message.channel.send("``거다이맥스 갈가부기의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 석탄산"):
        await message.channel.send("``거다이맥스 석탄산의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 애프룡"):
        await message.channel.send("``거다이맥스 애프룡의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 단지래픙"):
        await message.channel.send("``거다이맥스 단지래플의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 사다이사"):
        await message.channel.send("``거다이맥스 사다이사의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 스트린더"):
        await message.channel.send("``거다이맥스 스트린더의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 다태우지네"):
        await message.channel.send("``거다이맥스 다태우지네의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 브리무음"):
        await message.channel.send("``거다이맥스 브리무음의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 오롱털"):
        await message.channel.send("``거다이맥스 오롱털의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 마휘핑"):
        await message.channel.send("``거다이맥스 마휘핑의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 마빌크"):
        await message.channel.send("``거다이맥스 마빌크의 포획률은 200이다.\n확률로 나타내면 83.09%이고,\n하이퍼볼일때 100%, 다크볼일때 100%, 리피드볼일떄 100%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 대왕끼리동"):
        await message.channel.send("``거다이맥스 대왕끼리동의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스 두랄루돈"):
        await message.channel.send("``거다이맥스 두랄루돈의 포획률은 3이다.\n확률로 나타내면 3.35%이고,\n하이퍼볼일때 5.98%, 다크볼일때 8.11%, 리피드볼일떄 9.11%의 포획률을 갖는다.``")
    if message.content.startswith("!무한다이맥스 무한다이노"):
        await message.channel.send("``무한다이맥스 무한다이노의 포획률은 255이다.\n확률로 나타내면 100%이고,\n하이퍼볼일때 100%, 다크볼일때 100%, 리피드볼일떄 100%의 포획률을 갖는다.``")
    if message.content.startswith("!거다이맥스"):
        await message.channel.send("`거다이맥스 개체의 종류는\n각각 !거다이맥스 1세대, 8세대, 그 외 세대를 입력해서 알아보셈.\n포획률은 대체로 3으로 고정.`")
    if message.content.startswith("!거다이맥스 1세대"):
        await message.channel.send("``리자몽, 버터플, 피카츄, 이브이, 나옹,\n괴력몬, 팬텀, 킹크랩, 라프라스, 잠만보가 있다.``")
    if message.content.startswith("!거다이맥스 8세대"):
        await message.channel.send("```아머까오, 이올브, 갈가부기, 석탄산,\n애프룡, 단지래플, 사다이사, 스트린더, 다태우지네,\n브리무음, 오롱털, 마휘핑, 마빌크, 대왕끼리동, 두랄루돈, 무한다이노가 있다. 존나많네 ㅅㅂ```")
    if message.content.startswith("!거다이맥스 그 외 세대"):
        await message.channel.send("`더스트나, 멜메탈... 겜프릭 시발련들아`")
    if message.content.startswith("!볼"):
        await message.channel.send("종류는 여러가지이나, `!볼 [이름]` 이렇게 쓴다면 포획률 보정 등을 알려준다.")
    if message.content.startswith("!포획률"):
        await message.channel.send("`종류: 3, 25, 30, 45, 50, 60, 75`")
    if message.content.startswith("!포획률 3"):
        await message.channel.send("`거다이맥스, 그 외 해당 ㄹㅇ 없다~`")
    if message.content.startswith("!포획률 25"):
        await message.channel.send("`픽시, 잠만보, 강철톤, 만타인, 타만타, 타타륜`")
    if message.content.startswith("!포획률 30"):
        await message.channel.send("`거대코뿌리, 토게키스, 기기기어르, 산호르곤, 에써르`")
    if message.content.startswith("!포획률 45"):
        await message.channel.send("`파이리, 리자드, 리자몽, 버터플, 라플레시아, 괴력몬, 파오리, 팬텀, 롱스톤, 시라소몬`")
        await message.channel.send("`홍수몬, 마임맨, 갸라도스, 라프라스, 이브이, 샤미드, 쥬피썬더, 부스터, 아르코, 에브이, 블래키, 마자용, 딜리버드,`")
        await message.channel.send("`카포에라, 애버라스, 데기라스, 마기라스, 로파파, 페리퍼, 가디안, 껍질몬, 깜까미, 입치트, 플라이곤, 루나톤, 솔록, 비퀸, 루카리오, 드래피온, 포푸니라, 리피아, 글레이시아, 엘레이드, 야느와르몽, 로토무, 켄호로우, 기가이어스, 맘박쥐, 너트령, 두빅굴, 던지미, 타격귀, 심보러, 배바닐라, 샹델라, 액스라이즈, 절각참, 모노두, 디헤드, 삼삼드래, 킬가르도, 거북손데스, 님피아, 미끄메라, 미끄네일, 미끄래곤, 음번, 투구뿌논, 염뉴트, 달코퀸, 하랑우탄, 내던숭이, 갑주무사, 따라큐, 짜랑꼬, 짜랑고우, 짜랑고우거, 아머까오, 이올브, 펄스멍, 석탄산, 애프룡, 단지래플, 윽우지, 스트린더, 케오퍼스, 브리무음. 오롱털, 가로막구리, 창파나이트, 마임꽁꽁, 대여르, 드라꼰, 드래런치, 드래펄트`")
    if message.content.startswith("!포획률 50"):
        await message.channel.send("`닥트리오, 먹고자, 맘모꾸리, 고디모아젤, 란쿨루스`")
    if message.content.startswith("!포획률 60"):
        await message.channel.send("`날쌩마, 파르셀, 킹크랩, 또도가스, 코뿌리, 왕콘치, 포푸니, 고래왕, 밀로틱, 둥실라이드, 하마돈, 눈설왕`")
        await message.channel.send("`몰드류, 불비달마, 곤율거니. 더스트나, 치라치노, 탱탱겔, 기기어르, 액슨도, 툰베어, 워글, 버랜지나, 대로트, 펌킨인, 약어리, 만마드, 해무기, 꼬치조, 포트데스, 돌헨진, 빙큐보`")
        await message.channel.send("`대로트, 펌킨인, 약어리, 만마드, 해무기, 꼬치조, 포트데스, 돌헨진, 빙큐보`")
    if message.content.startswith("!포획률 75"):
        await message.channel.send("`라이츄, 나인테일, 윈디, 랜턴, 토게틱, 네이티오, 메꾸리, 대포무노,`")
        await message.channel.send("`배루키, 메깅, 얼음귀신, 로즈레이드, 체리꼬, 트리토돈, 리오르, 독개굴, 눈여아, 몽얌냐, 엘풍, 암팰리스, 슈바르고, 전툴라,`")
        await message.channel.send("`터검니, 어지리더, 메더, 냐오닉스, 일레도리자드, 에리본, 더시마사리, 마셰이드, 백솜모카, 갈가부기, 일레즌, 다태우지네, 찌르성게, 모스노우`")
    if message.content.startswith("!포획률 공식"):
        await message.channel.send("`몬스터볼을 던지는 순간 포켓몬 게임에서는 그 포켓몬의 CatchValue 를 계산하게 된다. 이 CatchValue는 어떤 숫자로 포켓몬을 포획하게 되는데 중요한 역할을 하고 있음. 그리고 몬스터볼은 3번 흔들리게 됨. 이 동안 0부터 65535까지의 난수를 총 4번 만들어내고 그 난수가 CatchValue로 만든 어떤 값보다 같거나 크게 되면 포켓몬이 볼에서 튀어나오게 된다.\n그 CatchValue는 다음 식으로 이루어져 있다.`")
        await message.channel.send("`((최대 HP*3 - 현재 HP*2) * 피포획률 * 볼 * 상태이상)/(최대 HP*3)`")
    if message.content.startswith("!볼 몬스터"):
        await message.channel.send("`몬스터볼\n200원\n포획률 보정 1.0\n획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 수퍼"):
        await message.channel.send("`수퍼볼\n600원\n포획률 보정 1.5\n획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 하이퍼"):
        await message.channel.send("`하이퍼볼\n800원\n포획률 보정 2.0\n획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 사파리"):
        await message.channel.send("`사파리볼\n사파리 게임에서 30개씩 대여\n포획률 보정 1.0\n획득 불가능한 시리즈: 2세대(리메이크 포함) 이후 모든 시리즈`")
    if message.content.startswith("!볼 마스터"):
        await message.channel.send("`마스터볼\n비매품\n포획률 고정 255\n획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 콤페"):
        await message.channel.send("`콤페볼\n비매품\n포획률 보정 1.5(자연공원)\n획득 불가능한 시리즈: 2세대(리메이크 포함) 이후 모든 시리즈")
    if message.content.startswith("!볼 레벨"):
        await message.channel.send("`레벨볼\n빨간규토리\n상대보다 레벨이 높다면 2.0, 2배 이상이라면 4.0, 4배 이상이라면 8.0, 그 외에 1.0\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
    if message.content.startswith("!볼 프렌드"):
        await message.channel.send("`프렌드볼\n초록규토리\n포획률 보정 1.0, 초기 친밀도 200\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
    if message.content.startswith("!볼 루어"):
        await message.channel.send("`루어볼\n파란규토리\n낚시로 잡았을 시 5.0, 그 외 1.0\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
    if message.content.startswith("!볼 문"):
        await message.channel.send("`문볼\n노란규토리\n달의 돌로 진화하는 포켓몬일시 4.0, 그 외 1.0\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
    if message.content.startswith("!볼 러브러브"):
        await message.channel.send("`러브러브볼\n분홍규토리\n같은 포켓몬의 다른 성별일시 8.0, 그 외 1.0\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
    if message.content.startswith("!볼 스피드"):
        await message.channel.send("`스피드볼\n하얀규토리\n스피드 종족값이 100 이상일시 4.0, 그 외 1.0\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
    if message.content.startswith("!볼 헤비"):
        await message.channel.send("`헤비볼\n검은규토리\n하단 참조\n획득 불가능한 시리즈: 2(리메이크 포함), 7, 8세대 제외 모든 시리즈`")
        await message.channel.send("`체중이 204kg 미만인 포켓몬에게는 포획률 20 감소.\n체중이 204~307kg인 포켓몬에게는 포획률 20 증가.\n체중이 307~409kg인 포켓몬에게는 포획률 30 증가\n체중이 409kg 이상인 포켓몬에게는 포획률 + 40(맥스 레이드배틀에서 적용 불가)`")
    if message.content.startswith("!볼 GS"):
        await message.channel.send("`GS볼\n배포\n효과 없음\n획득 불가능한 시리즈: 2세대 제외 전부")
    if message.content.startswith("!볼 프레미어"):
        await message.channel.send("`프레미어볼\n볼 10개당 1개 지급\n포획률 보정 1.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 넷트"):
        await message.channel.send("`넷트볼\n1000원, 50W\n물, 벌레 타입에게 포획률 3.5, 그 외 1.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 다이브"):
        await message.channel.send("`다이브볼\n1000원, 50W\n물에서 서식하는 포켓몬에게 포획률 3.5, 그 외 1.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 네스트"):
        await message.channel.send("`네스트볼\n1000원, 50W\n((41 - 포켓몬 레벨) ÷ 10)×1.0, 최소 1.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 타이마"):
        await message.channel.send("`타이마볼\n1000원, 50W\n(1+0.3×경과된 턴 수), 최대 4.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 리피드"):
        await message.channel.send("`리피드볼\n1000원, 50W\n도감에 등록되어 있다면 3.5, 그 외 1.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 럭셔리"):
        await message.channel.send("`럭셔리볼\n3000원, 100W\n모든 포획률 증가 조건에 +1, 그 외 1.0\n3세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 힐"):
        await message.channel.send("`힐볼\n300원, 20W\n잡은 포켓몬의 체력과 상태이상 회복, 그 외 1.0\n4세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 다크"):
        await message.channel.send("`다크볼\n300원, 20W\n잡은 포켓몬의 체력과 상태이상 회복, 그 외 1.0\n4세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 퀵"):
        await message.channel.send("`퀵볼\n300원, 20W\n잡은 포켓몬의 체력과 상태이상 회복, 그 외 1.0\n4세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!볼 파크"):
        await message.channel.send("`파크볼\n비매품\n포획률 255 고정\n4세대 이후 획득 불가능한 시리즈: 전부`")
    if message.content.startswith("!볼 프레셔스"):
        await message.channel.send("`프레셔스볼\n비매품\n배포 포켓몬들의 볼, 데이터상 포획률 1.0\n획득 불가능한 시리즈: 전부`")
    if message.content.startswith("!볼 드림"):
        await message.channel.send("`드림볼\n비매품, 볼가이가 1개 줌\n(5세대까지)255 고정/(8세대부터) 잠듦 상태일때 3.0, 그 외 1.0\n5세대 이후 획득 불가능한 시리즈: 8세대 외 전부`")
    if message.content.startswith("!볼 울트라"):
        await message.channel.send("`울트라볼\n(USUM) 1000원/(8세대) 볼가이가 1개 줌\n울트라비스트에게 5.0, 그 외 **0.1**\n7세대 이후 획득 불가능한 시리즈: 없음`")
    if message.content.startswith("!호출"):
        await message.channel.send("@everyone")
    if message.content.startswith("!이상해씨"):
        await message.channel.send("`도감번호 1번 이상해씨 \n종족값 45/49/49/65/65/45/총합:318`")
    if message.content.startswith("!이상해풀"):
        await message.channel.send("`도감번호 2 이상해풀 \n종족값 60/62/63/80/80/60/총합:405`")
    if message.content.startswith("!이상해꽃"):
        await message.channel.send("`도감번호 3 이상해꽃 \n종족값 80/82/83/100/100/80/총합:525`")
    if message.content.startswith("!메가이상해꽃"):
        await message.channel.send("`도감번호 3 메가이상해꽃 \n종족값 80/100/123/122/120/80/총합:625`")
    if message.content.startswith("!파이리"):
        await message.channel.send("`도감번호 4 파이리 \n종족값 39/52/43/60/50/65/총합:309`")
    if message.content.startswith("!리자드"):
        await message.channel.send("`도감번호 5 리자드 \n종족값 58/64/58/80/65/80/총합:405`")
    if message.content.startswith("!리자몽"):
        await message.channel.send("`도감번호 6 리자몽 \n종족값 78/84/78/109/85/100/총합:534`")
    if message.content.startswith("!메가리자몽X"):
        await message.channel.send("`도감번호 6 메가리자몽X \n종족값 78/130/111/130/85/100/총합:634`")
    if message.content.startswith("!메가리자몽Y"):
        await message.channel.send("`도감번호 6 메가리자몽Y \n종족값 78/104/78/159/115/100/총합:634`")
    if message.content.startswith("!꼬부기"):
        await message.channel.send("`도감번호 7 꼬부기 \n종족값 44/48/65/50/64/43/총합:314`")
    if message.content.startswith("!어니부기"):
        await message.channel.send("`도감번호 8 어니부기 \n종족값 59/63/80/65/80/58/총합:405`")
    if message.content.startswith("!거북왕"):
        await message.channel.send("`도감번호 9 거북왕 \n종족값 79/83/100/85/105/78/총합:530`")
    if message.content.startswith("!메가거북왕"):
        await message.channel.send("`도감번호 9 메가거북왕 \n종족값 79/103/120/135/115/78/총합:630`")
    if message.content.startswith("!캐터피"):
        await message.channel.send("`도감번호 10 캐터피 \n종족값 45/30/35/20/20/45/총합:195`")
    if message.content.startswith("!단데기"):
        await message.channel.send("`도감번호 11 단데기 \n종족값 50/20/55/25/25/30/총합:205`")
    if message.content.startswith("!버터플"):
        await message.channel.send("`도감번호 12 버터플 \n종족값 60/45/50/90/80/70/총합:395`")
    if message.content.startswith("!뿔충이"):
        await message.channel.send("`도감번호 13 뿔충이 \n종족값 40/35/30/20/20/50/총합:195`")
    if message.content.startswith("!딱충이"):
        await message.channel.send("`도감번호 14 딱충이 \n종족값 45/25/50/25/25/35/총합:205`")
    if message.content.startswith("!독침붕"):
        await message.channel.send("`도감번호 15 독침붕 \n종족값 65/90/40/45/80/75/총합:395`")
    if message.content.startswith("!메가독침붕"):
        await message.channel.send("`도감번호 15 메가독침붕 \n종족값 65/150/40/15/80/145/총합:495`")
    if message.content.startswith("!구구"):
        await message.channel.send("`도감번호 16 구구 \n종족값 40/45/40/35/35/56/총합:251`")
    if message.content.startswith("!피죤"):
        await message.channel.send("`도감번호 17 피죤 \n종족값 63/60/55/50/50/71/총합:349`")
    if message.content.startswith("!피죤투"):
        await message.channel.send("`도감번호 18 피죤투 \n종족값 83/80/75/70/70/101/총합:479`")
    if message.content.startswith("!메가피죤투"):
        await message.channel.send("`도감번호 18 메가피죤투 \n종족값 83/80/80/135/80/121/총합:579`")
    if message.content.startswith("!꼬렛"):
        await message.channel.send("`도감번호 19 꼬렛 \n종족값 30/56/35/25/35/72/총합:253`")
    if message.content.startswith("!꼬렛(알로라의 모습)"):
        await message.channel.send("`도감번호 19 꼬렛(알로라의 모습) \n종족값 30/56/35/25/35/72/총합:253`")
    if message.content.startswith("!레트라"):
        await message.channel.send("`도감번호 20 레트라 \n종족값 55/81/60/50/70/97/총합:413`")
    if message.content.startswith("!레트라(알로라의 모습)"):
        await message.channel.send("`도감번호 20 레트라(알로라의 모습) \n종족값 75/71/70/40/80/77/총합:413`")
    if message.content.startswith("!깨비참"):
        await message.channel.send("`도감번호 21 깨비참 \n종족값 40/60/30/31/31/70/총합:262`")
    if message.content.startswith("!깨비드릴조"):
        await message.channel.send("`도감번호 22 깨비드릴조 \n종족값 65/90/65/61/61/100/총합:442`")
    if message.content.startswith("!아보"):
        await message.channel.send("`도감번호 23 아보 \n종족값 35/60/44/40/54/55/총합:288`")
    if message.content.startswith("!아보크"):
        await message.channel.send("`도감번호 24 아보크 \n종족값 60/85/69/65/79/80/총합:438`")
    if message.content.startswith("!피카츄"):
        await message.channel.send("`도감번호 25 피카츄 \n종족값 35/55/40/50/50/90/총합:320`")
    if message.content.startswith("!라이츄"):
        await message.channel.send("`도감번호 26 라이츄 \n종족값 60/90/55/90/80/110/총합:485`")
    if message.content.startswith("!라이츄(알로라의 모습)"):
        await message.channel.send("`도감번호 26 라이츄(알로라의 모습) \n종족값 60/85/50/95/85/110/총합:485`")
    if message.content.startswith("!모래두지"):
        await message.channel.send("`도감번호 27 모래두지 \n종족값 50/75/85/20/30/40/총합:300`")
    if message.content.startswith("!모래두지(알로라의 모습)"):
        await message.channel.send("`도감번호 27 모래두지(알로라의 모습) \n종족값 50/75/90/10/35/40/총합:300`")
    if message.content.startswith("!고지"):
        await message.channel.send("`도감번호 28 고지 \n종족값 75/100/110/45/55/65/총합:450`")
    if message.content.startswith("!고지(알로라의 모습)"):
        await message.channel.send("`도감번호 28 고지(알로라의 모습) \n종족값 75/100/120/25/65/65/총합:450`")
    if message.content.startswith("!니드런♀"):
        await message.channel.send("`도감번호 29 니드런♀ \n종족값 55/47/52/40/40/41/총합:275`")
    if message.content.startswith("!니드리나"):
        await message.channel.send("`도감번호 30 니드리나 \n종족값 70/62/67/55/55/56/총합:365`")
    if message.content.startswith("!니드퀸"):
        await message.channel.send("`도감번호 31 니드퀸 \n종족값 90/92/87/75/85/76/총합:505`")
    if message.content.startswith("!니드런♂"):
        await message.channel.send("`도감번호 32 니드런♂ \n종족값 46/57/40/40/40/50/총합:273`")
    if message.content.startswith("!니드리노"):
        await message.channel.send("`도감번호 33 니드리노 \n종족값 61/72/57/55/55/65/총합:365`")
    if message.content.startswith("!니드킹"):
        await message.channel.send("`도감번호 34 니드킹 \n종족값 81/102/77/85/75/85/총합:505`")
    if message.content.startswith("!삐삐"):
        await message.channel.send("`도감번호 35 삐삐 \n종족값 70/45/48/60/65/35/총합:323`")
    if message.content.startswith("!픽시"):
        await message.channel.send("`도감번호 36 픽시 \n종족값 95/70/73/95/90/60/총합:483`")
    if message.content.startswith("!식스테일"):
        await message.channel.send("`도감번호 37 식스테일 \n종족값 38/41/40/50/65/65/총합:299`")
    if message.content.startswith("!식스테일(알로라의 모습)"):
        await message.channel.send("`도감번호 37 식스테일(알로라의 모습) \n종족값 38/41/40/50/65/65/총합:299`")
    if message.content.startswith("!나인테일"):
        await message.channel.send("`도감번호 38 나인테일 \n종족값 73/76/75/81/100/100/총합:505`")
    if message.content.startswith("!나인테일(알로라의 모습)"):
        await message.channel.send("`도감번호 38 나인테일(알로라의 모습) \n종족값 73/67/75/81/100/109/총합:505`")
    if message.content.startswith("!푸린"):
        await message.channel.send("`도감번호 39 푸린 \n종족값 115/45/20/45/25/20/총합:270`")
    if message.content.startswith("!푸크린"):
        await message.channel.send("`도감번호 40 푸크린 \n종족값 140/70/45/85/50/45/총합:435`")
    if message.content.startswith("!주뱃"):
        await message.channel.send("`도감번호 41 주뱃 \n종족값 40/45/35/30/40/55/총합:245`")
    if message.content.startswith("!골뱃"):
        await message.channel.send("`도감번호 42 골뱃 \n종족값 75/80/70/65/75/90/총합:455`")
    if message.content.startswith("!뚜벅쵸"):
        await message.channel.send("`도감번호 43 뚜벅쵸 \n종족값 45/50/55/75/65/30/총합:320`")
    if message.content.startswith("!냄새꼬"):
        await message.channel.send("`도감번호 44 냄새꼬 \n종족값 60/65/70/85/75/40/총합:395`")
    if message.content.startswith("!라플레시아"):
        await message.channel.send("`도감번호 45 라플레시아 \n종족값 75/80/85/110/90/50/총합:490`")
    if message.content.startswith("!파라스"):
        await message.channel.send("`도감번호 46 파라스 \n종족값 35/70/55/45/55/25/총합:285`")
    if message.content.startswith("!파라섹트"):
        await message.channel.send("`도감번호 47 파라섹트 \n종족값 60/95/80/60/80/30/총합:405`")
    if message.content.startswith("!콘팡"):
        await message.channel.send("`도감번호 48 콘팡 \n종족값 60/55/50/40/55/45/총합:305`")
    if message.content.startswith("!도나리"):
        await message.channel.send("`도감번호 49 도나리 \n종족값 70/65/60/90/75/90/총합:450`")
    if message.content.startswith("!디그다"):
        await message.channel.send("`도감번호 50 디그다 \n종족값 10/55/25/35/45/95/총합:265`")
    if message.content.startswith("!디그다(알로라의 모습)"):
        await message.channel.send("`도감번호 50 디그다(알로라의 모습) \n종족값 10/55/30/35/45/90/총합:265`")
    if message.content.startswith("!닥트리오"):
        await message.channel.send("`도감번호 51 닥트리오 \n종족값 35/80/50/50/70/120/총합:405`")
    if message.content.startswith("!닥트리오(알로라의 모습)"):
        await message.channel.send("`도감번호 51 닥트리오(알로라의 모습) \n종족값 35/100/60/50/70/110/총합:425`")
    if message.content.startswith("!나옹"):
        await message.channel.send("`도감번호 52 나옹 \n종족값 40/45/35/40/40/90/총합:290`")
    if message.content.startswith("!나옹(알로라의 모습)"):
        await message.channel.send("`도감번호 52 나옹(알로라의 모습) \n종족값 40/35/35/50/40/90/총합:290`")
    if message.content.startswith("!나옹(가라르의 모습)"):
        await message.channel.send("`도감번호 52 나옹(가라르의 모습) \n종족값 50/65/55/40/40/40/총합:290`")
    if message.content.startswith("!페르시온"):
        await message.channel.send("`도감번호 53 페르시온 \n종족값 65/70/60/65/65/115/총합:440`")
    if message.content.startswith("!페르시온(알로라의 모습)"):
        await message.channel.send("`도감번호 53 페르시온(알로라의 모습) \n종족값 65/60/60/75/65/115/총합:440`")
    if message.content.startswith("!고라파덕"):
        await message.channel.send("`도감번호 54 고라파덕 \n종족값 50/52/48/65/50/55/총합:320`")
    if message.content.startswith("!골덕"):
        await message.channel.send("`도감번호 55 골덕 \n종족값 80/82/78/95/80/85/총합:500`")
    if message.content.startswith("!망키"):
        await message.channel.send("`도감번호 56 망키 \n종족값 40/80/35/35/45/70/총합:305`")
    if message.content.startswith("!성원숭"):
        await message.channel.send("`도감번호 57 성원숭 \n종족값 65/105/60/60/70/95/총합:455`")
    if message.content.startswith("!가디"):
        await message.channel.send("`도감번호 58 가디 \n종족값 55/70/45/70/50/60/총합:350`")
    if message.content.startswith("!윈디"):
        await message.channel.send("`도감번호 59 윈디 \n종족값 90/110/80/100/80/95/총합:555`")
    if message.content.startswith("!발챙이"):
        await message.channel.send("`도감번호 60 발챙이 \n종족값 40/50/40/40/40/90/총합:300`")
    if message.content.startswith("!슈륙챙이"):
        await message.channel.send("`도감번호 61 슈륙챙이 \n종족값 65/65/65/50/50/90/총합:385`")
    if message.content.startswith("!강챙이"):
        await message.channel.send("`도감번호 62 강챙이 \n종족값 90/95/95/70/90/70/총합:510`")
    if message.content.startswith("!캐이시"):
        await message.channel.send("`도감번호 63 캐이시 \n종족값 25/20/15/105/55/90/총합:310`")
    if message.content.startswith("!윤겔라"):
        await message.channel.send("`도감번호 64 윤겔라 \n종족값 40/35/30/120/70/105/총합:400`")
    if message.content.startswith("!후딘"):
        await message.channel.send("`도감번호 65 후딘 \n종족값 55/50/45/135/95/120/총합:500`")
    if message.content.startswith("!메가후딘"):
        await message.channel.send("`도감번호 65 메가후딘 \n종족값 55/50/65/175/95/150/총합:590`")
    if message.content.startswith("!알통몬"):
        await message.channel.send("`도감번호 66 알통몬 \n종족값 70/80/50/35/35/35/총합:305`")
    if message.content.startswith("!근육몬"):
        await message.channel.send("`도감번호 67 근육몬 \n종족값 80/100/70/50/60/45/총합:405`")
    if message.content.startswith("!괴력몬"):
        await message.channel.send("`도감번호 68 괴력몬 \n종족값 90/130/80/65/85/55/총합:505`")
    if message.content.startswith("!모다피"):
        await message.channel.send("`도감번호 69 모다피 \n종족값 50/75/35/70/30/40/총합:300`")
    if message.content.startswith("!우츠동"):
        await message.channel.send("`도감번호 70 우츠동 \n종족값 65/90/50/85/45/55/총합:390`")
    if message.content.startswith("!우츠보트"):
        await message.channel.send("`도감번호 71 우츠보트 \n종족값 80/105/65/100/70/70/총합:490`")
    if message.content.startswith("!왕눈해"):
        await message.channel.send("`도감번호 72 왕눈해 \n종족값 40/40/35/50/100/70/총합:335`")
    if message.content.startswith("!독파리"):
        await message.channel.send("`도감번호 73 독파리 \n종족값 80/70/65/80/120/100/총합:515`")
    if message.content.startswith("!꼬마돌"):
        await message.channel.send("`도감번호 74 꼬마돌 \n종족값 40/80/100/30/30/20/총합:300`")
    if message.content.startswith("!꼬마돌(알로라의 모습)"):
        await message.channel.send("`도감번호 74 꼬마돌(알로라의 모습) \n종족값 40/80/100/30/30/20/총합:300`")
    if message.content.startswith("!데구리"):
        await message.channel.send("`도감번호 75 데구리 \n종족값 55/95/115/45/45/35/총합:390`")
    if message.content.startswith("!데구리(알로라의 모습)"):
        await message.channel.send("`도감번호 75 데구리(알로라의 모습) \n종족값 55/95/115/45/45/35/총합:390`")
    if message.content.startswith("!딱구리"):
        await message.channel.send("`도감번호 76 딱구리 \n종족값 80/120/130/55/65/45/총합:495`")
    if message.content.startswith("!딱구리(알로라의 모습)"):
        await message.channel.send("`도감번호 76 딱구리(알로라의 모습) \n종족값 80/120/130/55/65/45/총합:495`")
    if message.content.startswith("!포니타"):
        await message.channel.send("`도감번호 77 포니타 \n종족값 50/85/55/65/65/90/총합:410`")
    if message.content.startswith("!포니타(가라르의 모습)"):
        await message.channel.send("`도감번호 77 포니타(가라르의 모습) \n종족값 50/85/55/65/65/90/총합:410`")
    if message.content.startswith("!날쌩마"):
        await message.channel.send("`도감번호 78 날쌩마 \n종족값 65/100/70/80/80/105/총합:500`")
    if message.content.startswith("!날쌩마(가라르의 모습)"):
        await message.channel.send("`도감번호 78 날쌩마(가라르의 모습) \n종족값 65/100/70/80/80/105/총합:500`")
    if message.content.startswith("!야돈"):
        await message.channel.send("`도감번호 79 야돈 \n종족값 90/65/65/40/40/15/총합:315`")
    if message.content.startswith("!야도란"):
        await message.channel.send("`도감번호 80 야도란 \n종족값 95/75/110/100/80/30/총합:490`")
    if message.content.startswith("!메가야도란"):
        await message.channel.send("`도감번호 80 메가야도란 \n종족값 95/75/180/130/80/30/총합:590`")
    if message.content.startswith("!코일"):
        await message.channel.send("`도감번호 81 코일 \n종족값 25/35/70/95/55/45/총합:325`")
    if message.content.startswith("!레어코일"):
        await message.channel.send("`도감번호 82 레어코일 \n종족값 50/60/95/120/70/70/총합:465`")
    if message.content.startswith("!파오리"):
        await message.channel.send("`도감번호 83 파오리 \n종족값 52/65/55/58/62/60/총합:352`")
    if message.content.startswith("!파오리(가라르의 모습)"):
        await message.channel.send("`도감번호 83 파오리(가라르의 모습) \n종족값 52/95/55/58/62/55/총합:377`")
    if message.content.startswith("!두두"):
        await message.channel.send("`도감번호 84 두두 \n종족값 35/85/45/35/35/75/총합:310`")
    if message.content.startswith("!두트리오"):
        await message.channel.send("`도감번호 85 두트리오 \n종족값 60/110/70/60/60/100/총합:460`")
    if message.content.startswith("!쥬쥬"):
        await message.channel.send("`도감번호 86 쥬쥬 \n종족값 65/45/55/45/70/45/총합:325`")
    if message.content.startswith("!쥬레곤"):
        await message.channel.send("`도감번호 87 쥬레곤 \n종족값 90/70/80/70/95/70/총합:475`")
    if message.content.startswith("!질퍽이"):
        await message.channel.send("`도감번호 88 질퍽이 \n종족값 80/80/50/40/50/25/총합:325`")
    if message.content.startswith("!질퍽이(알로라의 모습)"):
        await message.channel.send("`도감번호 88 질퍽이(알로라의 모습) \n종족값 80/80/50/40/50/25/총합:325`")
    if message.content.startswith("!질뻐기"):
        await message.channel.send("`도감번호 89 질뻐기 \n종족값 105/105/75/65/100/50/총합:500`")
    if message.content.startswith("!질뻐기(알로라의 모습)"):
        await message.channel.send("`도감번호 89 질뻐기(알로라의 모습) \n종족값 105/105/75/65/100/50/총합:500`")
    if message.content.startswith("!셀러"):
        await message.channel.send("`도감번호 90 셀러 \n종족값 30/65/100/45/25/40/총합:305`")
    if message.content.startswith("!파르셀"):
        await message.channel.send("`도감번호 91 파르셀 \n종족값 50/95/180/85/45/70/총합:525`")
    if message.content.startswith("!고오스"):
        await message.channel.send("`도감번호 92 고오스 \n종족값 30/35/30/100/35/80/총합:310`")
    if message.content.startswith("!고우스트"):
        await message.channel.send("`도감번호 93 고우스트 \n종족값 45/50/45/115/55/95/총합:405`")
    if message.content.startswith("!팬텀"):
        await message.channel.send("`도감번호 94 팬텀 \n종족값 60/65/60/130/75/110/총합:500`")
    if message.content.startswith("!메가팬텀"):
        await message.channel.send("`도감번호 94 메가팬텀 \n종족값 60/65/80/170/95/130/총합:600`")
    if message.content.startswith("!롱스톤"):
        await message.channel.send("`도감번호 95 롱스톤 \n종족값 35/45/160/30/45/70/총합:385`")
    if message.content.startswith("!슬리프"):
        await message.channel.send("`도감번호 96 슬리프 \n종족값 60/48/45/43/90/42/총합:328`")
    if message.content.startswith("!슬리퍼"):
        await message.channel.send("`도감번호 97 슬리퍼 \n종족값 85/73/70/73/115/67/총합:483`")
    if message.content.startswith("!크랩"):
        await message.channel.send("`도감번호 98 크랩 \n종족값 30/105/90/25/25/50/총합:325`")
    if message.content.startswith("!킹크랩"):
        await message.channel.send("`도감번호 99 킹크랩 \n종족값 55/130/115/50/50/75/총합:475`")
    if message.content.startswith("!찌리리공"):
        await message.channel.send("`도감번호 100 찌리리공 \n종족값 40/30/50/55/55/100/총합:330`")
    if message.content.startswith("!붐볼"):
        await message.channel.send("`도감번호 101 붐볼 \n종족값 60/50/70/80/80/140/총합:480`")
    if message.content.startswith("!아라리"):
        await message.channel.send("`도감번호 102 아라리 \n종족값 60/40/80/60/45/40/총합:325`")
    if message.content.startswith("!나시"):
        await message.channel.send("`도감번호 103 나시 \n종족값 95/95/85/125/65/55/총합:520`")
    if message.content.startswith("!나시(알로라의 모습)"):
        await message.channel.send("`도감번호 103 나시(알로라의 모습) \n종족값 95/105/85/125/75/45/총합:530`")
    if message.content.startswith("!탕구리"):
        await message.channel.send("`도감번호 104 탕구리 \n종족값 50/50/95/40/50/35/총합:320`")
    if message.content.startswith("!텅구리"):
        await message.channel.send("`도감번호 105 텅구리 \n종족값 60/80/110/50/80/45/총합:425`")
    if message.content.startswith("!텅구리(알로라의 모습)"):
        await message.channel.send("`도감번호 105 텅구리(알로라의 모습) \n종족값 60/80/110/50/80/45/총합:425`")
    if message.content.startswith("!시라소몬"):
        await message.channel.send("`도감번호 106 시라소몬 \n종족값 50/120/53/35/110/87/총합:455`")
    if message.content.startswith("!홍수몬"):
        await message.channel.send("`도감번호 107 홍수몬 \n종족값 50/105/79/35/110/76/총합:455`")
    if message.content.startswith("!내루미"):
        await message.channel.send("`도감번호 108 내루미 \n종족값 90/55/75/60/75/30/총합:385`")
    if message.content.startswith("!또가스"):
        await message.channel.send("`도감번호 109 또가스 \n종족값 40/65/95/60/45/35/총합:340`")
    if message.content.startswith("!또도가스"):
        await message.channel.send("`도감번호 110 또도가스 \n종족값 65/90/120/85/70/60/총합:490`")
    if message.content.startswith("!또도가스(가라르의 모습)"):
        await message.channel.send("`도감번호 110 또도가스(가라르의 모습) \n종족값 65/90/120/85/70/60/총합:490`")
    if message.content.startswith("!뿔카노"):
        await message.channel.send("`도감번호 111 뿔카노 \n종족값 80/85/95/30/30/25/총합:345`")
    if message.content.startswith("!코뿌리"):
        await message.channel.send("`도감번호 112 코뿌리 \n종족값 105/130/120/45/45/40/총합:485`")
    if message.content.startswith("!럭키"):
        await message.channel.send("`도감번호 113 럭키 \n종족값 250/5/5/35/105/50/총합:450`")
    if message.content.startswith("!덩쿠리"):
        await message.channel.send("`도감번호 114 덩쿠리 \n종족값 65/55/115/100/40/60/총합:435`")
    if message.content.startswith("!캥카"):
        await message.channel.send("`도감번호 115 캥카 \n종족값 105/95/80/40/80/90/총합:490`")
    if message.content.startswith("!메가캥카"):
        await message.channel.send("`도감번호 115 메가캥카 \n종족값 105/125/100/60/100/100/총합:590`")
    if message.content.startswith("!쏘드라"):
        await message.channel.send("`도감번호 116 쏘드라 \n종족값 30/40/70/70/25/60/총합:295`")
    if message.content.startswith("!시드라"):
        await message.channel.send("`도감번호 117 시드라 \n종족값 55/65/95/95/45/85/총합:440`")
    if message.content.startswith("!콘치"):
        await message.channel.send("`도감번호 118 콘치 \n종족값 45/67/60/35/50/63/총합:320`")
    if message.content.startswith("!왕콘치"):
        await message.channel.send("`도감번호 119 왕콘치 \n종족값 80/92/65/65/80/68/총합:450`")
    if message.content.startswith("!별가사리"):
        await message.channel.send("`도감번호 120 별가사리 \n종족값 30/45/55/70/55/85/총합:340`")
    if message.content.startswith("!아쿠스타"):
        await message.channel.send("`도감번호 121 아쿠스타 \n종족값 60/75/85/100/85/115/총합:520`")
    if message.content.startswith("!마임맨"):
        await message.channel.send("`도감번호 122 마임맨 \n종족값 40/45/65/100/120/90/총합:460`")
    if message.content.startswith("!마임맨(가라르의 모습)"):
        await message.channel.send("`도감번호 122 마임맨(가라르의 모습) \n종족값 50/65/65/90/90/100/총합:460`")
    if message.content.startswith("!스라크"):
        await message.channel.send("`도감번호 123 스라크 \n종족값 70/110/80/55/80/105/총합:500`")
    if message.content.startswith("!루주라"):
        await message.channel.send("`도감번호 124 루주라 \n종족값 65/50/35/115/95/95/총합:455`")
    if message.content.startswith("!에레브"):
        await message.channel.send("`도감번호 125 에레브 \n종족값 65/83/57/95/85/105/총합:490`")
    if message.content.startswith("!마그마"):
        await message.channel.send("`도감번호 126 마그마 \n종족값 65/95/57/100/85/93/총합:495`")
    if message.content.startswith("!쁘사이저"):
        await message.channel.send("`도감번호 127 쁘사이저 \n종족값 65/125/100/55/70/85/총합:500`")
    if message.content.startswith("!메가쁘사이저"):
        await message.channel.send("`도감번호 127 메가쁘사이저 \n종족값 65/155/120/65/90/105/총합:600`")
    if message.content.startswith("!켄타로스"):
        await message.channel.send("`도감번호 128 켄타로스 \n종족값 75/100/95/40/70/110/총합:490`")
    if message.content.startswith("!잉어킹"):
        await message.channel.send("`도감번호 129 잉어킹 \n종족값 20/10/55/15/20/80/총합:200`")
    if message.content.startswith("!갸라도스"):
        await message.channel.send("`도감번호 130 갸라도스 \n종족값 95/125/79/60/100/81/총합:540`")
    if message.content.startswith("!메가갸라도스"):
        await message.channel.send("`도감번호 130 메가갸라도스 \n종족값 95/155/109/70/130/81/총합:640`")
    if message.content.startswith("!라프라스"):
        await message.channel.send("`도감번호 131 라프라스 \n종족값 130/85/80/85/95/60/총합:535`")
    if message.content.startswith("!메타몽"):
        await message.channel.send("`도감번호 132 메타몽 \n종족값 48/48/48/48/48/48/총합:288`")
    if message.content.startswith("!이브이"):
        await message.channel.send("`도감번호 133 이브이 \n종족값 55/55/50/45/65/55/총합:325`")
    if message.content.startswith("!샤미드"):
        await message.channel.send("`도감번호 134 샤미드 \n종족값 130/65/60/110/95/65/총합:525`")
    if message.content.startswith("!쥬피썬더"):
        await message.channel.send("`도감번호 135 쥬피썬더 \n종족값 65/65/60/110/95/130/총합:525`")
    if message.content.startswith("!부스터"):
        await message.channel.send("`도감번호 136 부스터 \n종족값 65/130/60/95/110/65/총합:525`")
    if message.content.startswith("!폴리곤"):
        await message.channel.send("`도감번호 137 폴리곤 \n종족값 65/60/70/85/75/40/총합:395`")
    if message.content.startswith("!암나이트"):
        await message.channel.send("`도감번호 138 암나이트 \n종족값 35/40/100/90/55/35/총합:355`")
    if message.content.startswith("!암스타"):
        await message.channel.send("`도감번호 139 암스타 \n종족값 70/60/125/115/70/55/총합:495`")
    if message.content.startswith("!투구"):
        await message.channel.send("`도감번호 140 투구 \n종족값 30/80/90/55/45/55/총합:355`")
    if message.content.startswith("!투구푸스"):
        await message.channel.send("`도감번호 141 투구푸스 \n종족값 60/115/105/65/70/80/총합:495`")
    if message.content.startswith("!프테라"):
        await message.channel.send("`도감번호 142 프테라 \n종족값 80/105/65/60/75/130/총합:515`")
    if message.content.startswith("!메가프테라"):
        await message.channel.send("`도감번호 142 메가프테라 \n종족값 80/135/85/70/95/150/총합:615`")
    if message.content.startswith("!잠만보"):
        await message.channel.send("`도감번호 143 잠만보 \n종족값 160/110/65/65/110/30/총합:540`")
    if message.content.startswith("!프리져"):
        await message.channel.send("`도감번호 144 프리져 \n종족값 90/85/100/95/125/85/총합:580`")
    if message.content.startswith("!썬더"):
        await message.channel.send("`도감번호 145 썬더 \n종족값 90/90/85/125/90/100/총합:580`")
    if message.content.startswith("!파이어"):
        await message.channel.send("`도감번호 146 파이어 \n종족값 90/100/90/125/85/90/총합:580`")
    if message.content.startswith("!미뇽"):
        await message.channel.send("`도감번호 147 미뇽 \n종족값 41/64/45/50/50/50/총합:300`")
    if message.content.startswith("!신뇽"):
        await message.channel.send("`도감번호 148 신뇽 \n종족값 61/84/65/70/70/70/총합:420`")
    if message.content.startswith("!망나뇽"):
        await message.channel.send("`도감번호 149 망나뇽 \n종족값 91/134/95/100/100/80/총합:600`")
    if message.content.startswith("!뮤츠"):
        await message.channel.send("`도감번호 150 뮤츠 \n종족값 106/110/90/154/90/130/총합:680`")
    if message.content.startswith("!메가뮤츠X"):
        await message.channel.send("`도감번호 150 메가뮤츠X \n종족값 106/190/100/154/100/130/총합:780`")
    if message.content.startswith("!메가뮤츠Y"):
        await message.channel.send("`도감번호 150 메가뮤츠Y \n종족값 106/150/70/194/120/140/총합:780`")
    if message.content.startswith("!뮤"):
        await message.channel.send("`도감번호 151 뮤 \n종족값 100/100/100/100/100/100/총합:600`")
    if message.content.startswith("!치코리타"):
        await message.channel.send("`도감번호 152 치코리타 \n종족값 45/49/65/49/65/45/총합:318`")
    if message.content.startswith("!베이리프"):
        await message.channel.send("`도감번호 153 베이리프 \n종족값 60/62/80/63/80/60/총합:405`")
    if message.content.startswith("!메가니움"):
        await message.channel.send("`도감번호 154 메가니움 \n종족값 80/82/100/83/100/80/총합:525`")
    if message.content.startswith("!브케인"):
        await message.channel.send("`도감번호 155 브케인 \n종족값 39/52/43/60/50/65/총합:309`")
    if message.content.startswith("!마그케인"):
        await message.channel.send("`도감번호 156 마그케인 \n종족값 58/64/58/80/65/80/총합:405`")
    if message.content.startswith("!블레이범"):
        await message.channel.send("`도감번호 157 블레이범 \n종족값 78/84/78/109/85/100/총합:534`")
    if message.content.startswith("!리아코"):
        await message.channel.send("`도감번호 158 리아코 \n종족값 50/65/64/44/48/43/총합:314`")
    if message.content.startswith("!엘리게이"):
        await message.channel.send("`도감번호 159 엘리게이 \n종족값 65/80/80/59/63/58/총합:405`")
    if message.content.startswith("!장크로다일"):
        await message.channel.send("`도감번호 160 장크로다일 \n종족값 85/105/100/79/83/78/총합:530`")
    if message.content.startswith("!꼬리선"):
        await message.channel.send("`도감번호 161 꼬리선 \n종족값 35/46/34/35/45/20/총합:215`")
    if message.content.startswith("!다꼬리"):
        await message.channel.send("`도감번호 162 다꼬리 \n종족값 85/76/64/45/55/90/총합:415`")
    if message.content.startswith("!부우부"):
        await message.channel.send("`도감번호 163 부우부 \n종족값 60/30/30/36/56/50/총합:262`")
    if message.content.startswith("!야부엉"):
        await message.channel.send("`도감번호 164 야부엉 \n종족값 100/50/50/76/96/70/총합:442`")
    if message.content.startswith("!레디바"):
        await message.channel.send("`도감번호 165 레디바 \n종족값 40/20/30/40/80/55/총합:265`")
    if message.content.startswith("!레디안"):
        await message.channel.send("`도감번호 166 레디안 \n종족값 55/35/50/55/110/85/총합:390`")
    if message.content.startswith("!페이검"):
        await message.channel.send("`도감번호 167 페이검 \n종족값 40/60/40/40/40/30/총합:250`")
    if message.content.startswith("!아리아도스"):
        await message.channel.send("`도감번호 168 아리아도스 \n종족값 70/90/70/60/60/40/총합:390`")
    if message.content.startswith("!크로뱃"):
        await message.channel.send("`도감번호 169 크로뱃 \n종족값 85/90/80/70/80/130/총합:535`")
    if message.content.startswith("!초라기"):
        await message.channel.send("`도감번호 170 초라기 \n종족값 75/38/38/56/56/67/총합:330`")
    if message.content.startswith("!랜턴"):
        await message.channel.send("`도감번호 171 랜턴 \n종족값 125/58/58/76/76/67/총합:460`")
    if message.content.startswith("!피츄"):
        await message.channel.send("`도감번호 172 피츄 \n종족값 20/40/15/35/35/60/총합:205`")
    if message.content.startswith("!삐"):
        await message.channel.send("`도감번호 173 삐 \n종족값 50/25/28/45/55/15/총합:218`")
    if message.content.startswith("!푸푸린"):
        await message.channel.send("`도감번호 174 푸푸린 \n종족값 90/30/15/40/20/15/총합:210`")
    if message.content.startswith("!토게피"):
        await message.channel.send("`도감번호 175 토게피 \n종족값 35/20/65/40/65/20/총합:245`")
    if message.content.startswith("!토게틱"):
        await message.channel.send("`도감번호 176 토게틱 \n종족값 55/40/85/80/105/40/총합:405`")
    if message.content.startswith("!네이티"):
        await message.channel.send("`도감번호 177 네이티 \n종족값 40/50/45/70/45/70/총합:320`")
    if message.content.startswith("!네이티오"):
        await message.channel.send("`도감번호 178 네이티오 \n종족값 65/75/70/95/70/95/총합:470`")
    if message.content.startswith("!메리프"):
        await message.channel.send("`도감번호 179 메리프 \n종족값 55/40/40/65/45/35/총합:280`")
    if message.content.startswith("!보송송"):
        await message.channel.send("`도감번호 180 보송송 \n종족값 70/55/55/80/60/45/총합:365`")
    if message.content.startswith("!전룡"):
        await message.channel.send("`도감번호 181 전룡 \n종족값 90/75/85/115/90/55/총합:510`")
    if message.content.startswith("!메가전룡"):
        await message.channel.send("`도감번호 181 메가전룡 \n종족값 90/95/105/165/110/45/총합:610`")
    if message.content.startswith("!아르코"):
        await message.channel.send("`도감번호 182 아르코 \n종족값 75/80/95/90/100/50/총합:490`")
    if message.content.startswith("!마릴"):
        await message.channel.send("`도감번호 183 마릴 \n종족값 70/20/50/20/50/40/총합:250`")
    if message.content.startswith("!마릴리"):
        await message.channel.send("`도감번호 184 마릴리 \n종족값 100/50/80/60/80/50/총합:420`")
    if message.content.startswith("!꼬지모"):
        await message.channel.send("`도감번호 185 꼬지모 \n종족값 70/100/115/30/65/30/총합:410`")
    if message.content.startswith("!왕구리"):
        await message.channel.send("`도감번호 186 왕구리 \n종족값 90/75/75/90/100/70/총합:500`")
    if message.content.startswith("!통통코"):
        await message.channel.send("`도감번호 187 통통코 \n종족값 35/35/40/35/55/50/총합:250`")
    if message.content.startswith("!두코"):
        await message.channel.send("`도감번호 188 두코 \n종족값 55/45/50/45/65/80/총합:340`")
    if message.content.startswith("!솜솜코"):
        await message.channel.send("`도감번호 189 솜솜코 \n종족값 75/55/70/55/95/110/총합:460`")
    if message.content.startswith("!에이팜"):
        await message.channel.send("`도감번호 190 에이팜 \n종족값 55/70/55/40/55/85/총합:360`")
    if message.content.startswith("!해너츠"):
        await message.channel.send("`도감번호 191 해너츠 \n종족값 30/30/30/30/30/30/총합:180`")
    if message.content.startswith("!해루미"):
        await message.channel.send("`도감번호 192 해루미 \n종족값 75/75/55/105/85/30/총합:425`")
    if message.content.startswith("!왕자리"):
        await message.channel.send("`도감번호 193 왕자리 \n종족값 65/65/45/75/45/95/총합:390`")
    if message.content.startswith("!우파"):
        await message.channel.send("`도감번호 194 우파 \n종족값 55/45/45/25/25/15/총합:210`")
    if message.content.startswith("!누오"):
        await message.channel.send("`도감번호 195 누오 \n종족값 95/85/85/65/65/35/총합:430`")
    if message.content.startswith("!에브이"):
        await message.channel.send("`도감번호 196 에브이 \n종족값 65/65/60/130/95/110/총합:525`")
    if message.content.startswith("!블래키"):
        await message.channel.send("`도감번호 197 블래키 \n종족값 95/65/110/60/130/65/총합:525`")
    if message.content.startswith("!니로우"):
        await message.channel.send("`도감번호 198 니로우 \n종족값 60/85/42/85/42/91/총합:405`")
    if message.content.startswith("!야도킹"):
        await message.channel.send("`도감번호 199 야도킹 \n종족값 95/75/80/100/110/30/총합:490`")
    if message.content.startswith("!무우마"):
        await message.channel.send("`도감번호 200 무우마 \n종족값 60/60/60/85/85/85/총합:435`")
    if message.content.startswith("!안농"):
        await message.channel.send("`도감번호 201 안농 \n종족값 48/72/48/72/48/48/총합:336`")
    if message.content.startswith("!마자용"):
        await message.channel.send("`도감번호 202 마자용 \n종족값 190/33/58/33/58/33/총합:405`")
    if message.content.startswith("!키링키"):
        await message.channel.send("`도감번호 203 키링키 \n종족값 70/80/65/90/65/85/총합:455`")
    if message.content.startswith("!피콘"):
        await message.channel.send("`도감번호 204 피콘 \n종족값 50/65/90/35/35/15/총합:290`")
    if message.content.startswith("!쏘콘"):
        await message.channel.send("`도감번호 205 쏘콘 \n종족값 75/90/140/60/60/40/총합:465`")
    if message.content.startswith("!노고치"):
        await message.channel.send("`도감번호 206 노고치 \n종족값 100/70/70/65/65/45/총합:415`")
    if message.content.startswith("!글라이거"):
        await message.channel.send("`도감번호 207 글라이거 \n종족값 65/75/105/35/65/85/총합:430`")
    if message.content.startswith("!강철톤"):
        await message.channel.send("`도감번호 208 강철톤 \n종족값 75/85/200/55/65/30/총합:510`")
    if message.content.startswith("!메가강철톤"):
        await message.channel.send("`도감번호 208 메가강철톤 \n종족값 75/125/230/55/95/30/총합:610`")
    if message.content.startswith("!블루"):
        await message.channel.send("`도감번호 209 블루 \n종족값 60/80/50/40/40/30/총합:300`")
    if message.content.startswith("!그랑블루"):
        await message.channel.send("`도감번호 210 그랑블루 \n종족값 90/120/75/60/60/45/총합:450`")
    if message.content.startswith("!침바루"):
        await message.channel.send("`도감번호 211 침바루 \n종족값 65/95/75/55/55/85/총합:430`")
    if message.content.startswith("!핫삼"):
        await message.channel.send("`도감번호 212 핫삼 \n종족값 70/130/100/55/80/65/총합:500`")
    if message.content.startswith("!메가핫삼"):
        await message.channel.send("`도감번호 212 메가핫삼 \n종족값 70/150/140/65/100/75/총합:600`")
    if message.content.startswith("!단단지"):
        await message.channel.send("`도감번호 213 단단지 \n종족값 20/10/230/10/230/5/총합:505`")
    if message.content.startswith("!헤라크로스"):
        await message.channel.send("`도감번호 214 헤라크로스 \n종족값 80/125/75/40/95/85/총합:500`")
    if message.content.startswith("!메가헤라크로스"):
        await message.channel.send("`도감번호 214 메가헤라크로스 \n종족값 80/185/115/40/105/75/총합:600`")
    if message.content.startswith("!포푸니"):
        await message.channel.send("`도감번호 215 포푸니 \n종족값 55/95/55/35/75/115/총합:430`")
    if message.content.startswith("!깜지곰"):
        await message.channel.send("`도감번호 216 깜지곰 \n종족값 60/80/50/50/50/40/총합:330`")
    if message.content.startswith("!링곰"):
        await message.channel.send("`도감번호 217 링곰 \n종족값 90/130/75/75/75/55/총합:500`")
    if message.content.startswith("!마그마그"):
        await message.channel.send("`도감번호 218 마그마그 \n종족값 40/40/40/70/40/20/총합:250`")
    if message.content.startswith("!마그카르고"):
        await message.channel.send("`도감번호 219 마그카르고 \n종족값 50/50/120/80/80/30/총합:410`")
    if message.content.startswith("!꾸꾸리"):
        await message.channel.send("`도감번호 220 꾸꾸리 \n종족값 50/50/40/30/30/50/총합:250`")
    if message.content.startswith("!메꾸리"):
        await message.channel.send("`도감번호 221 메꾸리 \n종족값 100/100/80/60/60/50/총합:450`")
    if message.content.startswith("!코산호"):
        await message.channel.send("`도감번호 222 코산호 \n종족값 55/55/85/65/85/35/총합:380`")
    if message.content.startswith("!코산호(가라르의 모습)"):
        await message.channel.send("`도감번호 222 코산호(가라르의 모습) \n종족값 60/55/100/65/100/30/총합:410`")
    if message.content.startswith("!총어"):
        await message.channel.send("`도감번호 223 총어 \n종족값 35/65/35/65/35/65/총합:300`")
    if message.content.startswith("!대포무노"):
        await message.channel.send("`도감번호 224 대포무노 \n종족값 75/105/75/105/75/45/총합:480`")
    if message.content.startswith("!딜리버드"):
        await message.channel.send("`도감번호 225 딜리버드 \n종족값 45/55/45/65/45/75/총합:330`")
    if message.content.startswith("!만타인"):
        await message.channel.send("`도감번호 226 만타인 \n종족값 65/40/70/80/140/70/총합:465`")
    if message.content.startswith("!무장조"):
        await message.channel.send("`도감번호 227 무장조 \n종족값 65/80/140/40/70/70/총합:465`")
    if message.content.startswith("!델빌"):
        await message.channel.send("`도감번호 228 델빌 \n종족값 45/60/30/80/50/65/총합:330`")
    if message.content.startswith("!헬가"):
        await message.channel.send("`도감번호 229 헬가 \n종족값 75/90/50/110/80/95/총합:500`")
    if message.content.startswith("!메가헬가"):
        await message.channel.send("`도감번호 229 메가헬가 \n종족값 75/90/90/140/90/115/총합:600`")
    if message.content.startswith("!킹드라"):
        await message.channel.send("`도감번호 230 킹드라 \n종족값 75/95/95/95/95/85/총합:540`")
    if message.content.startswith("!코코리"):
        await message.channel.send("`도감번호 231 코코리 \n종족값 90/60/60/40/40/40/총합:330`")
    if message.content.startswith("!코리갑"):
        await message.channel.send("`도감번호 232 코리갑 \n종족값 90/120/120/60/60/50/총합:500`")
    if message.content.startswith("!폴리곤2"):
        await message.channel.send("`도감번호 233 폴리곤2 \n종족값 85/80/90/105/95/60/총합:515`")
    if message.content.startswith("!노라키"):
        await message.channel.send("`도감번호 234 노라키 \n종족값 73/95/62/85/65/85/총합:465`")
    if message.content.startswith("!루브도"):
        await message.channel.send("`도감번호 235 루브도 \n종족값 55/20/35/20/45/75/총합:250`")
    if message.content.startswith("!배루키"):
        await message.channel.send("`도감번호 236 배루키 \n종족값 35/35/35/35/35/35/총합:210`")
    if message.content.startswith("!카포에라"):
        await message.channel.send("`도감번호 237 카포에라 \n종족값 50/95/95/35/110/70/총합:455`")
    if message.content.startswith("!뽀뽀라"):
        await message.channel.send("`도감번호 238 뽀뽀라 \n종족값 45/30/15/85/65/65/총합:305`")
    if message.content.startswith("!에레키드"):
        await message.channel.send("`도감번호 239 에레키드 \n종족값 45/63/37/65/55/95/총합:360`")
    if message.content.startswith("!마그비"):
        await message.channel.send("`도감번호 240 마그비 \n종족값 45/75/37/70/55/83/총합:365`")
    if message.content.startswith("!밀탱크"):
        await message.channel.send("`도감번호 241 밀탱크 \n종족값 95/80/105/40/70/100/총합:490`")
    if message.content.startswith("!해피너스"):
        await message.channel.send("`도감번호 242 해피너스 \n종족값 255/10/10/75/135/55/총합:540`")
    if message.content.startswith("!라이코"):
        await message.channel.send("`도감번호 243 라이코 \n종족값 90/85/75/115/100/115/총합:580`")
    if message.content.startswith("!앤테이"):
        await message.channel.send("`도감번호 244 앤테이 \n종족값 115/115/85/90/75/100/총합:580`")
    if message.content.startswith("!스이쿤"):
        await message.channel.send("`도감번호 245 스이쿤 \n종족값 100/75/115/90/115/85/총합:580`")
    if message.content.startswith("!애버라스"):
        await message.channel.send("`도감번호 246 애버라스 \n종족값 50/64/50/45/50/41/총합:300`")
    if message.content.startswith("!데기라스"):
        await message.channel.send("`도감번호 247 데기라스 \n종족값 70/84/70/65/70/51/총합:410`")
    if message.content.startswith("!마기라스"):
        await message.channel.send("`도감번호 248 마기라스 \n종족값 100/134/110/95/100/61/총합:600`")
    if message.content.startswith("!메가마기라스"):
        await message.channel.send("`도감번호 248 메가마기라스 \n종족값 100/164/150/95/120/71/총합:700`")
    if message.content.startswith("!루기아"):
        await message.channel.send("`도감번호 249 루기아 \n종족값 106/90/130/90/154/110/총합:680`")
    if message.content.startswith("!칠색조"):
        await message.channel.send("`도감번호 250 칠색조 \n종족값 106/130/90/110/154/90/총합:680`")
    if message.content.startswith("!세레비"):
        await message.channel.send("`도감번호 251 세레비 \n종족값 100/100/100/100/100/100/총합:600`")
    if message.content.startswith("!나무지기"):
        await message.channel.send("`도감번호 252 나무지기 \n종족값 40/45/35/65/55/70/총합:310`")
    if message.content.startswith("!나무돌이"):
        await message.channel.send("`도감번호 253 나무돌이 \n종족값 50/65/45/85/65/95/총합:405`")
    if message.content.startswith("!나무킹"):
        await message.channel.send("`도감번호 254 나무킹 \n종족값 70/85/65/105/85/120/총합:530`")
    if message.content.startswith("!메가나무킹"):
        await message.channel.send("`도감번호 254 메가나무킹 \n종족값 70/110/75/145/85/145/총합:630`")
    if message.content.startswith("!아차모"):
        await message.channel.send("`도감번호 255 아차모 \n종족값 45/60/40/70/50/45/총합:310`")
    if message.content.startswith("!영치코"):
        await message.channel.send("`도감번호 256 영치코 \n종족값 60/85/60/85/60/55/총합:405`")
    if message.content.startswith("!번치코"):
        await message.channel.send("`도감번호 257 번치코 \n종족값 80/120/70/110/70/80/총합:530`")
    if message.content.startswith("!메가번치코"):
        await message.channel.send("`도감번호 257 메가번치코 \n종족값 80/160/80/130/80/100/총합:630`")
    if message.content.startswith("!물짱이"):
        await message.channel.send("`도감번호 258 물짱이 \n종족값 50/70/50/50/50/40/총합:310`")
    if message.content.startswith("!늪짱이"):
        await message.channel.send("`도감번호 259 늪짱이 \n종족값 70/85/70/60/70/50/총합:405`")
    if message.content.startswith("!대짱이"):
        await message.channel.send("`도감번호 260 대짱이 \n종족값 100/110/90/85/90/60/총합:535`")
    if message.content.startswith("!메가대짱이"):
        await message.channel.send("`도감번호 260 메가대짱이 \n종족값 100/150/110/95/110/70/총합:635`")
    if message.content.startswith("!포챠나"):
        await message.channel.send("`도감번호 261 포챠나 \n종족값 35/55/35/30/30/35/총합:220`")
    if message.content.startswith("!그라에나"):
        await message.channel.send("`도감번호 262 그라에나 \n종족값 70/90/70/60/60/70/총합:420`")
    if message.content.startswith("!지그제구리"):
        await message.channel.send("`도감번호 263 지그제구리 \n종족값 38/30/41/30/41/60/총합:240`")
    if message.content.startswith("!지그제구리(가라르의 모습)"):
        await message.channel.send("`도감번호 263 지그제구리(가라르의 모습) \n종족값 38/30/41/30/41/60/총합:240`")
    if message.content.startswith("!직구리"):
        await message.channel.send("`도감번호 264 직구리 \n종족값 78/70/61/50/61/100/총합:420`")
    if message.content.startswith("!직구리(가라르의 모습)"):
        await message.channel.send("`도감번호 264 직구리(가라르의 모습) \n종족값 78/70/61/50/61/100/총합:420`")
    if message.content.startswith("!개무소"):
        await message.channel.send("`도감번호 265 개무소 \n종족값 45/45/35/20/30/20/총합:195`")
    if message.content.startswith("!실쿤"):
        await message.channel.send("`도감번호 266 실쿤 \n종족값 50/35/55/25/25/15/총합:205`")
    if message.content.startswith("!뷰티플라이"):
        await message.channel.send("`도감번호 267 뷰티플라이 \n종족값 60/70/50/100/50/65/총합:395`")
    if message.content.startswith("!카스쿤"):
        await message.channel.send("`도감번호 268 카스쿤 \n종족값 50/35/55/25/25/15/총합:205`")
    if message.content.startswith("!독케일"):
        await message.channel.send("`도감번호 269 독케일 \n종족값 60/50/70/50/90/65/총합:385`")
    if message.content.startswith("!연꽃몬"):
        await message.channel.send("`도감번호 270 연꽃몬 \n종족값 40/30/30/40/50/30/총합:220`")
    if message.content.startswith("!로토스"):
        await message.channel.send("`도감번호 271 로토스 \n종족값 60/50/50/60/70/50/총합:340`")
    if message.content.startswith("!로파파"):
        await message.channel.send("`도감번호 272 로파파 \n종족값 80/70/70/90/100/70/총합:480`")
    if message.content.startswith("!도토링"):
        await message.channel.send("`도감번호 273 도토링 \n종족값 40/40/50/30/30/30/총합:220`")
    if message.content.startswith("!잎새코"):
        await message.channel.send("`도감번호 274 잎새코 \n종족값 70/70/40/60/40/60/총합:340`")
    if message.content.startswith("!다탱구"):
        await message.channel.send("`도감번호 275 다탱구 \n종족값 90/100/60/90/60/80/총합:480`")
    if message.content.startswith("!테일로"):
        await message.channel.send("`도감번호 276 테일로 \n종족값 40/55/30/30/30/85/총합:270`")
    if message.content.startswith("!스왈로"):
        await message.channel.send("`도감번호 277 스왈로 \n종족값 60/85/60/50/50/125/총합:430`")
    if message.content.startswith("!갈모매"):
        await message.channel.send("`도감번호 278 갈모매 \n종족값 40/30/30/55/30/85/총합:270`")
    if message.content.startswith("!패리퍼"):
        await message.channel.send("`도감번호 279 패리퍼 \n종족값 60/50/100/85/70/65/총합:430`")
    if message.content.startswith("!랄토스"):
        await message.channel.send("`도감번호 280 랄토스 \n종족값 28/25/25/45/35/40/총합:198`")
    if message.content.startswith("!킬리아"):
        await message.channel.send("`도감번호 281 킬리아 \n종족값 38/35/35/65/55/50/총합:278`")
    if message.content.startswith("!가디안"):
        await message.channel.send("`도감번호 282 가디안 \n종족값 68/65/65/125/115/80/총합:518`")
    if message.content.startswith("!메가가디안"):
        await message.channel.send("`도감번호 282 메가가디안 \n종족값 68/85/65/165/135/100/총합:618`")
    if message.content.startswith("!비구술"):
        await message.channel.send("`도감번호 283 비구술 \n종족값 40/30/32/50/52/65/총합:269`")
    if message.content.startswith("!비나방"):
        await message.channel.send("`도감번호 284 비나방 \n종족값 70/60/62/80/82/60/총합:414`")
    if message.content.startswith("!버섯꼬"):
        await message.channel.send("`도감번호 285 버섯꼬 \n종족값 60/40/60/40/60/35/총합:295`")
    if message.content.startswith("!버섯모"):
        await message.channel.send("`도감번호 286 버섯모 \n종족값 60/130/80/60/60/70/총합:460`")
    if message.content.startswith("!게을로"):
        await message.channel.send("`도감번호 287 게을로 \n종족값 60/60/60/35/35/30/총합:280`")
    if message.content.startswith("!발바로"):
        await message.channel.send("`도감번호 288 발바로 \n종족값 80/80/80/55/55/90/총합:440`")
    if message.content.startswith("!게을킹"):
        await message.channel.send("`도감번호 289 게을킹 \n종족값 150/160/100/95/65/100/총합:670`")
    if message.content.startswith("!토중몬"):
        await message.channel.send("`도감번호 290 토중몬 \n종족값 31/45/90/30/30/40/총합:266`")
    if message.content.startswith("!아이스크"):
        await message.channel.send("`도감번호 291 아이스크 \n종족값 61/90/45/50/50/160/총합:456`")
    if message.content.startswith("!껍질몬"):
        await message.channel.send("`도감번호 292 껍질몬 \n종족값 1/90/45/30/30/40/총합:236`")
    if message.content.startswith("!소곤룡"):
        await message.channel.send("`도감번호 293 소곤룡 \n종족값 64/51/23/51/23/28/총합:240`")
    if message.content.startswith("!노공룡"):
        await message.channel.send("`도감번호 294 노공룡 \n종족값 84/71/43/71/43/48/총합:360`")
    if message.content.startswith("!폭음룡"):
        await message.channel.send("`도감번호 295 폭음룡 \n종족값 104/91/63/91/73/68/총합:490`")
    if message.content.startswith("!마크탕"):
        await message.channel.send("`도감번호 296 마크탕 \n종족값 72/60/30/20/30/25/총합:237`")
    if message.content.startswith("!하리뭉"):
        await message.channel.send("`도감번호 297 하리뭉 \n종족값 144/120/60/40/60/50/총합:474`")
    if message.content.startswith("!루리리"):
        await message.channel.send("`도감번호 298 루리리 \n종족값 50/20/40/20/40/20/총합:190`")
    if message.content.startswith("!코코파스"):
        await message.channel.send("`도감번호 299 코코파스 \n종족값 30/45/135/45/90/30/총합:375`")
    if message.content.startswith("!에나비"):
        await message.channel.send("`도감번호 300 에나비 \n종족값 50/45/45/35/35/50/총합:260`")
    if message.content.startswith("!델케티"):
        await message.channel.send("`도감번호 301 델케티 \n종족값 70/65/65/55/55/70/총합:380`")
    if message.content.startswith("!깜까미"):
        await message.channel.send("`도감번호 302 깜까미 \n종족값 50/75/75/65/65/50/총합:380`")
    if message.content.startswith("!메가깜까미"):
        await message.channel.send("`도감번호 302 메가깜까미 \n종족값 50/85/125/85/115/20/총합:480`")
    if message.content.startswith("!입치트"):
        await message.channel.send("`도감번호 303 입치트 \n종족값 50/85/85/55/55/50/총합:380`")
    if message.content.startswith("!메가입치트"):
        await message.channel.send("`도감번호 303 메가입치트 \n종족값 50/105/125/55/95/50/총합:480`")
    if message.content.startswith("!가보리"):
        await message.channel.send("`도감번호 304 가보리 \n종족값 50/70/100/40/40/30/총합:330`")
    if message.content.startswith("!갱도라"):
        await message.channel.send("`도감번호 305 갱도라 \n종족값 60/90/140/50/50/40/총합:430`")
    if message.content.startswith("!보스로라"):
        await message.channel.send("`도감번호 306 보스로라 \n종족값 70/110/180/60/60/50/총합:530`")
    if message.content.startswith("!메가보스로라"):
        await message.channel.send("`도감번호 306 메가보스로라 \n종족값 70/140/230/60/80/50/총합:630`")
    if message.content.startswith("!요가랑"):
        await message.channel.send("`도감번호 307 요가랑 \n종족값 30/40/55/40/55/60/총합:280`")
    if message.content.startswith("!요가램"):
        await message.channel.send("`도감번호 308 요가램 \n종족값 60/60/75/60/75/80/총합:410`")
    if message.content.startswith("!메가요가램"):
        await message.channel.send("`도감번호 308 메가요가램 \n종족값 60/100/85/80/85/100/총합:510`")
    if message.content.startswith("!썬더라이"):
        await message.channel.send("`도감번호 309 썬더라이 \n종족값 40/45/40/65/40/65/총합:295`")
    if message.content.startswith("!썬더볼트"):
        await message.channel.send("`도감번호 310 썬더볼트 \n종족값 70/75/60/105/60/105/총합:475`")
    if message.content.startswith("!메가썬더볼트"):
        await message.channel.send("`도감번호 310 메가썬더볼트 \n종족값 70/75/80/135/80/135/총합:575`")
    if message.content.startswith("!플러시"):
        await message.channel.send("`도감번호 311 플러시 \n종족값 60/50/40/85/75/95/총합:405`")
    if message.content.startswith("!마이농"):
        await message.channel.send("`도감번호 312 마이농 \n종족값 60/40/50/75/85/95/총합:405`")
    if message.content.startswith("!볼비트"):
        await message.channel.send("`도감번호 313 볼비트 \n종족값 65/73/55/47/75/85/총합:400`")
    if message.content.startswith("!네오비트"):
        await message.channel.send("`도감번호 314 네오비트 \n종족값 65/47/55/73/75/85/총합:400`")
    if message.content.startswith("!로젤리아"):
        await message.channel.send("`도감번호 315 로젤리아 \n종족값 50/60/45/100/80/65/총합:400`")
    if message.content.startswith("!꼴깍몬"):
        await message.channel.send("`도감번호 316 꼴깍몬 \n종족값 70/43/53/43/53/40/총합:302`")
    if message.content.startswith("!꿀꺽몬"):
        await message.channel.send("`도감번호 317 꿀꺽몬 \n종족값 100/73/83/73/83/55/총합:467`")
    if message.content.startswith("!샤프니아"):
        await message.channel.send("`도감번호 318 샤프니아 \n종족값 45/90/20/65/20/65/총합:305`")
    if message.content.startswith("!샤크니아"):
        await message.channel.send("`도감번호 319 샤크니아 \n종족값 70/120/40/95/40/95/총합:460`")
    if message.content.startswith("!메가샤크니아"):
        await message.channel.send("`도감번호 319 메가샤크니아 \n종족값 70/140/70/110/65/105/총합:560`")
    if message.content.startswith("!고래왕자"):
        await message.channel.send("`도감번호 320 고래왕자 \n종족값 130/70/35/70/35/60/총합:400`")
    if message.content.startswith("!고래왕"):
        await message.channel.send("`도감번호 321 고래왕 \n종족값 170/90/45/90/45/60/총합:500`")
    if message.content.startswith("!둔타"):
        await message.channel.send("`도감번호 322 둔타 \n종족값 60/60/40/65/45/35/총합:305`")
    if message.content.startswith("!폭타"):
        await message.channel.send("`도감번호 323 폭타 \n종족값 70/100/70/105/75/40/총합:460`")
    if message.content.startswith("!메가폭타"):
        await message.channel.send("`도감번호 323 메가폭타 \n종족값 70/120/100/145/105/20/총합:560`")
    if message.content.startswith("!코터스"):
        await message.channel.send("`도감번호 324 코터스 \n종족값 70/85/140/85/70/20/총합:470`")
    if message.content.startswith("!피그점프"):
        await message.channel.send("`도감번호 325 피그점프 \n종족값 60/25/35/70/80/60/총합:330`")
    if message.content.startswith("!피그킹"):
        await message.channel.send("`도감번호 326 피그킹 \n종족값 80/45/65/90/110/80/총합:470`")
    if message.content.startswith("!얼루기"):
        await message.channel.send("`도감번호 327 얼루기 \n종족값 60/60/60/60/60/60/총합:360`")
    if message.content.startswith("!톱치"):
        await message.channel.send("`도감번호 328 톱치 \n종족값 45/100/45/45/45/10/총합:290`")
    if message.content.startswith("!비브라바"):
        await message.channel.send("`도감번호 329 비브라바 \n종족값 50/70/50/50/50/70/총합:340`")
    if message.content.startswith("!플라이곤"):
        await message.channel.send("`도감번호 330 플라이곤 \n종족값 80/100/80/80/80/100/총합:520`")
    if message.content.startswith("!선인왕"):
        await message.channel.send("`도감번호 331 선인왕 \n종족값 50/85/40/85/40/35/총합:335`")
    if message.content.startswith("!밤선인"):
        await message.channel.send("`도감번호 332 밤선인 \n종족값 70/115/60/115/60/55/총합:475`")
    if message.content.startswith("!파비코"):
        await message.channel.send("`도감번호 333 파비코 \n종족값 45/40/60/40/75/50/총합:310`")
    if message.content.startswith("!파비코리"):
        await message.channel.send("`도감번호 334 파비코리 \n종족값 75/70/90/70/105/80/총합:490`")
    if message.content.startswith("!메가파비코리"):
        await message.channel.send("`도감번호 334 메가파비코리 \n종족값 75/110/110/110/105/80/총합:590`")
    if message.content.startswith("!쟝고"):
        await message.channel.send("`도감번호 335 쟝고 \n종족값 73/115/60/60/60/90/총합:458`")
    if message.content.startswith("!세비퍼"):
        await message.channel.send("`도감번호 336 세비퍼 \n종족값 73/100/60/100/60/65/총합:458`")
    if message.content.startswith("!루나톤"):
        await message.channel.send("`도감번호 337 루나톤 \n종족값 70/55/65/95/85/70/총합:440`")
    if message.content.startswith("!솔록"):
        await message.channel.send("`도감번호 338 솔록 \n종족값 70/95/85/55/65/70/총합:440`")
    if message.content.startswith("!미꾸리"):
        await message.channel.send("`도감번호 339 미꾸리 \n종족값 50/48/43/46/41/60/총합:288`")
    if message.content.startswith("!메깅"):
        await message.channel.send("`도감번호 340 메깅 \n종족값 110/78/73/76/71/60/총합:468`")
    if message.content.startswith("!가재군"):
        await message.channel.send("`도감번호 341 가재군 \n종족값 43/80/65/50/35/35/총합:308`")
    if message.content.startswith("!가재장군"):
        await message.channel.send("`도감번호 342 가재장군 \n종족값 63/120/85/90/55/55/총합:468`")
    if message.content.startswith("!오뚝군"):
        await message.channel.send("`도감번호 343 오뚝군 \n종족값 40/40/55/40/70/55/총합:300`")
    if message.content.startswith("!점토도리"):
        await message.channel.send("`도감번호 344 점토도리 \n종족값 60/70/105/70/120/75/총합:500`")
    if message.content.startswith("!릴링"):
        await message.channel.send("`도감번호 345 릴링 \n종족값 66/41/77/61/87/23/총합:355`")
    if message.content.startswith("!릴리요"):
        await message.channel.send("`도감번호 346 릴리요 \n종족값 86/81/97/81/107/43/총합:495`")
    if message.content.startswith("!아노딥스"):
        await message.channel.send("`도감번호 347 아노딥스 \n종족값 45/95/50/40/50/75/총합:355`")
    if message.content.startswith("!아말도"):
        await message.channel.send("`도감번호 348 아말도 \n종족값 75/125/100/70/80/45/총합:495`")
    if message.content.startswith("!빈티나"):
        await message.channel.send("`도감번호 349 빈티나 \n종족값 20/15/20/10/55/80/총합:200`")
    if message.content.startswith("!밀로틱"):
        await message.channel.send("`도감번호 350 밀로틱 \n종족값 95/60/79/100/125/81/총합:540`")
    if message.content.startswith("!캐스퐁"):
        await message.channel.send("`도감번호 351 캐스퐁 \n종족값 70/70/70/70/70/70/총합:420`")
    if message.content.startswith("!켈리몬"):
        await message.channel.send("`도감번호 352 켈리몬 \n종족값 60/90/70/60/120/40/총합:440`")
    if message.content.startswith("!어둠대신"):
        await message.channel.send("`도감번호 353 어둠대신 \n종족값 44/75/35/63/33/45/총합:295`")
    if message.content.startswith("!다크펫"):
        await message.channel.send("`도감번호 354 다크펫 \n종족값 64/115/65/83/63/65/총합:455`")
    if message.content.startswith("!메가다크펫"):
        await message.channel.send("`도감번호 354 메가다크펫 \n종족값 64/165/75/93/83/75/총합:555`")
    if message.content.startswith("!해골몽"):
        await message.channel.send("`도감번호 355 해골몽 \n종족값 20/40/90/30/90/25/총합:295`")
    if message.content.startswith("!미라몽"):
        await message.channel.send("`도감번호 356 미라몽 \n종족값 40/70/130/60/130/25/총합:455`")
    if message.content.startswith("!트로피우스"):
        await message.channel.send("`도감번호 357 트로피우스 \n종족값 99/68/83/72/87/51/총합:460`")
    if message.content.startswith("!치렁"):
        await message.channel.send("`도감번호 358 치렁 \n종족값 65/50/70/95/80/65/총합:425`")
    if message.content.startswith("!앱솔"):
        await message.channel.send("`도감번호 359 앱솔 \n종족값 65/130/60/75/60/75/총합:465`")
    if message.content.startswith("!메가앱솔"):
        await message.channel.send("`도감번호 359 메가앱솔 \n종족값 65/150/60/115/60/115/총합:565`")
    if message.content.startswith("!마자"):
        await message.channel.send("`도감번호 360 마자 \n종족값 95/23/48/23/48/23/총합:260`")
    if message.content.startswith("!눈꼬마"):
        await message.channel.send("`도감번호 361 눈꼬마 \n종족값 50/50/50/50/50/50/총합:300`")
    if message.content.startswith("!얼음귀신"):
        await message.channel.send("`도감번호 362 얼음귀신 \n종족값 80/80/80/80/80/80/총합:480`")
    if message.content.startswith("!메가얼음귀신"):
        await message.channel.send("`도감번호 362 메가얼음귀신 \n종족값 80/120/80/120/80/100/총합:580`")
    if message.content.startswith("!대굴레오"):
        await message.channel.send("`도감번호 363 대굴레오 \n종족값 70/40/50/55/50/25/총합:290`")
    if message.content.startswith("!씨레오"):
        await message.channel.send("`도감번호 364 씨레오 \n종족값 90/60/70/75/70/45/총합:410`")
    if message.content.startswith("!씨카이저"):
        await message.channel.send("`도감번호 365 씨카이저 \n종족값 110/80/90/95/90/65/총합:530`")
    if message.content.startswith("!진주몽"):
        await message.channel.send("`도감번호 366 진주몽 \n종족값 35/64/85/74/55/32/총합:345`")
    if message.content.startswith("!헌테일"):
        await message.channel.send("`도감번호 367 헌테일 \n종족값 55/104/105/94/75/52/총합:485`")
    if message.content.startswith("!분홍장이"):
        await message.channel.send("`도감번호 368 분홍장이 \n종족값 55/84/105/114/75/52/총합:485`")
    if message.content.startswith("!시라칸"):
        await message.channel.send("`도감번호 369 시라칸 \n종족값 100/90/130/45/65/55/총합:485`")
    if message.content.startswith("!사랑동이"):
        await message.channel.send("`도감번호 370 사랑동이 \n종족값 43/30/55/40/65/97/총합:330`")
    if message.content.startswith("!아공이"):
        await message.channel.send("`도감번호 371 아공이 \n종족값 45/75/60/40/30/50/총합:300`")
    if message.content.startswith("!쉘곤"):
        await message.channel.send("`도감번호 372 쉘곤 \n종족값 65/95/100/60/50/50/총합:420`")
    if message.content.startswith("!보만다"):
        await message.channel.send("`도감번호 373 보만다 \n종족값 95/135/80/110/80/100/총합:600`")
    if message.content.startswith("!메가보만다"):
        await message.channel.send("`도감번호 373 메가보만다 \n종족값 95/145/130/120/90/120/총합:700`")
    if message.content.startswith("!메탕"):
        await message.channel.send("`도감번호 374 메탕 \n종족값 40/55/80/35/60/30/총합:300`")
    if message.content.startswith("!메탕구"):
        await message.channel.send("`도감번호 375 메탕구 \n종족값 60/75/100/55/80/50/총합:420`")
    if message.content.startswith("!메타그로스"):
        await message.channel.send("`도감번호 376 메타그로스 \n종족값 80/135/130/95/90/70/총합:600`")
    if message.content.startswith("!메가메타그로스"):
        await message.channel.send("`도감번호 376 메가메타그로스 \n종족값 80/145/150/105/110/110/총합:700`")
    if message.content.startswith("!레지락"):
        await message.channel.send("`도감번호 377 레지락 \n종족값 80/100/200/50/100/50/총합:580`")
    if message.content.startswith("!레지아이스"):
        await message.channel.send("`도감번호 378 레지아이스 \n종족값 80/50/100/100/200/50/총합:580`")
    if message.content.startswith("!레지스틸"):
        await message.channel.send("`도감번호 379 레지스틸 \n종족값 80/75/150/75/150/50/총합:580`")
    if message.content.startswith("!라티아스"):
        await message.channel.send("`도감번호 380 라티아스 \n종족값 80/80/90/110/130/110/총합:600`")
    if message.content.startswith("!메가라티아스"):
        await message.channel.send("`도감번호 380 메가라티아스 \n종족값 80/100/120/140/150/110/총합:700`")
    if message.content.startswith("!라티오스"):
        await message.channel.send("`도감번호 381 라티오스 \n종족값 80/90/80/130/110/110/총합:600`")
    if message.content.startswith("!메가라티오스"):
        await message.channel.send("`도감번호 381 메가라티오스 \n종족값 80/130/100/160/120/110/총합:700`")
    if message.content.startswith("!가이오가"):
        await message.channel.send("`도감번호 382 가이오가 \n종족값 100/100/90/150/140/90/총합:670`")
    if message.content.startswith("!원시가이오가"):
        await message.channel.send("`도감번호 382 원시가이오가 \n종족값 100/150/90/180/160/90/총합:770`")
    if message.content.startswith("!그란돈"):
        await message.channel.send("`도감번호 383 그란돈 \n종족값 100/150/140/100/90/90/총합:670`")
    if message.content.startswith("!원시그란돈"):
        await message.channel.send("`도감번호 383 원시그란돈 \n종족값 100/180/160/150/90/90/총합:770`")
    if message.content.startswith("!레쿠쟈"):
        await message.channel.send("`도감번호 384 레쿠쟈 \n종족값 105/150/90/150/90/95/총합:680`")
    if message.content.startswith("!메가레쿠쟈"):
        await message.channel.send("`도감번호 384 메가레쿠쟈 \n종족값 105/180/100/180/100/115/총합:780`")
    if message.content.startswith("!지라치"):
        await message.channel.send("`도감번호 385 지라치 \n종족값 100/100/100/100/100/100/총합:600`")
    if message.content.startswith("!테오키스(노말폼)"):
        await message.channel.send("`도감번호 386 테오키스(노말폼) \n종족값 50/150/50/150/50/150/총합:600`")
    if message.content.startswith("!테오키스(어택폼)"):
        await message.channel.send("`도감번호 386 테오키스(어택폼) \n종족값 50/180/20/180/20/150/총합:600`")
    if message.content.startswith("!테오키스(디펜스폼)"):
        await message.channel.send("`도감번호 386 테오키스(디펜스폼) \n종족값 50/70/160/70/160/90/총합:600`")
    if message.content.startswith("!테오키스(스피드폼)"):
        await message.channel.send("`도감번호 386 테오키스(스피드폼) \n종족값 50/95/90/95/90/180/총합:600`")
    if message.content.startswith("!모부기"):
        await message.channel.send("`도감번호 387 모부기 \n종족값 55/68/64/45/55/31/총합:318`")
    if message.content.startswith("!수풀부기"):
        await message.channel.send("`도감번호 388 수풀부기 \n종족값 75/89/85/55/65/36/총합:405`")
    if message.content.startswith("!토대부기"):
        await message.channel.send("`도감번호 389 토대부기 \n종족값 95/109/105/75/85/56/총합:525`")
    if message.content.startswith("!불꽃숭이"):
        await message.channel.send("`도감번호 390 불꽃숭이 \n종족값 44/58/44/58/44/61/총합:309`")
    if message.content.startswith("!파이숭이"):
        await message.channel.send("`도감번호 391 파이숭이 \n종족값 64/78/52/78/52/81/총합:405`")
    if message.content.startswith("!초염몽"):
        await message.channel.send("`도감번호 392 초염몽 \n종족값 76/104/71/104/71/108/총합:534`")
    if message.content.startswith("!팽도리"):
        await message.channel.send("`도감번호 393 팽도리 \n종족값 53/51/53/61/56/40/총합:314`")
    if message.content.startswith("!팽태자"):
        await message.channel.send("`도감번호 394 팽태자 \n종족값 64/66/68/81/76/50/총합:405`")
    if message.content.startswith("!엠페르트"):
        await message.channel.send("`도감번호 395 엠페르트 \n종족값 84/86/88/111/101/60/총합:530`")
    if message.content.startswith("!찌르꼬"):
        await message.channel.send("`도감번호 396 찌르꼬 \n종족값 40/55/30/30/30/60/총합:245`")
    if message.content.startswith("!찌르버드"):
        await message.channel.send("`도감번호 397 찌르버드 \n종족값 55/75/50/40/40/80/총합:340`")
    if message.content.startswith("!찌르호크"):
        await message.channel.send("`도감번호 398 찌르호크 \n종족값 85/120/70/50/60/100/총합:485`")
    if message.content.startswith("!비버니"):
        await message.channel.send("`도감번호 399 비버니 \n종족값 59/45/40/35/40/31/총합:250`")
    if message.content.startswith("!비버통"):
        await message.channel.send("`도감번호 400 비버통 \n종족값 79/85/60/55/60/71/총합:410`")
    if message.content.startswith("!귀뚤뚜기"):
        await message.channel.send("`도감번호 401 귀뚤뚜기 \n종족값 37/25/41/25/41/25/총합:194`")
    if message.content.startswith("!귀뚤톡크"):
        await message.channel.send("`도감번호 402 귀뚤톡크 \n종족값 77/85/51/55/51/65/총합:384`")
    if message.content.startswith("!꼬링크"):
        await message.channel.send("`도감번호 403 꼬링크 \n종족값 45/65/34/40/34/45/총합:263`")
    if message.content.startswith("!럭시오"):
        await message.channel.send("`도감번호 404 럭시오 \n종족값 60/85/49/60/49/60/총합:363`")
    if message.content.startswith("!렌트라"):
        await message.channel.send("`도감번호 405 렌트라 \n종족값 80/120/79/95/79/70/총합:523`")
    if message.content.startswith("!꼬몽울"):
        await message.channel.send("`도감번호 406 꼬몽울 \n종족값 40/30/35/50/70/55/총합:280`")
    if message.content.startswith("!로즈레이드"):
        await message.channel.send("`도감번호 407 로즈레이드 \n종족값 60/70/65/125/105/90/총합:515`")
    if message.content.startswith("!두개도스"):
        await message.channel.send("`도감번호 408 두개도스 \n종족값 67/125/40/30/30/58/총합:350`")
    if message.content.startswith("!램펄드"):
        await message.channel.send("`도감번호 409 램펄드 \n종족값 97/165/60/65/50/58/총합:495`")
    if message.content.startswith("!방패톱스"):
        await message.channel.send("`도감번호 410 방패톱스 \n종족값 30/42/118/42/88/30/총합:350`")
    if message.content.startswith("!바리톱스"):
        await message.channel.send("`도감번호 411 바리톱스 \n종족값 60/52/168/47/138/30/총합:495`")
    if message.content.startswith("!도롱충이"):
        await message.channel.send("`도감번호 412 도롱충이 \n종족값 40/29/45/29/45/36/총합:224`")
    if message.content.startswith("!도롱마담(초목도롱)"):
        await message.channel.send("`도감번호 413 도롱마담(초목도롱) \n종족값 60/59/85/79/105/36/총합:424`")
    if message.content.startswith("!도롱마담(슈레도롱)"):
        await message.channel.send("`도감번호 413 도롱마담(슈레도롱) \n종족값 60/69/95/69/95/36/총합:424`")
    if message.content.startswith("!도롱마담(모래땅도롱)"):
        await message.channel.send("`도감번호 413 도롱마담(모래땅도롱) \n종족값 60/79/105/59/85/36/총합:424`")
    if message.content.startswith("!나메일"):
        await message.channel.send("`도감번호 414 나메일 \n종족값 70/94/50/94/50/66/총합:424`")
    if message.content.startswith("!세꿀버리"):
        await message.channel.send("`도감번호 415 세꿀버리 \n종족값 30/30/42/30/42/70/총합:244`")
    if message.content.startswith("!비퀸"):
        await message.channel.send("`도감번호 416 비퀸 \n종족값 70/80/102/80/102/40/총합:474`")
    if message.content.startswith("!파치리스"):
        await message.channel.send("`도감번호 417 파치리스 \n종족값 60/45/70/45/90/95/총합:405`")
    if message.content.startswith("!브이젤"):
        await message.channel.send("`도감번호 418 브이젤 \n종족값 55/65/35/60/30/85/총합:330`")
    if message.content.startswith("!플로젤"):
        await message.channel.send("`도감번호 419 플로젤 \n종족값 85/105/55/85/50/115/총합:495`")
    if message.content.startswith("!체리버"):
        await message.channel.send("`도감번호 420 체리버 \n종족값 45/35/45/62/53/35/총합:275`")
    if message.content.startswith("!체리꼬"):
        await message.channel.send("`도감번호 421 체리꼬 \n종족값 70/60/70/87/78/85/총합:450`")
    if message.content.startswith("!깝질무"):
        await message.channel.send("`도감번호 422 깝질무 \n종족값 76/48/48/57/62/34/총합:325`")
    if message.content.startswith("!트리토돈"):
        await message.channel.send("`도감번호 423 트리토돈 \n종족값 111/83/68/92/82/39/총합:475`")
    if message.content.startswith("!겟핸보숭"):
        await message.channel.send("`도감번호 424 겟핸보숭 \n종족값 75/100/66/60/66/115/총합:482`")
    if message.content.startswith("!흔들풍손"):
        await message.channel.send("`도감번호 425 흔들풍손 \n종족값 90/50/34/60/44/70/총합:348`")
    if message.content.startswith("!둥실라이드"):
        await message.channel.send("`도감번호 426 둥실라이드 \n종족값 150/80/44/90/54/80/총합:498`")
    if message.content.startswith("!이어롤"):
        await message.channel.send("`도감번호 427 이어롤 \n종족값 55/66/44/44/56/85/총합:350`")
    if message.content.startswith("!이어롭"):
        await message.channel.send("`도감번호 428 이어롭 \n종족값 65/76/84/54/96/105/총합:480`")
    if message.content.startswith("!메가이어롭"):
        await message.channel.send("`도감번호 428 메가이어롭 \n종족값 65/136/94/54/96/135/총합:580`")
    if message.content.startswith("!무우마직"):
        await message.channel.send("`도감번호 429 무우마직 \n종족값 60/60/60/105/105/105/총합:495`")
    if message.content.startswith("!돈크로우"):
        await message.channel.send("`도감번호 430 돈크로우 \n종족값 100/125/52/105/52/71/총합:505`")
    if message.content.startswith("!나옹마"):
        await message.channel.send("`도감번호 431 나옹마 \n종족값 49/55/42/42/37/85/총합:310`")
    if message.content.startswith("!몬냥이"):
        await message.channel.send("`도감번호 432 몬냥이 \n종족값 71/82/64/64/59/112/총합:452`")
    if message.content.startswith("!랑딸랑"):
        await message.channel.send("`도감번호 433 랑딸랑 \n종족값 45/30/50/65/50/45/총합:285`")
    if message.content.startswith("!스컹뿡"):
        await message.channel.send("`도감번호 434 스컹뿡 \n종족값 63/63/47/41/41/74/총합:329`")
    if message.content.startswith("!스컹탱크"):
        await message.channel.send("`도감번호 435 스컹탱크 \n종족값 103/93/67/71/61/84/총합:479`")
    if message.content.startswith("!동미러"):
        await message.channel.send("`도감번호 436 동미러 \n종족값 57/24/86/24/86/23/총합:300`")
    if message.content.startswith("!동탁군"):
        await message.channel.send("`도감번호 437 동탁군 \n종족값 67/89/116/79/116/33/총합:500`")
    if message.content.startswith("!꼬지지"):
        await message.channel.send("`도감번호 438 꼬지지 \n종족값 50/80/95/10/45/10/총합:290`")
    if message.content.startswith("!흉내내"):
        await message.channel.send("`도감번호 439 흉내내 \n종족값 20/25/45/70/90/60/총합:310`")
    if message.content.startswith("!핑복"):
        await message.channel.send("`도감번호 440 핑복 \n종족값 100/5/5/15/65/30/총합:220`")
    if message.content.startswith("!페라페"):
        await message.channel.send("`도감번호 441 페라페 \n종족값 76/65/45/92/42/91/총합:411`")
    if message.content.startswith("!화강돌"):
        await message.channel.send("`도감번호 442 화강돌 \n종족값 50/92/108/92/108/35/총합:485`")
    if message.content.startswith("!딥상어동"):
        await message.channel.send("`도감번호 443 딥상어동 \n종족값 58/70/45/40/45/42/총합:300`")
    if message.content.startswith("!한바이트"):
        await message.channel.send("`도감번호 444 한바이트 \n종족값 68/90/65/50/55/82/총합:410`")
    if message.content.startswith("!한카리아스"):
        await message.channel.send("`도감번호 445 한카리아스 \n종족값 108/130/95/80/85/102/총합:600`")
    if message.content.startswith("!메가한카리아스"):
        await message.channel.send("`도감번호 445 메가한카리아스 \n종족값 108/170/115/120/95/92/총합:700`")
    if message.content.startswith("!먹고자"):
        await message.channel.send("`도감번호 446 먹고자 \n종족값 135/85/40/40/85/5/총합:390`")
    if message.content.startswith("!리오르"):
        await message.channel.send("`도감번호 447 리오르 \n종족값 40/70/40/35/40/60/총합:285`")
    if message.content.startswith("!루카리오"):
        await message.channel.send("`도감번호 448 루카리오 \n종족값 70/110/70/115/70/90/총합:525`")
    if message.content.startswith("!메가루카리오"):
        await message.channel.send("`도감번호 448 메가루카리오 \n종족값 70/145/88/140/70/112/총합:625`")
    if message.content.startswith("!히포포타스"):
        await message.channel.send("`도감번호 449 히포포타스 \n종족값 68/72/78/38/42/32/총합:330`")
    if message.content.startswith("!하마돈"):
        await message.channel.send("`도감번호 450 하마돈 \n종족값 108/112/118/68/72/47/총합:525`")
    if message.content.startswith("!스콜피"):
        await message.channel.send("`도감번호 451 스콜피 \n종족값 40/50/90/30/55/65/총합:330`")
    if message.content.startswith("!드래피온"):
        await message.channel.send("`도감번호 452 드래피온 \n종족값 70/90/110/60/75/95/총합:500`")
    if message.content.startswith("!삐딱구리"):
        await message.channel.send("`도감번호 453 삐딱구리 \n종족값 48/61/40/61/40/50/총합:300`")
    if message.content.startswith("!독개굴"):
        await message.channel.send("`도감번호 454 독개굴 \n종족값 83/106/65/86/65/85/총합:490`")
    if message.content.startswith("!무스틈니"):
        await message.channel.send("`도감번호 455 무스틈니 \n종족값 74/100/72/90/72/46/총합:454`")
    if message.content.startswith("!형광어"):
        await message.channel.send("`도감번호 456 형광어 \n종족값 49/49/56/49/61/66/총합:330`")
    if message.content.startswith("!네오라이트"):
        await message.channel.send("`도감번호 457 네오라이트 \n종족값 69/69/76/69/86/91/총합:460`")
    if message.content.startswith("!타만타"):
        await message.channel.send("`도감번호 458 타만타 \n종족값 45/20/50/60/120/50/총합:345`")
    if message.content.startswith("!눈쓰개"):
        await message.channel.send("`도감번호 459 눈쓰개 \n종족값 60/62/50/62/60/40/총합:334`")
    if message.content.startswith("!눈설왕"):
        await message.channel.send("`도감번호 460 눈설왕 \n종족값 90/92/75/92/85/60/총합:494`")
    if message.content.startswith("!메가눈설왕"):
        await message.channel.send("`도감번호 460 메가눈설왕 \n종족값 90/132/105/132/105/30/총합:594`")
    if message.content.startswith("!포푸니라"):
        await message.channel.send("`도감번호 461 포푸니라 \n종족값 70/120/65/45/85/125/총합:510`")
    if message.content.startswith("!자포코일"):
        await message.channel.send("`도감번호 462 자포코일 \n종족값 70/70/115/130/90/60/총합:535`")
    if message.content.startswith("!내룸벨트"):
        await message.channel.send("`도감번호 463 내룸벨트 \n종족값 110/85/95/80/95/50/총합:515`")
    if message.content.startswith("!거대코뿌리"):
        await message.channel.send("`도감번호 464 거대코뿌리 \n종족값 115/140/130/55/55/40/총합:535`")
    if message.content.startswith("!덩쿠림보"):
        await message.channel.send("`도감번호 465 덩쿠림보 \n종족값 100/100/125/110/50/50/총합:535`")
    if message.content.startswith("!에레키블"):
        await message.channel.send("`도감번호 466 에레키블 \n종족값 75/123/67/95/85/95/총합:540`")
    if message.content.startswith("!마그마번"):
        await message.channel.send("`도감번호 467 마그마번 \n종족값 75/95/67/125/95/83/총합:540`")
    if message.content.startswith("!토게키스"):
        await message.channel.send("`도감번호 468 토게키스 \n종족값 85/50/95/120/115/80/총합:545`")
    if message.content.startswith("!메가자리"):
        await message.channel.send("`도감번호 469 메가자리 \n종족값 86/76/86/116/56/95/총합:515`")
    if message.content.startswith("!리피아"):
        await message.channel.send("`도감번호 470 리피아 \n종족값 65/110/130/60/65/95/총합:525`")
    if message.content.startswith("!글레이시아"):
        await message.channel.send("`도감번호 471 글레이시아 \n종족값 65/60/110/130/95/65/총합:525`")
    if message.content.startswith("!글라이온"):
        await message.channel.send("`도감번호 472 글라이온 \n종족값 75/95/125/45/75/95/총합:510`")
    if message.content.startswith("!맘모꾸리"):
        await message.channel.send("`도감번호 473 맘모꾸리 \n종족값 110/130/80/70/60/80/총합:530`")
    if message.content.startswith("!폴리곤Z"):
        await message.channel.send("`도감번호 474 폴리곤Z \n종족값 85/80/70/135/75/90/총합:535`")
    if message.content.startswith("!엘레이드"):
        await message.channel.send("`도감번호 475 엘레이드 \n종족값 68/125/65/65/115/80/총합:518`")
    if message.content.startswith("!메가엘레이드"):
        await message.channel.send("`도감번호 475 메가엘레이드 \n종족값 68/165/95/65/115/110/총합:618`")
    if message.content.startswith("!대코파스"):
        await message.channel.send("`도감번호 476 대코파스 \n종족값 60/55/145/75/150/40/총합:525`")
    if message.content.startswith("!야느와르몽"):
        await message.channel.send("`도감번호 477 야느와르몽 \n종족값 45/100/135/65/135/45/총합:525`")
    if message.content.startswith("!눈여아"):
        await message.channel.send("`도감번호 478 눈여아 \n종족값 70/80/70/80/70/110/총합:480`")
    if message.content.startswith("!로토무(노말 로토무)"):
        await message.channel.send("`도감번호 479 로토무(노말 로토무) \n종족값 50/50/77/95/77/91/총합:440`")
    if message.content.startswith("!로토무(폼체인지 로토무)"):
        await message.channel.send("`도감번호 479 로토무(폼체인지 로토무) \n종족값 50/65/107/105/107/86/총합:520`")
    if message.content.startswith("!유크시"):
        await message.channel.send("`도감번호 480 유크시 \n종족값 75/75/130/75/130/95/총합:580`")
    if message.content.startswith("!엠라이트"):
        await message.channel.send("`도감번호 481 엠라이트 \n종족값 80/105/105/105/105/80/총합:580`")
    if message.content.startswith("!아그놈"):
        await message.channel.send("`도감번호 482 아그놈 \n종족값 75/125/70/125/70/115/총합:580`")
    if message.content.startswith("!디아루가"):
        await message.channel.send("`도감번호 483 디아루가 \n종족값 100/120/120/150/100/90/총합:680`")
    if message.content.startswith("!펄기아"):
        await message.channel.send("`도감번호 484 펄기아 \n종족값 90/120/100/150/120/100/총합:680`")
    if message.content.startswith("!히드런"):
        await message.channel.send("`도감번호 485 히드런 \n종족값 91/90/106/130/106/77/총합:600`")
    if message.content.startswith("!레지기가스"):
        await message.channel.send("`도감번호 486 레지기가스 \n종족값 110/160/110/80/110/100/총합:670`")
    if message.content.startswith("!기라티나(어나더폼)"):
        await message.channel.send("`도감번호 487 기라티나(어나더폼) \n종족값 150/100/120/100/120/90/총합:680`")
    if message.content.startswith("!기라티나(오리진폼)"):
        await message.channel.send("`도감번호 487 기라티나(오리진폼) \n종족값 150/120/100/120/100/90/총합:680`")
    if message.content.startswith("!크레세리아"):
        await message.channel.send("`도감번호 488 크레세리아 \n종족값 120/70/120/75/130/85/총합:600`")
    if message.content.startswith("!피오네"):
        await message.channel.send("`도감번호 489 피오네 \n종족값 80/80/80/80/80/80/총합:480`")
    if message.content.startswith("!마나피"):
        await message.channel.send("`도감번호 490 마나피 \n종족값 100/100/100/100/100/100/총합:600`")
    if message.content.startswith("!다크라이"):
        await message.channel.send("`도감번호 491 다크라이 \n종족값 70/90/90/135/90/125/총합:600`")
    if message.content.startswith("!쉐이미(랜드폼)"):
        await message.channel.send("`도감번호 492 쉐이미(랜드폼) \n종족값 100/100/100/100/100/100/총합:600`")
    if message.content.startswith("!쉐이미(스카이폼)"):
        await message.channel.send("`도감번호 492 쉐이미(스카이폼) \n종족값 100/103/75/120/75/127/총합:600`")
    if message.content.startswith("!아르세우스"):
        await message.channel.send("`도감번호 493 아르세우스 \n종족값 120/120/120/120/120/120/총합:720`")
    if message.content.startswith("!비크티니"):
        await message.channel.send("`도감번호 494 비크티니 \n종족값 100/100/100/100/100/100/총합:600`")
    if message.content.startswith("!주리비얀"):
        await message.channel.send("`도감번호 495 주리비얀 \n종족값 45/45/55/45/55/63/총합:308`")
    if message.content.startswith("!샤비"):
        await message.channel.send("`도감번호 496 샤비 \n종족값 60/60/75/60/75/83/총합:413`")
    if message.content.startswith("!샤로다"):
        await message.channel.send("`도감번호 497 샤로다 \n종족값 75/75/95/75/95/113/총합:528`")
    if message.content.startswith("!뚜꾸리"):
        await message.channel.send("`도감번호 498 뚜꾸리 \n종족값 65/63/45/45/45/45/총합:308`")
    if message.content.startswith("!차오꿀"):
        await message.channel.send("`도감번호 499 차오꿀 \n종족값 90/93/55/70/55/55/총합:418`")
    if message.content.startswith("!염무왕"):
        await message.channel.send("`도감번호 500 염무왕 \n종족값 110/123/65/100/65/65/총합:528`")
    if message.content.startswith("!수댕이"):
        await message.channel.send("`도감번호 501 수댕이 \n종족값 55/55/45/63/45/45/총합:308`")
    if message.content.startswith("!쌍검자비"):
        await message.channel.send("`도감번호 502 쌍검자비 \n종족값 75/75/60/83/60/60/총합:413`")
    if message.content.startswith("!대검귀"):
        await message.channel.send("`도감번호 503 대검귀 \n종족값 95/100/85/108/70/70/총합:528`")
    if message.content.startswith("!보르쥐"):
        await message.channel.send("`도감번호 504 보르쥐 \n종족값 45/55/39/35/39/42/총합:255`")
    if message.content.startswith("!보르그"):
        await message.channel.send("`도감번호 505 보르그 \n종족값 60/85/69/60/69/77/총합:420`")
    if message.content.startswith("!요테리"):
        await message.channel.send("`도감번호 506 요테리 \n종족값 45/60/45/25/45/55/총합:275`")
    if message.content.startswith("!하데리어"):
        await message.channel.send("`도감번호 507 하데리어 \n종족값 65/80/65/35/65/60/총합:370`")
    if message.content.startswith("!바랜드"):
        await message.channel.send("`도감번호 508 바랜드 \n종족값 85/110/90/45/90/80/총합:500`")
    if message.content.startswith("!쌔비냥"):
        await message.channel.send("`도감번호 509 쌔비냥 \n종족값 41/50/37/50/37/66/총합:281`")
    if message.content.startswith("!레파르다스"):
        await message.channel.send("`도감번호 510 레파르다스 \n종족값 64/88/50/88/50/106/총합:446`")
    if message.content.startswith("!야나프"):
        await message.channel.send("`도감번호 511 야나프 \n종족값 50/53/48/53/48/64/총합:316`")
    if message.content.startswith("!야나키"):
        await message.channel.send("`도감번호 512 야나키 \n종족값 75/98/63/98/63/101/총합:498`")
    if message.content.startswith("!바오프"):
        await message.channel.send("`도감번호 513 바오프 \n종족값 50/53/48/53/48/64/총합:316`")
    if message.content.startswith("!바오키"):
        await message.channel.send("`도감번호 514 바오키 \n종족값 75/98/63/98/63/101/총합:498`")
    if message.content.startswith("!앗차프"):
        await message.channel.send("`도감번호 515 앗차프 \n종족값 50/53/48/53/48/64/총합:316`")
    if message.content.startswith("!앗차키"):
        await message.channel.send("`도감번호 516 앗차키 \n종족값 75/98/63/98/63/101/총합:498`")
    if message.content.startswith("!몽나"):
        await message.channel.send("`도감번호 517 몽나 \n종족값 76/25/45/67/55/24/총합:292`")
    if message.content.startswith("!몽얌나"):
        await message.channel.send("`도감번호 518 몽얌나 \n종족값 116/55/85/107/95/29/총합:487`")
    if message.content.startswith("!콩둘기"):
        await message.channel.send("`도감번호 519 콩둘기 \n종족값 50/55/50/36/30/43/총합:264`")
    if message.content.startswith("!유토브"):
        await message.channel.send("`도감번호 520 유토브 \n종족값 62/77/62/50/42/65/총합:358`")
    if message.content.startswith("!켄호로우"):
        await message.channel.send("`도감번호 521 켄호로우 \n종족값 80/115/80/65/55/93/총합:488`")
    if message.content.startswith("!줄뮤마"):
        await message.channel.send("`도감번호 522 줄뮤마 \n종족값 45/60/32/50/32/76/총합:295`")
    if message.content.startswith("!제브라이카"):
        await message.channel.send("`도감번호 523 제브라이카 \n종족값 75/100/63/80/63/116/총합:497`")
    if message.content.startswith("!단굴"):
        await message.channel.send("`도감번호 524 단굴 \n종족값 55/75/85/25/25/15/총합:280`")
    if message.content.startswith("!암트르"):
        await message.channel.send("`도감번호 525 암트르 \n종족값 70/105/105/50/40/20/총합:390`")
    if message.content.startswith("!기가이어스"):
        await message.channel.send("`도감번호 526 기가이어스 \n종족값 85/135/130/60/80/25/총합:515`")
    if message.content.startswith("!또르박쥐"):
        await message.channel.send("`도감번호 527 또르박쥐 \n종족값 55/45/43/55/43/72/총합:313`")
    if message.content.startswith("!맘박쥐"):
        await message.channel.send("`도감번호 528 맘박쥐 \n종족값 67/57/55/77/55/114/총합:425`")
    if message.content.startswith("!두더류"):
        await message.channel.send("`도감번호 529 두더류 \n종족값 60/85/40/30/45/68/총합:328`")
    if message.content.startswith("!몰드류"):
        await message.channel.send("`도감번호 530 몰드류 \n종족값 110/135/60/50/65/88/총합:508`")
    if message.content.startswith("!다부니"):
        await message.channel.send("`도감번호 531 다부니 \n종족값 103/60/86/60/86/50/총합:445`")
    if message.content.startswith("!메가다부니"):
        await message.channel.send("`도감번호 531 메가다부니 \n종족값 103/60/126/80/126/50/총합:545`")
    if message.content.startswith("!으랏차"):
        await message.channel.send("`도감번호 532 으랏차 \n종족값 75/80/55/25/35/35/총합:305`")
    if message.content.startswith("!토쇠골"):
        await message.channel.send("`도감번호 533 토쇠골 \n종족값 85/105/85/40/50/40/총합:405`")
    if message.content.startswith("!노보청"):
        await message.channel.send("`도감번호 534 노보청 \n종족값 105/140/95/55/65/45/총합:505`")
    if message.content.startswith("!동챙이"):
        await message.channel.send("`도감번호 535 동챙이 \n종족값 50/50/40/50/40/64/총합:294`")
    if message.content.startswith("!두까비"):
        await message.channel.send("`도감번호 536 두까비 \n종족값 75/65/55/65/55/69/총합:384`")
    if message.content.startswith("!두빅굴"):
        await message.channel.send("`도감번호 537 두빅굴 \n종족값 105/95/75/85/75/74/총합:509`")
    if message.content.startswith("!던지미"):
        await message.channel.send("`도감번호 538 던지미 \n종족값 120/100/85/30/85/45/총합:465`")
    if message.content.startswith("!타격귀"):
        await message.channel.send("`도감번호 539 타격귀 \n종족값 75/125/75/30/75/85/총합:465`")
    if message.content.startswith("!두르보"):
        await message.channel.send("`도감번호 540 두르보 \n종족값 45/53/70/40/60/42/총합:310`")
    if message.content.startswith("!두르쿤"):
        await message.channel.send("`도감번호 541 두르쿤 \n종족값 55/63/90/50/80/42/총합:380`")
    if message.content.startswith("!모아머"):
        await message.channel.send("`도감번호 542 모아머 \n종족값 75/103/80/70/80/92/총합:500`")
    if message.content.startswith("!마디네"):
        await message.channel.send("`도감번호 543 마디네 \n종족값 30/45/59/30/39/57/총합:260`")
    if message.content.startswith("!휠구"):
        await message.channel.send("`도감번호 544 휠구 \n종족값 40/55/99/40/79/47/총합:360`")
    if message.content.startswith("!펜드라"):
        await message.channel.send("`도감번호 545 펜드라 \n종족값 60/100/89/55/69/112/총합:485`")
    if message.content.startswith("!소미안"):
        await message.channel.send("`도감번호 546 소미안 \n종족값 40/27/60/37/50/66/총합:280`")
    if message.content.startswith("!엘풍"):
        await message.channel.send("`도감번호 547 엘풍 \n종족값 60/67/85/77/75/116/총합:480`")
    if message.content.startswith("!치릴리"):
        await message.channel.send("`도감번호 548 치릴리 \n종족값 45/35/50/70/50/30/총합:280`")
    if message.content.startswith("!드레디어"):
        await message.channel.send("`도감번호 549 드레디어 \n종족값 70/60/75/110/75/90/총합:480`")
    if message.content.startswith("!배쓰나이"):
        await message.channel.send("`도감번호 550 배쓰나이 \n종족값 70/92/65/80/55/98/총합:460`")
    if message.content.startswith("!깜눈크"):
        await message.channel.send("`도감번호 551 깜눈크 \n종족값 50/72/35/35/35/65/총합:292`")
    if message.content.startswith("!악비르"):
        await message.channel.send("`도감번호 552 악비르 \n종족값 60/82/45/45/45/74/총합:351`")
    if message.content.startswith("!악비아르"):
        await message.channel.send("`도감번호 553 악비아르 \n종족값 95/117/80/65/70/92/총합:519`")



client.run("Njc5Njk0OTc4OTUxMjgyNzMy.Xk9qVg.9_Tet-qtf6Bi80deSD2y4NikLsQ")