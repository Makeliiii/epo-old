from jinja2 import *
import jinja2


def main():

    board_members=[
        {"title": "Puheenjohtaja", "name": "Timo Keisala", "img": "img/keisala.jpg"},
        {"title": "Fuksikapteeni & vpj.", "name": "Aleksi Yli-Sissala", "img": "img/ylisissala.jpg"},
        {"title": "Sihteeri", "name": "Katri Ollila", "img": "img/ollila.jpg"},
        {"title": "Talousvastaava", "name": "Tuulia Ala-Nisula", "img": "img/alanisula.jpg"},
        {"title": "Haalarimerkkivastaava", "name": "Mikko Hakoniemi", "img": "img/hakoniemi.jpg"},
        {"title": "Homo Economicus", "name": "Erno Ahola-Olli", "img": "img/aholaolli.jpg"},
        {"title": "Hallituksen jäsen", "name": "Bence Berki", "img": "img/berki.jpg"},
    ]

    clerks = [
        {"title": "Webmaster", "name": "Jukka Pajukangas", "img": "img/placeholder_600x600.png"}
    ]


    templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    # Generate multiple pages
    index_template=templateEnv.get_template("index_template.html")
    index_template.stream(index_active=" active").dump("index.html")

    epo_template = templateEnv.get_template("epo_template.html")
    epo_template.stream(epo_active=" active", board_members=board_members, clerks=clerks).dump("epo.html")

    jaseneksi_template = templateEnv.get_template("jaseneksi_template.html")
    jaseneksi_template.stream(jaseneksi_active=" active").dump("jaseneksi.html")

    linkkeja_template = templateEnv.get_template("linkkeja_template.html")
    linkkeja_template.stream(linkkeja_active=" active").dump("linkkeja.html")


if __name__ == '__main__':
    main()