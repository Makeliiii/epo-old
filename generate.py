from jinja2 import *
import jinja2


def main():
    templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    # Generate multiple pages
    index_template=templateEnv.get_template("index_template.html")
    index_template.stream().dump("index.html")

    epo_template = templateEnv.get_template("epo_template.html")
    epo_template.stream().dump("epo.html")

    jaseneksi_template = templateEnv.get_template("jaseneksi_template.html")
    jaseneksi_template.stream().dump("jaseneksi.html")


if __name__ == '__main__':
    main()