import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("질문 딱대")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!나몰빼미"):
        await message.channel.send("`도감번호 722 나몰빼미 \n종족값 68/55/55/50/50/42/총합:320`")
    if message.content.startswith("!빼미스로우"):
        await message.channel.send("`도감번호 723 빼미스로우 \n종족값 78/75/75/70/70/52/총합:420`")
    if message.content.startswith("!모크나이퍼"):
        await message.channel.send("`도감번호 724 모크나이퍼 \n종족값 78/107/75/100/100/70/총합:530`")
    if message.content.startswith("!냐오불"):
        await message.channel.send("`도감번호 725 냐오불 \n종족값 45/65/40/60/40/70/총합:320`")
    if message.content.startswith("!냐오히트"):
        await message.channel.send("`도감번호 726 냐오히트 \n종족값 65/85/50/80/50/90/총합:420`")
    if message.content.startswith("!어흥염"):
        await message.channel.send("`도감번호 727 어흥염 \n종족값 95/115/90/80/90/60/총합:530`")
    if message.content.startswith("!누리공"):
        await message.channel.send("`도감번호 728 누리공 \n종족값 50/54/54/66/56/40/총합:320`")
    if message.content.startswith("!키요공"):
        await message.channel.send("`도감번호 729 키요공 \n종족값 60/69/69/91/81/50/총합:420`")
    if message.content.startswith("!누리레느"):
        await message.channel.send("`도감번호 730 누리레느 \n종족값 80/74/74/126/116/60/총합:530`")
    if message.content.startswith("!콕코구리"):
        await message.channel.send("`도감번호 731 콕코구리 \n종족값 35/75/30/30/30/65/총합:265`")
    if message.content.startswith("!크라파"):
        await message.channel.send("`도감번호 732 크라파 \n종족값 55/85/50/40/50/75/총합:355`")
    if message.content.startswith("!왕큰부리"):
        await message.channel.send("`도감번호 733 왕큰부리 \n종족값 80/120/75/75/75/60/총합:485`")
    if message.content.startswith("!영구스"):
        await message.channel.send("`도감번호 734 영구스 \n종족값 48/70/30/30/30/45/총합:253`")
    if message.content.startswith("!형사구스"):
        await message.channel.send("`도감번호 735 형사구스 \n종족값 88/110/60/55/60/45/총합:418`")
    if message.content.startswith("!턱지충이"):
        await message.channel.send("`도감번호 736 턱지충이 \n종족값 47/62/45/55/45/46/총합:300`")
    if message.content.startswith("!전지충이"):
        await message.channel.send("`도감번호 737 전지충이 \n종족값 57/82/95/55/75/36/총합:400`")
    if message.content.startswith("!투구뿌논"):
        await message.channel.send("`도감번호 738 투구뿌논 \n종족값 77/70/90/145/75/43/총합:500`")
    if message.content.startswith("!오기지게"):
        await message.channel.send("`도감번호 739 오기지게 \n종족값 47/82/57/42/47/63/총합:338`")
    if message.content.startswith("!모단단게"):
        await message.channel.send("`도감번호 740 모단단게 \n종족값 97/132/77/62/67/43/총합:478`")
    if message.content.startswith("!춤추새"):
        await message.channel.send("`도감번호 741 춤추새 \n종족값 75/70/70/98/70/93/총합:476`")
    if message.content.startswith("!에블리"):
        await message.channel.send("`도감번호 742 에블리 \n종족값 40/45/40/55/40/84/총합:304`")
    if message.content.startswith("!에리본"):
        await message.channel.send("`도감번호 743 에리본 \n종족값 60/55/60/95/70/124/총합:464`")
    if message.content.startswith("!암멍이"):
        await message.channel.send("`도감번호 744 암멍이 \n종족값 45/65/40/30/40/60/총합:280`")
    if message.content.startswith("!루가루암"):
        await message.channel.send("`도감번호 745 루가루암 \n종족값 75/115/65/55/65/112/총합:487`")
    if message.content.startswith("!약어리(단독의 모습)"):
        await message.channel.send("`도감번호 746 약어리(단독의 모습) \n종족값 45/20/20/25/25/40/총합:175`")
    if message.content.startswith("!약어리(군집의 모습)"):
        await message.channel.send("`도감번호 746 약어리(군집의 모습) \n종족값 45/140/130/140/135/30/총합:620`")
    if message.content.startswith("!시마사리"):
        await message.channel.send("`도감번호 747 시마사리 \n종족값 50/53/62/43/52/45/총합:305`")
    if message.content.startswith("!더시마사리"):
        await message.channel.send("`도감번호 748 더시마사리 \n종족값 50/63/152/53/142/35/총합:495`")
    if message.content.startswith("!머드나기"):
        await message.channel.send("`도감번호 749 머드나기 \n종족값 70/100/70/45/55/45/총합:385`")
    if message.content.startswith("!만마드"):
        await message.channel.send("`도감번호 750 만마드 \n종족값 100/125/100/55/85/35/총합:500`")
    if message.content.startswith("!물거미"):
        await message.channel.send("`도감번호 751 물거미 \n종족값 38/40/52/40/72/27/총합:269`")
    if message.content.startswith("!깨비물거미"):
        await message.channel.send("`도감번호 752 깨비물거미 \n종족값 68/70/92/50/132/42/총합:454`")
    if message.content.startswith("!짜랑랑"):
        await message.channel.send("`도감번호 753 짜랑랑 \n종족값 40/55/35/50/35/35/총합:250`")
    if message.content.startswith("!라란티스"):
        await message.channel.send("`도감번호 754 라란티스 \n종족값 70/105/90/80/90/45/총합:480`")
    if message.content.startswith("!자마슈"):
        await message.channel.send("`도감번호 755 자마슈 \n종족값 40/35/55/65/75/15/총합:285`")
    if message.content.startswith("!마셰이드"):
        await message.channel.send("`도감번호 756 마셰이드 \n종족값 60/45/80/90/100/30/총합:405`")
    if message.content.startswith("!야도뇽"):
        await message.channel.send("`도감번호 757 야도뇽 \n종족값 48/44/40/71/40/77/총합:320`")
    if message.content.startswith("!염뉴트"):
        await message.channel.send("`도감번호 758 염뉴트 \n종족값 68/64/60/111/60/117/총합:480`")
    if message.content.startswith("!포곰곰"):
        await message.channel.send("`도감번호 759 포곰곰 \n종족값 70/75/50/45/50/50/총합:340`")
    if message.content.startswith("!이븐곰"):
        await message.channel.send("`도감번호 760 이븐곰 \n종족값 120/125/80/55/60/60/총합:500`")
    if message.content.startswith("!달콤아"):
        await message.channel.send("`도감번호 761 달콤아 \n종족값 42/30/38/30/38/32/총합:210`")
    if message.content.startswith("!달무리나"):
        await message.channel.send("`도감번호 762 달무리나 \n종족값 52/40/48/40/48/62/총합:290`")
    if message.content.startswith("!달코퀸"):
        await message.channel.send("`도감번호 763 달코퀸 \n종족값 72/120/98/50/98/72/총합:510`")
    if message.content.startswith("!큐아링"):
        await message.channel.send("`도감번호 764 큐아링 \n종족값 51/52/90/82/110/100/총합:485`")
    if message.content.startswith("!하랑우탄"):
        await message.channel.send("`도감번호 765 하랑우탄 \n종족값 90/60/80/90/110/60/총합:490`")
    if message.content.startswith("!내던숭이"):
        await message.channel.send("`도감번호 766 내던숭이 \n종족값 100/120/90/40/60/80/총합:490`")
    if message.content.startswith("!꼬시레"):
        await message.channel.send("`도감번호 767 꼬시레 \n종족값 25/35/40/20/30/80/총합:230`")
    if message.content.startswith("!갑주무사"):
        await message.channel.send("`도감번호 768 갑주무사 \n종족값 75/125/140/60/90/40/총합:530`")
    if message.content.startswith("!모래꿍"):
        await message.channel.send("`도감번호 769 모래꿍 \n종족값 55/55/80/70/45/15/총합:320`")
    if message.content.startswith("!모래성이당"):
        await message.channel.send("`도감번호 770 모래성이당 \n종족값 85/75/110/100/75/35/총합:480`")
    if message.content.startswith("!해무기"):
        await message.channel.send("`도감번호 771 해무기 \n종족값 55/60/130/30/130/5/총합:410`")
    if message.content.startswith("!타입:널")
        await message.channel.send("`도감번호 772 타입:널: \n종족값 95/95/95/95/95/59/총합:534`")
    if message.content.startswith("!실버디"):
        await message.channel.send("`도감번호 773 실버디 \n종족값 95/95/95/95/95/95/총합:570`")
    if message.content.startswith("!메테노"):
        await message.channel.send("`도감번호 774 메테노 \n종족값 60/60/100/60/100/60/총합:440`")
    if message.content.startswith("!자말라"):
        await message.channel.send("`도감번호 775 자말라 \n종족값 65/115/65/75/95/65/총합:480`")
    if message.content.startswith("!폭거북스"):
        await message.channel.send("`도감번호 776 폭거북스 \n종족값 60/78/135/91/85/36/총합:485`")
    if message.content.startswith("!토게데마루"):
        await message.channel.send("`도감번호 777 토게데마루 \n종족값 65/98/63/40/73/96/총합:435`")
    if message.content.startswith("!따라큐"):
        await message.channel.send("`도감번호 778 따라큐 \n종족값 55/90/80/50/105/96/총합:476`")
    if message.content.startswith("!치갈기"):
        await message.channel.send("`도감번호 779 치갈기 \n종족값 68/105/70/70/70/92/총합:475`")
    if message.content.startswith("!할비롱"):
        await message.channel.send("`도감번호 780 할비롱 \n종족값 78/60/85/135/91/36/총합:485`")
    if message.content.startswith("!타타륜"):
        await message.channel.send("`도감번호 781 타타륜 \n종족값 70/131/100/86/90/40/총합:517`")
    if message.content.startswith("!짜랑꼬"):
        await message.channel.send("`도감번호 782 짜랑꼬 \n종족값 45/55/65/45/45/45/총합:300`")
    if message.content.startswith("!짜랑고우"):
        await message.channel.send("`도감번호 783 짜랑고우 \n종족값 55/75/90/65/70/65/총합:420`")
    if message.content.startswith("!짜랑고우거"):
        await message.channel.send("`도감번호 784 짜랑고우거 \n종족값 75/110/125/100/105/85/총합:600`")
    if message.content.startswith("!카푸꼬꼬꼭"):
        await message.channel.send("`도감번호 785 카푸꼬꼬꼭 \n종족값 70/115/85/95/75/130/총합:570`")
    if message.content.startswith("!카푸나비나"):
        await message.channel.send("`도감번호 786 카푸나비나 \n종족값 70/85/75/130/115/95/총합:570`")
    if message.content.startswith("!카푸브루루"):
        await message.channel.send("`도감번호 787 카푸브루루 \n종족값 70/130/115/85/95/75/총합:570`")
    if message.content.startswith("!카푸느지느"):
        await message.channel.send("`도감번호 788 카푸느지느 \n종족값 70/75/115/95/130/85/총합:570`")
    if message.content.startswith("!코스모그"):
        await message.channel.send("`도감번호 789 코스모그 \n종족값 43/29/31/29/31/37/총합:200`")
    if message.content.startswith("!코스모움"):
        await message.channel.send("`도감번호 790 코스모움 \n종족값 43/29/131/29/131/37/총합:400`")
    if message.content.startswith("!솔가레오"):
        await message.channel.send("`도감번호 791 솔가레오 \n종족값 137/137/107/113/89/97/총합:680`")
    if message.content.startswith("!루나아라"):
        await message.channel.send("`도감번호 792 루나아라 \n종족값 137/113/89/137/107/97/총합:680`")
    if message.content.startswith("!텅비드"):
        await message.channel.send("`도감번호 793 텅비드 \n종족값 109/53/47/127/131/103/총합:570`")
    if message.content.startswith("!매시붕"):
        await message.channel.send("`도감번호 794 매시붕 \n종족값 107/139/139/53/53/79/총합:570`")
    if message.content.startswith("!페로코체"):
        await message.channel.send("`도감번호 795 페로코체 \n종족값 71/137/37/137/37/151/총합:570`")
    if message.content.startswith("!전수목"):
        await message.channel.send("`도감번호 796 전수목 \n종족값 83/89/71/173/71/83/총합:570`")
    if message.content.startswith("!철화구야"):
        await message.channel.send("`도감번호 797 철화구야 \n종족값 97/101/103/107/101/61/총합:570`")
    if message.content.startswith("!종이신도"):
        await message.channel.send("`도감번호 798 종이신도 \n종족값 59/181/131/59/31/109/총합:570`")
    if message.content.startswith("!악식킹"):
        await message.channel.send("`도감번호 799 악식킹 \n종족값 223/101/53/97/53/43/총합:570`")
    if message.content.startswith("!네크로즈마"):
        await message.channel.send("`도감번호 800 네크로즈마 \n종족값 97/107/101/127/89/79/총합:600`")
    if message.content.startswith("!마기아나"):
        await message.channel.send("`도감번호 801 마기아나 \n종족값 80/95/115/130/115/65/총합:600`")
    if message.content.startswith("!마샤도"):
        await message.channel.send("`도감번호 802 마샤도 \n종족값 90/125/80/90/90/125/총합:600`")
    if message.content.startswith("!베베놈"):
        await message.channel.send("`도감번호 803 베베놈 \n종족값 67/73/67/73/67/73/총합:420`")
    if message.content.startswith("!아고용"):
        await message.channel.send("`도감번호 804 아고용 \n종족값 73/73/73/127/73/121/총합:540`")
    if message.content.startswith("!차곡차곡"):
        await message.channel.send("`도감번호 805 차곡차곡 \n종족값 61/131/211/53/101/13/총합:570`")
    if message.content.startswith("!두파팡"):
        await message.channel.send("`도감번호 806 두파팡 \n종족값 53/127/53/151/79/107/총합:570`")
    if message.content.startswith("!제라오라"):
        await message.channel.send("`도감번호 807 제라오라 \n종족값 88/112/75/102/80/143/총합:600`")
    if message.content.startswith("!멜탄"):
        await message.channel.send("`도감번호 808 멜탄 \n종족값 46/65/65/55/35/34/총합:300`")
    if message.content.startswith("!멜메탈"):
        await message.channel.send("`도감번호 809 멜메탈 \n종족값 135/143/143/80/65/34/총합:600`")

client.run("Njc5OTMyOTU0OTM5NzUyNDQ4.Xk4jAA.qmvFoZ-hc9peFsr09fm0GDMz1SM")
