from PIL import Image
import random as rd

class Manipulate():
    sub_img_lis = []
    # 메인 이미지 설정
    main_img = Image.open('1.jpg')

    # 합성에 사용할 이미지 리스트에 추가
    for i in range(9):
        a = Image.open(f"{i}.png")
        a = a.resize((60, 60))
        sub_img_lis.append(a)

    for i in range(9):
        x = rd.randint(0, 500)
        y = rd.randint(0, 300)
        a = sub_img_lis[i]
        main_img.paste(sub_img_lis[i], (x, y), sub_img_lis[i])

    # result로 저장
    main_img.save('result.jpg')
    main_img.show()
