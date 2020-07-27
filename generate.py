from jinja2 import *
import jinja2


def main():

    board_members=[
        {"title": "Puheenjohtaja", "name": "Timo Keisala"},
        {"title": "Fuksikapteeni & vpj.", "name": "Aleksi Yli-Sissala"},
        {"title": "Sihteeri", "name": "Katri Ollila"},
        {"title": "Talousvastaava", "name": "Tuulia Ala-Nisula"},
        {"title": "Haalarimerkkivastaava", "name": "Mikko Hakoniemi"},
        {"title": "Homo Economicus", "name": "Erno Ahola-Olli"},
        {"title": "Hallituksen jäsen", "name": "Bence Berki"},
    ]


    templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    # Generate multiple pages
    index_template=templateEnv.get_template("index_template.html")
    index_template.stream(index_active=" active").dump("index.html")

    epo_template = templateEnv.get_template("epo_template.html")
    epo_template.stream(epo_active=" active", board_members=board_members).dump("epo.html")

    jaseneksi_template = templateEnv.get_template("jaseneksi_template.html")
    jaseneksi_template.stream(jaseneksi_active=" active").dump("jaseneksi.html")

    linkkeja_template = templateEnv.get_template("linkkeja_template.html")
    linkkeja_template.stream(linkkeja_active=" active").dump("linkkeja.html")


if __name__ == '__main__':
    main()