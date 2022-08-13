import requests
from lxml import html
import os.path

root = "https://www.goodreads.com"
info = {
"session_id2_" : "6f4920b76a56ec1e86475be8f9aaafb2",
"at-main" : "Atza|IwEBICF4f5I7_1J9dv9tCC29HRqRYSDOzqQdYvnJbm1d7kcMA0xqApn5Vn99SEgQFoq8BFCMrvfs-TlW-HEe68V_bPl8OCZuV2PD19nI0cWmTHwXQCkVPVu8VqTLkZdWRlCLbveYgN_Plqo4RE51bfnFVQdOjQ0LUWaLlygSSinBRYGh3ZJ0bfsVMULWWyJxFH5b8dFQSVnit_NBPwpmmmlSJNbA0_fqRIPSCQ2LLYOaDoGCYfY-dftGcrPyCEsg67O53Ho",
"session-id" : "132-6882092-4981846",
"session-token" : "fNNb/QeL7yOctbAf99fcvRUq0mnw+p2D9xAOdU6R/yzwO+NvzISWfS0wr1PZeZxSMeuQIA+v7y1ByAniMZZQDdj/2YbvXkJHnurfGOkWXtR811rUvg90408qWieFy16Sv/sP4kHThWVbD+wTNm1zl5Hbj/5Ehbl2XVxmdDBDewyPlT1r5GSuFgCe3H/jubCjbZPR/Z1vD1DIFAFVJBWnnfYWHvyk7sbDkgFVXYfUAAg2zsCu0p+eCi6SoIQEXcvn",
"ubid-main" : "135-8469359-7029943"
}

pageno = 10
imageno = 451

while pageno < 50:
    page = requests.get("https://www.goodreads.com/shelf/show/fantasy?page=" + str(pageno), cookies = info)
    tree = html.fromstring(page.content)
    bookno = 4
    while bookno < 104:
        for i in range(0, 5):
            try:
                link = tree.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div['+str(bookno)+']/div[1]/a[2]/@href')
                bookpage = requests.get(root+link[0])
                booktree = html.fromstring(bookpage.content)
                coverart = booktree.xpath('//*[@id="coverImage"]/@src')
                file = open("F:/Game project/images/book"+str(imageno)+".jpg", "wb")
                file.write(requests.get(coverart[0]).content)
                file.close()
            except:
                continue
            else:
                break
        bookno += 2
        imageno += 1
    pageno += 1



