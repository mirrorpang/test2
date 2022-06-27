from PIL import Image
import piexif
import os


def address():
    """
    遍历目标文件夹所有文件名
    """

    list = os.listdir(inPwd)
    return list


def getInfo():
    """
    获取一个图片将其Exif信息输出
    函数内的imgPwd为一种图片的绝对路径，因为测试，若要使用，需查看上下逻辑，重写
    """

    exif_dict = piexif.load(imgPwd)
    for ifd in ("Exif",):
        for tag in exif_dict[ifd]:
            print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])


def changeDate(imgName):
    """
    修改一张图片的Exif值，前提是能够获取这个值
    """

    imagePwd = inPwd + imgName
    im = Image.open(imagePwd)
    exif_dict = piexif.load(im.info["exif"])
    exif_dict = {}
    exif_dict["Exif"][piexif.ExifIFD.DateTime] = takeTime
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = takeTime
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = takeTime
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, imagePwd)


def setDate(imgName):
    """
    对于一张信息为空的图片，填充Exif数据
    """

    imagePwd = inPwd + '\\'+ imgName
    exif_ifd = {
        piexif.ExifIFD.DateTimeOriginal: imgTime,
        piexif.ExifIFD.DateTimeDigitized: imgTime,
    }
    exif_dict = {"Exif": exif_ifd}
    exif_bytes = piexif.dump(exif_dict)
    im = Image.open(imagePwd)
    im.save(outPwd + imgName, exif=exif_bytes)


if __name__ == '__main__':
    """
    inPwd 图片所在文件夹
    outPwd 图片输出文件夹
    imgTime 修改的图片时间
    imgName 图片名称
    imagePwd 图片绝对路径
    """
    inPwd = r"F:\自学内容\python\excel操作\pic_date\data"
    outPwd = r"F:\自学内容\python\excel操作\pic_date"
    imgTime = "2013:12:19 10:10:10"
    list = address()
    for x in list:
        setDate(x)
