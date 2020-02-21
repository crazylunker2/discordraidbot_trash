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
    if message.content.startswith("!달막화"):
        await message.channel.send("`도감번호 554 달막화 \n종족값 70/90/45/15/45/50/총합:315`")
    if message.content.startswith("!달막화(가라르의 모습)"):
        await message.channel.send("`도감번호 554 달막화(가라르의 모습) \n종족값 70/90/45/15/45/50/총합:315`")
    if message.content.startswith("!불비달마(노말모드)"):
        await message.channel.send("`도감번호 555 불비달마(노말모드) \n종족값 105/140/55/30/55/95/총합:480`")
    if message.content.startswith("!불비달마(달마모드)"):
        await message.channel.send("`도감번호 555 불비달마(달마모드) \n종족값 105/30/105/140/105/55/총합:540`")
    if message.content.startswith("!불비달마(가라르의 모습)"):
        await message.channel.send("`도감번호 555 불비달마(가라르의 모습) \n종족값 105/140/55/30/55/95/총합:480`")
    if message.content.startswith("!불비달마(가라르의 모습 달마모드)"):
        await message.channel.send("`도감번호 555 불비달마(가라르의 모습 달마모드) \n종족값 105/160/55/30/55/135/총합:540`")
    if message.content.startswith("!마라카치"):
        await message.channel.send("`도감번호 556 마라카치 \n종족값 75/86/67/106/67/60/총합:461`")
    if message.content.startswith("!돌살이"):
        await message.channel.send("`도감번호 557 돌살이 \n종족값 50/65/85/35/35/55/총합:325`")
    if message.content.startswith("!암팰리스"):
        await message.channel.send("`도감번호 558 암팰리스 \n종족값 70/95/125/65/75/45/총합:475`")
    if message.content.startswith("!곤율랭"):
        await message.channel.send("`도감번호 559 곤율랭 \n종족값 50/75/70/35/70/48/총합:348`")
    if message.content.startswith("!곤율거니"):
        await message.channel.send("`도감번호 560 곤율거니 \n종족값 65/90/115/45/115/58/총합:488`")
    if message.content.startswith("!심보러"):
        await message.channel.send("`도감번호 561 심보러 \n종족값 72/58/80/103/80/97/총합:490`")
    if message.content.startswith("!데스마스"):
        await message.channel.send("`도감번호 562 데스마스 \n종족값 38/30/85/55/65/30/총합:303`")
    if message.content.startswith("!데스마스(가라르의 모습)"):
        await message.channel.send("`도감번호 562 데스마스(가라르의 모습) \n종족값 38/55/85/30/65/30/총합:303`")
    if message.content.startswith("!데스니칸"):
        await message.channel.send("`도감번호 563 데스니칸 \n종족값 58/50/145/95/105/30/총합:483`")
    if message.content.startswith("!프로토가"):
        await message.channel.send("`도감번호 564 프로토가 \n종족값 54/78/103/53/45/22/총합:355`")
    if message.content.startswith("!늑골라"):
        await message.channel.send("`도감번호 565 늑골라 \n종족값 74/108/133/83/65/32/총합:495`")
    if message.content.startswith("!아켄"):
        await message.channel.send("`도감번호 566 아켄 \n종족값 55/112/45/74/45/70/총합:401`")
    if message.content.startswith("!아케오스"):
        await message.channel.send("`도감번호 567 아케오스 \n종족값 75/140/65/112/65/110/총합:567`")
    if message.content.startswith("!깨봉이"):
        await message.channel.send("`도감번호 568 깨봉이 \n종족값 50/50/62/40/62/65/총합:329`")
    if message.content.startswith("!더스트나"):
        await message.channel.send("`도감번호 569 더스트나 \n종족값 80/95/82/60/82/75/총합:474`")
    if message.content.startswith("!조로아"):
        await message.channel.send("`도감번호 570 조로아 \n종족값 40/65/40/80/40/65/총합:330`")
    if message.content.startswith("!조로아크"):
        await message.channel.send("`도감번호 571 조로아크 \n종족값 60/105/60/120/60/105/총합:510`")
    if message.content.startswith("!치라미"):
        await message.channel.send("`도감번호 572 치라미 \n종족값 55/50/40/40/40/75/총합:300`")
    if message.content.startswith("!치라치노"):
        await message.channel.send("`도감번호 573 치라치노 \n종족값 75/95/60/65/60/115/총합:470`")
    if message.content.startswith("!고디탱"):
        await message.channel.send("`도감번호 574 고디탱 \n종족값 45/30/50/55/65/45/총합:290`")
    if message.content.startswith("!고디보미"):
        await message.channel.send("`도감번호 575 고디보미 \n종족값 60/45/70/75/85/55/총합:390`")
    if message.content.startswith("!고디모아젤"):
        await message.channel.send("`도감번호 576 고디모아젤 \n종족값 70/55/95/95/110/65/총합:490`")
    if message.content.startswith("!유니란"):
        await message.channel.send("`도감번호 577 유니란 \n종족값 45/30/40/105/50/20/총합:290`")
    if message.content.startswith("!듀란"):
        await message.channel.send("`도감번호 578 듀란 \n종족값 65/40/50/125/60/30/총합:370`")
    if message.content.startswith("!란쿨루스"):
        await message.channel.send("`도감번호 579 란쿨루스 \n종족값 110/65/75/125/85/30/총합:490`")
    if message.content.startswith("!꼬지보리"):
        await message.channel.send("`도감번호 580 꼬지보리 \n종족값 62/44/50/44/50/55/총합:305`")
    if message.content.startswith("!스완나"):
        await message.channel.send("`도감번호 581 스완나 \n종족값 75/87/63/87/63/98/총합:473`")
    if message.content.startswith("!바닐프티"):
        await message.channel.send("`도감번호 582 바닐프티 \n종족값 36/50/50/65/60/44/총합:305`")
    if message.content.startswith("!바닐리치"):
        await message.channel.send("`도감번호 583 바닐리치 \n종족값 51/65/65/80/75/59/총합:395`")
    if message.content.startswith("!배바닐라"):
        await message.channel.send("`도감번호 584 배바닐라 \n종족값 71/95/85/110/95/79/총합:535`")
    if message.content.startswith("!사철록"):
        await message.channel.send("`도감번호 585 사철록 \n종족값 60/60/50/40/50/75/총합:335`")
    if message.content.startswith("!바라철록"):
        await message.channel.send("`도감번호 586 바라철록 \n종족값 80/100/70/60/70/95/총합:475`")
    if message.content.startswith("!에몽가"):
        await message.channel.send("`도감번호 587 에몽가 \n종족값 55/75/60/75/60/103/총합:428`")
    if message.content.startswith("!딱정곤"):
        await message.channel.send("`도감번호 588 딱정곤 \n종족값 50/75/45/40/45/60/총합:315`")
    if message.content.startswith("!슈바르고"):
        await message.channel.send("`도감번호 589 슈바르고 \n종족값 70/135/105/60/105/20/총합:495`")
    if message.content.startswith("!깜놀버슬"):
        await message.channel.send("`도감번호 590 깜놀버슬 \n종족값 69/55/45/55/55/15/총합:294`")
    if message.content.startswith("!뽀록나"):
        await message.channel.send("`도감번호 591 뽀록나 \n종족값 114/85/70/85/80/30/총합:464`")
    if message.content.startswith("!탱그릴"):
        await message.channel.send("`도감번호 592 탱그릴 \n종족값 55/40/50/65/85/40/총합:335`")
    if message.content.startswith("!탱탱겔"):
        await message.channel.send("`도감번호 593 탱탱겔 \n종족값 100/60/70/85/105/60/총합:480`")
    if message.content.startswith("!맘복치"):
        await message.channel.send("`도감번호 594 맘복치 \n종족값 165/75/80/40/45/65/총합:470`")
    if message.content.startswith("!파쪼옥"):
        await message.channel.send("`도감번호 595 파쪼옥 \n종족값 50/47/50/57/50/65/총합:319`")
    if message.content.startswith("!전툴라"):
        await message.channel.send("`도감번호 596 전툴라 \n종족값 70/77/60/97/60/108/총합:472`")
    if message.content.startswith("!철시드"):
        await message.channel.send("`도감번호 597 철시드 \n종족값 44/50/91/24/86/10/총합:305`")
    if message.content.startswith("!너트령"):
        await message.channel.send("`도감번호 598 너트령 \n종족값 74/94/131/54/116/20/총합:489`")
    if message.content.startswith("!기어르"):
        await message.channel.send("`도감번호 599 기어르 \n종족값 40/55/70/45/60/30/총합:300`")
    if message.content.startswith("!기기어르"):
        await message.channel.send("`도감번호 600 기기어르 \n종족값 60/80/95/70/85/50/총합:440`")
    if message.content.startswith("!기기기어르"):
        await message.channel.send("`도감번호 601 기기기어르 \n종족값 60/100/115/70/85/90/총합:520`")
    if message.content.startswith("!저리어"):
        await message.channel.send("`도감번호 602 저리어 \n종족값 35/55/40/45/40/60/총합:275`")
    if message.content.startswith("!저리릴"):
        await message.channel.send("`도감번호 603 저리릴 \n종족값 65/85/70/75/70/40/총합:405`")
    if message.content.startswith("!저리더프"):
        await message.channel.send("`도감번호 604 저리더프 \n종족값 85/115/80/105/80/50/총합:515`")
    if message.content.startswith("!리그레"):
        await message.channel.send("`도감번호 605 리그레 \n종족값 55/55/55/85/55/30/총합:335`")
    if message.content.startswith("!벰크"):
        await message.channel.send("`도감번호 606 벰크 \n종족값 75/75/75/125/95/40/총합:485`")
    if message.content.startswith("!불켜미"):
        await message.channel.send("`도감번호 607 불켜미 \n종족값 50/30/55/65/55/20/총합:275`")
    if message.content.startswith("!램프라"):
        await message.channel.send("`도감번호 608 램프라 \n종족값 60/40/60/95/60/55/총합:370`")
    if message.content.startswith("!샹델라"):
        await message.channel.send("`도감번호 609 샹델라 \n종족값 60/55/90/145/90/80/총합:520`")
    if message.content.startswith("!터검니"):
        await message.channel.send("`도감번호 610 터검니 \n종족값 46/87/60/30/40/57/총합:320`")
    if message.content.startswith("!액슨도"):
        await message.channel.send("`도감번호 611 액슨도 \n종족값 66/117/70/40/50/67/총합:410`")
    if message.content.startswith("!액스라이즈"):
        await message.channel.send("`도감번호 612 액스라이즈 \n종족값 76/147/90/60/70/97/총합:540`")
    if message.content.startswith("!코고미"):
        await message.channel.send("`도감번호 613 코고미 \n종족값 55/70/40/60/40/40/총합:305`")
    if message.content.startswith("!툰베어"):
        await message.channel.send("`도감번호 614 툰베어 \n종족값 95/110/80/70/80/50/총합:485`")
    if message.content.startswith("!프리지오"):
        await message.channel.send("`도감번호 615 프리지오 \n종족값 70/50/30/95/135/105/총합:485`")
    if message.content.startswith("!쪼마리"):
        await message.channel.send("`도감번호 616 쪼마리 \n종족값 50/40/85/40/65/25/총합:305`")
    if message.content.startswith("!어지리더"):
        await message.channel.send("`도감번호 617 어지리더 \n종족값 80/70/40/100/60/145/총합:495`")
    if message.content.startswith("!메더"):
        await message.channel.send("`도감번호 618 메더 \n종족값 109/66/84/81/99/32/총합:471`")
    if message.content.startswith("!메더(가라르의 모습)"):
        await message.channel.send("`도감번호 618 메더(가라르의 모습) \n종족값 109/81/99/66/84/32/총합:471`")
    if message.content.startswith("!비조푸"):
        await message.channel.send("`도감번호 619 비조푸 \n종족값 45/85/50/55/50/65/총합:350`")
    if message.content.startswith("!비조도"):
        await message.channel.send("`도감번호 620 비조도 \n종족값 65/125/60/95/60/105/총합:510`")
    if message.content.startswith("!크리만"):
        await message.channel.send("`도감번호 621 크리만 \n종족값 77/120/90/60/90/48/총합:485`")
    if message.content.startswith("!골비람"):
        await message.channel.send("`도감번호 622 골비람 \n종족값 59/74/50/35/50/35/총합:303`")
    if message.content.startswith("!골루그"):
        await message.channel.send("`도감번호 623 골루그 \n종족값 89/124/80/55/80/55/총합:483`")
    if message.content.startswith("!자망칼"):
        await message.channel.send("`도감번호 624 자망칼 \n종족값 45/85/70/40/40/60/총합:340`")
    if message.content.startswith("!절각참"):
        await message.channel.send("`도감번호 625 절각참 \n종족값 65/125/100/60/70/70/총합:490`")
    if message.content.startswith("!버프론"):
        await message.channel.send("`도감번호 626 버프론 \n종족값 95/110/95/40/95/55/총합:490`")
    if message.content.startswith("!수리둥보"):
        await message.channel.send("`도감번호 627 수리둥보 \n종족값 70/83/50/37/50/60/총합:350`")
    if message.content.startswith("!워글"):
        await message.channel.send("`도감번호 628 워글 \n종족값 100/123/75/57/75/80/총합:510`")
    if message.content.startswith("!벌차이"):
        await message.channel.send("`도감번호 629 벌차이 \n종족값 70/55/75/45/65/60/총합:370`")
    if message.content.startswith("!버랜지나"):
        await message.channel.send("`도감번호 630 버랜지나 \n종족값 110/65/105/55/95/80/총합:510`")
    if message.content.startswith("!앤티골"):
        await message.channel.send("`도감번호 631 앤티골 \n종족값 85/97/66/105/66/65/총합:484`")
    if message.content.startswith("!아이앤트"):
        await message.channel.send("`도감번호 632 아이앤트 \n종족값 58/109/112/48/48/109/총합:484`")
    if message.content.startswith("!모노두"):
        await message.channel.send("`도감번호 633 모노두 \n종족값 52/65/50/45/50/38/총합:300`")
    if message.content.startswith("!디헤드"):
        await message.channel.send("`도감번호 634 디헤드 \n종족값 72/85/70/65/70/58/총합:420`")
    if message.content.startswith("!삼삼드래"):
        await message.channel.send("`도감번호 635 삼삼드래 \n종족값 92/105/90/125/90/98/총합:600`")
    if message.content.startswith("!활화르바"):
        await message.channel.send("`도감번호 636 활화르바 \n종족값 55/85/55/50/55/60/총합:360`")
    if message.content.startswith("!불카모스"):
        await message.channel.send("`도감번호 637 불카모스 \n종족값 85/60/65/135/105/100/총합:550`")
    if message.content.startswith("!코바르온"):
        await message.channel.send("`도감번호 638 코바르온 \n종족값 91/90/129/90/72/108/총합:580`")
    if message.content.startswith("!테라키온"):
        await message.channel.send("`도감번호 639 테라키온 \n종족값 91/129/90/72/90/108/총합:580`")
    if message.content.startswith("!비리디온"):
        await message.channel.send("`도감번호 640 비리디온 \n종족값 91/90/72/90/129/108/총합:580`")
    if message.content.startswith("!토네로스(영물폼)"):
        await message.channel.send("`도감번호 641 토네로스(영물폼) \n종족값 79/100/80/110/90/121/총합:580`")
    if message.content.startswith("!토네로스(화신폼)"):
        await message.channel.send("`도감번호 641 토네로스(화신폼) \n종족값 79/115/70/125/80/111/총합:580`")
    if message.content.startswith("!볼트로스(영물폼)"):
        await message.channel.send("`도감번호 642 볼트로스(영물폼) \n종족값 79/105/70/145/80/101/총합:580`")
    if message.content.startswith("!볼트로스(화신폼)"):
        await message.channel.send("`도감번호 642 볼트로스(화신폼) \n종족값 79/115/70/125/80/111/총합:580`")
    if message.content.startswith("!레시라무"):
        await message.channel.send("`도감번호 643 레시라무 \n종족값 100/120/100/150/120/90/총합:680`")
    if message.content.startswith("!제크로무"):
        await message.channel.send("`도감번호 644 제크로무 \n종족값 100/150/120/120/100/90/총합:680`")
    if message.content.startswith("!랜드로스(화신폼)"):
        await message.channel.send("`도감번호 645 랜드로스(화신폼) \n종족값 89/125/90/115/80/101/총합:600`")
    if message.content.startswith("!랜드로스(영물폼)"):
        await message.channel.send("`도감번호 645 랜드로스(영물폼) \n종족값 89/145/90/105/80/91/총합:600`")
    if message.content.startswith("!큐레무 (화이트)"):
        await message.channel.send("`도감번호 646 큐레무 (화이트) \n종족값 125/120/90/170/100/95/총합:700`")
    if message.content.startswith("!큐레무"):
        await message.channel.send("`도감번호 646 큐레무 \n종족값 125/130/90/130/90/95/총합:660`")
    if message.content.startswith("!큐레무 (블랙)"):
        await message.channel.send("`도감번호 646 큐레무 (블랙) \n종족값 125/170/100/120/90/95/총합:700`")
    if message.content.startswith("!케르디오"):
        await message.channel.send("`도감번호 647 케르디오 \n종족값 91/72/90/129/90/108/총합:580`")
    if message.content.startswith("!메로엣타(스텝폼)"):
        await message.channel.send("`도감번호 648 메로엣타(스텝폼) \n종족값 100/128/90/77/77/128/총합:600`")
    if message.content.startswith("!메로엣타(보이스폼)"):
        await message.channel.send("`도감번호 648 메로엣타(보이스폼) \n종족값 100/77/77/128/128/90/총합:600`")
    if message.content.startswith("!게노세크트"):
        await message.channel.send("`도감번호 649 게노세크트 \n종족값 71/120/95/120/95/99/총합:600`")
    if message.content.startswith("!도치마론"):
        await message.channel.send("`도감번호 650 도치마론 \n종족값 56/61/65/48/45/38/총합:313`")
    if message.content.startswith("!도치보구"):
        await message.channel.send("`도감번호 651 도치보구 \n종족값 61/78/95/56/58/57/총합:405`")
    if message.content.startswith("!브리가론"):
        await message.channel.send("`도감번호 652 브리가론 \n종족값 90/100/120/80/70/70/총합:530`")
    if message.content.startswith("!푸호꼬"):
        await message.channel.send("`도감번호 653 푸호꼬 \n종족값 40/45/40/62/60/60/총합:307`")
    if message.content.startswith("!테르나"):
        await message.channel.send("`도감번호 654 테르나 \n종족값 59/59/58/90/70/73/총합:409`")
    if message.content.startswith("!마폭시"):
        await message.channel.send("`도감번호 655 마폭시 \n종족값 75/69/72/114/100/104/총합:534`")
    if message.content.startswith("!개구마르"):
        await message.channel.send("`도감번호 656 개구마르 \n종족값 41/56/40/62/44/71/총합:314`")
    if message.content.startswith("!개굴반장"):
        await message.channel.send("`도감번호 657 개굴반장 \n종족값 54/63/52/83/56/97/총합:405`")
    if message.content.startswith("!개굴닌자"):
        await message.channel.send("`도감번호 658 개굴닌자 \n종족값 72/95/67/103/71/122/총합:530`")
    if message.content.startswith("!파르빗"):
        await message.channel.send("`도감번호 659 파르빗 \n종족값 38/36/38/32/36/57/총합:237`")
    if message.content.startswith("!파르토"):
        await message.channel.send("`도감번호 660 파르토 \n종족값 85/56/77/50/77/78/총합:423`")
    if message.content.startswith("!화살꼬빈"):
        await message.channel.send("`도감번호 661 화살꼬빈 \n종족값 45/50/43/40/38/62/총합:278`")
    if message.content.startswith("!불화살빈"):
        await message.channel.send("`도감번호 662 불화살빈 \n종족값 62/73/55/56/52/84/총합:382`")
    if message.content.startswith("!파이어로"):
        await message.channel.send("`도감번호 663 파이어로 \n종족값 78/81/71/74/69/126/총합:499`")
    if message.content.startswith("!분이벌레"):
        await message.channel.send("`도감번호 664 분이벌레 \n종족값 38/35/40/27/25/35/총합:200`")
    if message.content.startswith("!분떠도리"):
        await message.channel.send("`도감번호 665 분떠도리 \n종족값 45/22/60/27/30/29/총합:213`")
    if message.content.startswith("!비비용"):
        await message.channel.send("`도감번호 666 비비용 \n종족값 80/52/50/90/50/89/총합:411`")
    if message.content.startswith("!레오꼬"):
        await message.channel.send("`도감번호 667 레오꼬 \n종족값 62/50/58/73/54/72/총합:369`")
    if message.content.startswith("!화염레오"):
        await message.channel.send("`도감번호 668 화염레오 \n종족값 86/68/72/109/66/106/총합:507`")
    if message.content.startswith("!플라베베"):
        await message.channel.send("`도감번호 669 플라베베 \n종족값 44/38/39/61/79/42/총합:303`")
    if message.content.startswith("!플라엣테"):
        await message.channel.send("`도감번호 670 플라엣테 \n종족값 54/45/47/75/98/52/총합:371`")
    if message.content.startswith("!플라제스"):
        await message.channel.send("`도감번호 671 플라제스 \n종족값 78/65/68/112/154/75/총합:552`")
    if message.content.startswith("!메이클"):
        await message.channel.send("`도감번호 672 메이클 \n종족값 66/65/48/62/57/52/총합:350`")
    if message.content.startswith("!고고트"):
        await message.channel.send("`도감번호 673 고고트 \n종족값 123/100/62/97/81/68/총합:531`")
    if message.content.startswith("!판짱"):
        await message.channel.send("`도감번호 674 판짱 \n종족값 67/82/62/46/48/53/총합:358`")
    if message.content.startswith("!부란다"):
        await message.channel.send("`도감번호 675 부란다 \n종족값 95/124/78/69/71/58/총합:495`")
    if message.content.startswith("!트리미앙"):
        await message.channel.send("`도감번호 676 트리미앙 \n종족값 75/80/60/65/90/102/총합:472`")
    if message.content.startswith("!냐스퍼"):
        await message.channel.send("`도감번호 677 냐스퍼 \n종족값 62/48/54/63/60/68/총합:355`")
    if message.content.startswith("!냐오닉스"):
        await message.channel.send("`도감번호 678 냐오닉스 \n종족값 74/48/76/83/81/104/총합:466`")
    if message.content.startswith("!단칼빙"):
        await message.channel.send("`도감번호 679 단칼빙 \n종족값 45/80/100/35/37/28/총합:325`")
    if message.content.startswith("!쌍검킬"):
        await message.channel.send("`도감번호 680 쌍검킬 \n종족값 59/110/150/45/49/35/총합:448`")
    if message.content.startswith("!킬가르도(블레이드폼)"):
        await message.channel.send("`도감번호 681 킬가르도(블레이드폼) \n종족값 60/150/50/150/50/60/총합:520`")
    if message.content.startswith("!킬가르도(실드폼)"):
        await message.channel.send("`도감번호 681 킬가르도(실드폼) \n종족값 60/50/150/50/150/60/총합:520`")
    if message.content.startswith("!슈쁘"):
        await message.channel.send("`도감번호 682 슈쁘 \n종족값 78/52/60/63/65/23/총합:341`")
    if message.content.startswith("!프레프티르"):
        await message.channel.send("`도감번호 683 프레프티르 \n종족값 101/72/72/99/89/29/총합:462`")
    if message.content.startswith("!나룸퍼프"):
        await message.channel.send("`도감번호 684 나룸퍼프 \n종족값 62/48/66/59/57/49/총합:341`")
    if message.content.startswith("!나루림"):
        await message.channel.send("`도감번호 685 나루림 \n종족값 82/80/86/85/75/72/총합:480`")
    if message.content.startswith("!오케이징"):
        await message.channel.send("`도감번호 686 오케이징 \n종족값 53/54/53/37/46/45/총합:288`")
    if message.content.startswith("!칼라마네로"):
        await message.channel.send("`도감번호 687 칼라마네로 \n종족값 86/92/88/68/75/73/총합:482`")
    if message.content.startswith("!거북손손"):
        await message.channel.send("`도감번호 688 거북손손 \n종족값 42/52/67/39/56/50/총합:306`")
    if message.content.startswith("!거북손데스"):
        await message.channel.send("`도감번호 689 거북손데스 \n종족값 72/92/115/54/86/68/총합:487`")
    if message.content.startswith("!수레기"):
        await message.channel.send("`도감번호 690 수레기 \n종족값 50/60/60/60/60/30/총합:320`")
    if message.content.startswith("!드래캄"):
        await message.channel.send("`도감번호 691 드래캄 \n종족값 65/75/90/97/123/44/총합:494`")
    if message.content.startswith("!완철포"):
        await message.channel.send("`도감번호 692 완철포 \n종족값 50/53/62/58/63/44/총합:330`")
    if message.content.startswith("!블로스터"):
        await message.channel.send("`도감번호 693 블로스터 \n종족값 71/73/88/120/89/59/총합:500`")
    if message.content.startswith("!목도리키텔"):
        await message.channel.send("`도감번호 694 목도리키텔 \n종족값 44/38/33/61/43/70/총합:289`")
    if message.content.startswith("!일레도리자드"):
        await message.channel.send("`도감번호 695 일레도리자드 \n종족값 62/55/52/109/94/109/총합:481`")
    if message.content.startswith("!티고라스"):
        await message.channel.send("`도감번호 696 티고라스 \n종족값 58/89/77/45/45/48/총합:362`")
    if message.content.startswith("!견고라스"):
        await message.channel.send("`도감번호 697 견고라스 \n종족값 82/121/119/69/59/71/총합:521`")
    if message.content.startswith("!아마루스"):
        await message.channel.send("`도감번호 698 아마루스 \n종족값 77/59/50/67/63/46/총합:362`")
    if message.content.startswith("!아마루르가"):
        await message.channel.send("`도감번호 699 아마루르가 \n종족값 123/77/72/99/92/58/총합:521`")
    if message.content.startswith("!님피아"):
        await message.channel.send("`도감번호 700 님피아 \n종족값 95/65/65/110/130/60/총합:525`")
    if message.content.startswith("!루차불"):
        await message.channel.send("`도감번호 701 루차불 \n종족값 78/92/75/74/63/118/총합:500`")
    if message.content.startswith("!데덴네"):
        await message.channel.send("`도감번호 702 데덴네 \n종족값 67/58/57/81/67/101/총합:431`")
    if message.content.startswith("!멜리시"):
        await message.channel.send("`도감번호 703 멜리시 \n종족값 50/50/150/50/150/50/총합:500`")
    if message.content.startswith("!미끄메라"):
        await message.channel.send("`도감번호 704 미끄메라 \n종족값 45/50/35/55/75/40/총합:300`")
    if message.content.startswith("!미끄네일"):
        await message.channel.send("`도감번호 705 미끄네일 \n종족값 68/75/53/83/113/60/총합:452`")
    if message.content.startswith("!미끄래곤"):
        await message.channel.send("`도감번호 706 미끄래곤 \n종족값 90/100/70/110/150/80/총합:600`")
    if message.content.startswith("!클레피"):
        await message.channel.send("`도감번호 707 클레피 \n종족값 57/80/91/80/87/75/총합:470`")
    if message.content.startswith("!나목령"):
        await message.channel.send("`도감번호 708 나목령 \n종족값 43/70/48/50/60/38/총합:309`")
    if message.content.startswith("!대로트"):
        await message.channel.send("`도감번호 709 대로트 \n종족값 85/110/76/65/82/56/총합:474`")
    if message.content.startswith("!호바귀(S)"):
        await message.channel.send("`도감번호 710 호바귀(S) \n종족값 44/66/70/44/55/56/총합:335`")
    if message.content.startswith("!호바귀(M)"):
        await message.channel.send("`도감번호 710 호바귀(M) \n종족값 49/66/70/44/55/51/총합:335`")
    if message.content.startswith("!호바귀(L)"):
        await message.channel.send("`도감번호 710 호바귀(L) \n종족값 54/66/70/44/55/46/총합:335`")
    if message.content.startswith("!호바귀(XL)"):
        await message.channel.send("`도감번호 710 호바귀(XL) \n종족값 59/66/70/44/55/41/총합:335`")
    if message.content.startswith("!펌킨인(S)"):
        await message.channel.send("`도감번호 711 펌킨인(S) \n종족값 55/85/122/58/75/99/총합:494`")
    if message.content.startswith("!펌킨인(M)"):
        await message.channel.send("`도감번호 711 펌킨인(M) \n종족값 65/90/122/58/75/84/총합:494`")
    if message.content.startswith("!펌킨인(L)"):
        await message.channel.send("`도감번호 711 펌킨인(L) \n종족값 75/95/122/58/75/69/총합:494`")
    if message.content.startswith("!펌킨인(XL)"):
        await message.channel.send("`도감번호 711 펌킨인(XL) \n종족값 85/100/122/58/75/54/총합:494`")
    if message.content.startswith("!꽁어름"):
        await message.channel.send("`도감번호 712 꽁어름 \n종족값 55/69/85/32/35/28/총합:304`")
    if message.content.startswith("!크레베이스"):
        await message.channel.send("`도감번호 713 크레베이스 \n종족값 95/117/184/44/46/28/총합:514`")
    if message.content.startswith("!음뱃"):
        await message.channel.send("`도감번호 714 음뱃 \n종족값 40/30/35/45/40/55/총합:245`")
    if message.content.startswith("!음번"):
        await message.channel.send("`도감번호 715 음번 \n종족값 85/70/80/97/80/123/총합:535`")
    if message.content.startswith("!제르네아스"):
        await message.channel.send("`도감번호 716 제르네아스 \n종족값 126/131/95/131/98/99/총합:680`")
    if message.content.startswith("!이벨타르"):
        await message.channel.send("`도감번호 717 이벨타르 \n종족값 126/131/95/131/98/99/총합:680`")
    if message.content.startswith("!지가르데"):
        await message.channel.send("`도감번호 718 지가르데 \n종족값 108/100/121/81/95/95/총합:600`")
    if message.content.startswith("!디안시"):
        await message.channel.send("`도감번호 719 디안시 \n종족값 50/100/150/100/150/50/총합:600`")
    if message.content.startswith("!메가디안시"):
        await message.channel.send("`도감번호 719 메가디안시 \n종족값 50/160/110/160/110/110/총합:700`")
    if message.content.startswith("!후파(굴레에 빠진 폼)"):
        await message.channel.send("`도감번호 720 후파(굴레에 빠진 폼) \n종족값 80/110/60/150/130/70/총합:600`")
    if message.content.startswith("!후파(굴레를 벗어난 폼)"):
        await message.channel.send("`도감번호 720 후파(굴레를 벗어난 폼) \n종족값 80/160/60/170/130/80/총합:680`")
    if message.content.startswith("!볼케니온"):
        await message.channel.send("`도감번호 721 볼케니온 \n종족값 80/110/120/130/90/70/총합:600`")
    if message.content.startswith("!흥나숭"):
        await message.channel.send("`도감번호 810 흥나숭 \n종족값 50/65/50/40/40/65/총합:310`")
    if message.content.startswith("!채키몽"):
        await message.channel.send("`도감번호 811 채키몽 \n종족값 70/85/70/55/60/80/총합:420`")
    if message.content.startswith("!고릴타"):
        await message.channel.send("`도감번호 812 고릴타 \n종족값 100/125/90/60/70/85/총합:530`")
    if message.content.startswith("!염버니"):
        await message.channel.send("`도감번호 813 염버니 \n종족값 50/71/40/40/40/69/총합:310`")
    if message.content.startswith("!래비풋"):
        await message.channel.send("`도감번호 814 래비풋 \n종족값 65/86/60/55/60/94/총합:420`")
    if message.content.startswith("!에이스번"):
        await message.channel.send("`도감번호 815 에이스번 \n종족값 80/116/75/65/75/119/총합:530`")
    if message.content.startswith("!울머기"):
        await message.channel.send("`도감번호 816 울머기 \n종족값 50/40/40/70/40/70/총합:310`")
    if message.content.startswith("!누겔레온"):
        await message.channel.send("`도감번호 817 누겔레온 \n종족값 65/60/55/95/55/90/총합:420`")
    if message.content.startswith("!인텔리레온"):
        await message.channel.send("`도감번호 818 인텔리레온 \n종족값 70/85/65/125/65/120/총합:530`")
    if message.content.startswith("!탐리스"):
        await message.channel.send("`도감번호 819 탐리스 \n종족값 70/55/55/35/35/25/총합:275`")
    if message.content.startswith("!요씽리스"):
        await message.channel.send("`도감번호 820 요씽리스 \n종족값 120/95/95/55/75/20/총합:460`")
    if message.content.startswith("!파라꼬"):
        await message.channel.send("`도감번호 821 파라꼬 \n종족값 38/47/35/33/35/57/총합:245`")
    if message.content.startswith("!파크로우"):
        await message.channel.send("`도감번호 822 파크로우 \n종족값 68/67/55/43/55/77/총합:365`")
    if message.content.startswith("!아머까오"):
        await message.channel.send("`도감번호 823 아머까오 \n종족값 98/87/105/53/85/67/총합:495`")
    if message.content.startswith("!두루지벌레"):
        await message.channel.send("`도감번호 824 두루지벌레 \n종족값 25/20/20/25/45/45/총합:180`")
    if message.content.startswith("!레돔벌레"):
        await message.channel.send("`도감번호 825 레돔벌레 \n종족값 50/35/80/50/90/30/총합:335`")
    if message.content.startswith("!이올브"):
        await message.channel.send("`도감번호 826 이올브 \n종족값 60/45/110/80/120/90/총합:505`")
    if message.content.startswith("!훔처우"):
        await message.channel.send("`도감번호 827 훔처우 \n종족값 40/28/28/47/52/50/총합:245`")
    if message.content.startswith("!폭슬라이"):
        await message.channel.send("`도감번호 828 폭슬라이 \n종족값 70/58/58/87/92/90/총합:455`")
    if message.content.startswith("!꼬모카"):
        await message.channel.send("`도감번호 829 꼬모카 \n종족값 40/40/60/40/60/10/총합:250`")
    if message.content.startswith("!백솜모카"):
        await message.channel.send("`도감번호 830 백솜모카 \n종족값 60/50/90/80/120/60/총합:460`")
    if message.content.startswith("!우르"):
        await message.channel.send("`도감번호 831 우르 \n종족값 42/40/55/40/45/48/총합:270`")
    if message.content.startswith("!배우르"):
        await message.channel.send("`도감번호 832 배우르 \n종족값 72/80/100/60/90/88/총합:490`")
    if message.content.startswith("!깨물부기"):
        await message.channel.send("`도감번호 833 깨물부기 \n종족값 50/64/50/38/38/44/총합:284`")
    if message.content.startswith("!갈가부기"):
        await message.channel.send("`도감번호 834 갈가부기 \n종족값 90/115/90/48/68/74/총합:485`")
    if message.content.startswith("!멍파치"):
        await message.channel.send("`도감번호 835 멍파치 \n종족값 59/45/50/40/50/26/총합:270`")
    if message.content.startswith("!펄스멍"):
        await message.channel.send("`도감번호 836 펄스멍 \n종족값 69/90/60/90/60/121/총합:490`")
    if message.content.startswith("!탄동"):
        await message.channel.send("`도감번호 837 탄동 \n종족값 30/40/50/40/50/30/총합:240`")
    if message.content.startswith("!탄차곤"):
        await message.channel.send("`도감번호 838 탄차곤 \n종족값 80/60/90/60/70/50/총합:410`")
    if message.content.startswith("!석탄산"):
        await message.channel.send("`도감번호 839 석탄산 \n종족값 110/80/120/80/90/30/총합:510`")
    if message.content.startswith("!과사삭벌레"):
        await message.channel.send("`도감번호 840 과사삭벌레 \n종족값 40/40/80/40/40/20/총합:260`")
    if message.content.startswith("!애프룡"):
        await message.channel.send("`도감번호 841 애프룡 \n종족값 70/110/80/95/60/70/총합:485`")
    if message.content.startswith("!단지래플"):
        await message.channel.send("`도감번호 842 단지래플 \n종족값 110/85/80/100/80/30/총합:485`")
    if message.content.startswith("!모래뱀"):
        await message.channel.send("`도감번호 843 모래뱀 \n종족값 52/57/75/35/50/46/총합:315`")
    if message.content.startswith("!사다이사"):
        await message.channel.send("`도감번호 844 사다이사 \n종족값 72/107/125/65/70/71/총합:510`")
    if message.content.startswith("!윽우지"):
        await message.channel.send("`도감번호 845 윽우지 \n종족값 70/85/55/85/95/85/총합:475`")
    if message.content.startswith("!찌로꼬치"):
        await message.channel.send("`도감번호 846 찌로꼬치 \n종족값 41/63/40/40/30/66/총합:280`")
    if message.content.startswith("!꼬치조"):
        await message.channel.send("`도감번호 847 꼬치조 \n종족값 61/123/60/60/50/136/총합:490`")
    if message.content.startswith("!일레즌"):
        await message.channel.send("`도감번호 848 일레즌 \n종족값 40/38/35/54/35/40/총합:242`")
    if message.content.startswith("!스트린더"):
        await message.channel.send("`도감번호 849 스트린더 \n종족값 75/98/70/114/70/75/총합:502`")
    if message.content.startswith("!태우지네"):
        await message.channel.send("`도감번호 850 태우지네 \n종족값 50/65/45/50/50/45/총합:305`")
    if message.content.startswith("!다태우지네"):
        await message.channel.send("`도감번호 851 다태우지네 \n종족값 100/115/65/90/90/65/총합:525`")
    if message.content.startswith("!때때무노"):
        await message.channel.send("`도감번호 852 때때무노 \n종족값 50/68/60/50/50/32/총합:310`")
    if message.content.startswith("!케오퍼스"):
        await message.channel.send("`도감번호 853 케오퍼스 \n종족값 80/118/90/70/80/42/총합:480`")
    if message.content.startswith("!데인차"):
        await message.channel.send("`도감번호 854 데인차 \n종족값 40/45/45/74/54/50/총합:308`")
    if message.content.startswith("!포트데스"):
        await message.channel.send("`도감번호 855 포트데스 \n종족값 60/65/65/134/114/70/총합:508`")
    if message.content.startswith("!몸지브림"):
        await message.channel.send("`도감번호 856 몸지브림 \n종족값 42/30/45/56/53/39/총합:265`")
    if message.content.startswith("!손지브림"):
        await message.channel.send("`도감번호 857 손지브림 \n종족값 57/40/65/86/73/49/총합:370`")
    if message.content.startswith("!브리무음"):
        await message.channel.send("`도감번호 858 브리무음 \n종족값 57/90/95/136/103/29/총합:510`")
    if message.content.startswith("!메롱꿍"):
        await message.channel.send("`도감번호 859 메롱꿍 \n종족값 45/45/30/55/40/50/총합:265`")
    if message.content.startswith("!쏘겨모"):
        await message.channel.send("`도감번호 860 쏘겨모 \n종족값 65/60/45/75/55/70/총합:370`")
    if message.content.startswith("!오롱털"):
        await message.channel.send("`도감번호 861 오롱털 \n종족값 95/120/65/95/75/60/총합:510`")
    if message.content.startswith("!가로막구리"):
        await message.channel.send("`도감번호 862 가로막구리 \n종족값 93/90/101/60/81/95/총합:520`")
    if message.content.startswith("!나이킹"):
        await message.channel.send("`도감번호 863 나이킹 \n종족값 70/110/100/50/60/50/총합:440`")
    if message.content.startswith("!산호르곤"):
        await message.channel.send("`도감번호 864 산호르곤 \n종족값 60/95/50/145/130/30/총합:510`")
    if message.content.startswith("!창파나이트"):
        await message.channel.send("`도감번호 865 창파나이트 \n종족값 62/135/95/68/82/65/총합:507`")
    if message.content.startswith("!마임꽁꽁"):
        await message.channel.send("`도감번호 866 마임꽁꽁 \n종족값 80/85/75/110/100/70/총합:520`")
    if message.content.startswith("!데스판"):
        await message.channel.send("`도감번호 867 데스판 \n종족값 58/95/145/50/105/30/총합:483`")
    if message.content.startswith("!마빌크"):
        await message.channel.send("`도감번호 868 마빌크 \n종족값 45/40/40/50/61/34/총합:270`")
    if message.content.startswith("!마휘핑"):
        await message.channel.send("`도감번호 869 마휘핑 \n종족값 65/60/75/110/121/64/총합:495`")
    if message.content.startswith("!대여르"):
        await message.channel.send("`도감번호 870 대여르 \n종족값 65/100/100/70/60/75/총합:470`")
    if message.content.startswith("!찌르성게"):
        await message.channel.send("`도감번호 871 찌르성게 \n종족값 48/101/95/91/85/15/총합:435`")
    if message.content.startswith("!누니머기"):
        await message.channel.send("`도감번호 872 누니머기 \n종족값 30/25/35/45/30/20/총합:185`")
    if message.content.startswith("!모스노우"):
        await message.channel.send("`도감번호 873 모스노우 \n종족값 70/65/60/125/90/65/총합:475`")
    if message.content.startswith("!돌헨진"):
        await message.channel.send("`도감번호 874 돌헨진 \n종족값 100/125/135/20/20/70/총합:470`")
    if message.content.startswith("!빙큐보(아이스페이스)"):
        await message.channel.send("`도감번호 875 빙큐보(아이스페이스) \n종족값 75/80/110/65/90/50/총합:470`")
    if message.content.startswith("!빙큐보(나이스페이스)"):
        await message.channel.send("`도감번호 875 빙큐보(나이스페이스) \n종족값 75/80/70/65/50/130/총합:470`")
    if message.content.startswith("!에써르(수컷)"):
        await message.channel.send("`도감번호 876 에써르(수컷) \n종족값 60/65/55/105/95/95/총합:475`")
    if message.content.startswith("!에써르(암컷)"):
        await message.channel.send("`도감번호 876 에써르(암컷) \n종족값 70/55/65/95/105/85/총합:475`")
    if message.content.startswith("!모르페코"):
        await message.channel.send("`도감번호 877 모르페코 \n종족값 58/95/58/70/58/97/총합:436`")
    if message.content.startswith("!끼리동"):
        await message.channel.send("`도감번호 878 끼리동 \n종족값 72/80/49/40/49/40/총합:330`")
    if message.content.startswith("!대왕끼리동"):
        await message.channel.send("`도감번호 879 대왕끼리동 \n종족값 122/130/69/80/69/30/총합:500`")
    if message.content.startswith("!파치래곤"):
        await message.channel.send("`도감번호 880 파치래곤 \n종족값 90/100/90/80/70/75/총합:505`")
    if message.content.startswith("!파치르돈"):
        await message.channel.send("`도감번호 881 파치르돈 \n종족값 90/100/90/90/80/55/총합:505`")
    if message.content.startswith("!어래곤"):
        await message.channel.send("`도감번호 882 어래곤 \n종족값 90/90/100/70/80/75/총합:505`")
    if message.content.startswith("!어치르돈"):
        await message.channel.send("`도감번호 883 어치르돈 \n종족값 90/90/100/80/90/55/총합:505`")
    if message.content.startswith("!두랄루돈"):
        await message.channel.send("`도감번호 884 두랄루돈 \n종족값 70/95/115/120/50/85/총합:535`")
    if message.content.startswith("!드라꼰"):
        await message.channel.send("`도감번호 885 드라꼰 \n종족값 28/60/30/40/30/82/총합:270`")
    if message.content.startswith("!드래런치"):
        await message.channel.send("`도감번호 886 드래런치 \n종족값 68/80/50/60/50/102/총합:410`")
    if message.content.startswith("!드래펄트"):
        await message.channel.send("`도감번호 887 드래펄트 \n종족값 88/120/75/100/75/142/총합:600`")
    if message.content.startswith("!자시안(역전의 용사)"):
        await message.channel.send("`도감번호 888 자시안(역전의 용사) \n종족값 92/130/115/80/115/138/총합:670`")
    if message.content.startswith("!자시안(검왕)"):
        await message.channel.send("`도감번호 888 자시안(검왕) \n종족값 92/170/115/80/115/148/총합:720`")
    if message.content.startswith("!자마젠타(역전의 용사)"):
        await message.channel.send("`도감번호 889 자마젠타(역전의 용사) \n종족값 92/130/115/80/115/138/총합:670`")
    if message.content.startswith("!자마젠타(방패왕)"):
        await message.channel.send("`도감번호 889 자마젠타(방패왕) \n종족값 92/130/145/80/145/128/총합:720`")
    if message.content.startswith("!무한다이노"):
        await message.channel.send("`도감번호 890 무한다이노 \n종족값 140/85/95/145/95/130/총합:690`")
    if message.content.startswith("!무한다이노(무한다이맥스)"):
        await message.channel.send("`도감번호 890 무한다이노(무한다이맥스) \n종족값 255/115/250/125/250/130/총합:1125`")


client.run("Njc5OTMxNzE3NTQwMzgwNjg5.Xk4iEw.wQnBhthx1kHPZA48qpT2CiZS4VM")