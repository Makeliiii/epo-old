from jinja2 import *
import jinja2


def main():

    old_members = [
        {
            "year": 2019,
            "board": [
                {"title": "Puheenjohtaja", "name": "Erno Ahola-Olli"},
                {"title": "Varapuheenjohtaja", "name": "Timo Keisala"},
                {"title": "Fuksikapteeni", "name": "Aleksi Yli-Sissala"},
                {"title": "Sihteeri", "name": "Katri Ollila"},
                {"title": "Talousvastaava", "name": "Sanni Yli-Ojanperä"},
                {"title": "Emäntä ja merkkivastaava", "name": "Tuulia Ala-Nisula"},
                {"title": "Varajäsen", "name": "Tuulia Tuomaala"},
                {"title": "Varajäsen", "name": "Jukka Pajukangas"}
            ],
            "clerks": [
                {"title": "Liikunta- ja AMK-vastaava", "name": "Pietari Purola"},
                {"title": "Analfabeetti Teknokraatti ja Lohikäärmeiden Äiti", "name": "Eetu Riskumäki"},
                {"title": "Webmaster", "name": "Jukka Pajukangas"}
            ]
        },
        {
            "year": 2018,
            "board": [
                {"title": "Puheenjohtaja", "name": "Eetu Riskumäki"},
                {"title": "Varapuheenjohtaja/Fuksikapteeni", "name": "Bence Berki"},
                {"title": "Sihteeri", "name": "Sanni Yli-Ojanperä"},
                {"title": "Rahastonhoitaja", "name": "Erno Ahola-Olli"},
                {"title": "Emäntä", "name": "Tuulia Tuomaala"},
                {"title": "Isäntä", "name": "Timo Keisala"},
                {"title": "Haalarimerkkivastaava", "name": "Paavo Lahdensuo"},
                {"title": "Webmaster", "name": "Jukka Pajukangas"}
            ],
            "clerks": [
                {"title": "AMK-vastaava", "name": "Pietari Purola"},
                {"title": "Seniori", "name": "Sameli Piirto"},
                {"title": "Liikuntavastaava", "name": "Pietari Purola"}
            ]
        },
        {
            "year": 2017,
            "board": [
                {"title": "Puheenjohtaja", "name": "Sameli Piirto"},
                {"title": "Varapuheenjohtaja/Sihteeri", "name": "Erno Ahola-Olli"},
                {"title": "Fuksikapteeni", "name": "Ulla Mäkinen"},
                {"title": "Talousvastaava", "name": "Eetu Riskumäki"},
                {"title": "Emäntä", "name": "Sanni Yli-Ojanperä"},
                {"title": "Isäntä", "name": "Kimmo Mäkelä"},
                {"title": "Liikuntavastaava", "name": "Pietari Purola"},
                {"title": "Webmaster", "name": "Jukka Pajukangas"}
            ],
            "clerks": [
                {"title": "Pikkuemäntä", "name": "Anna Mäkinen"},
                {"title": "AMK-vastaava", "name": "Sanna Saarenpää"},
                {"title": "Seniori/Ylijumalatar", "name": "Anna Mäkinen"},
                {"title": "Projekti-Sami", "name": "Sami Saarenpää"},
                {"title": "Apuprojekti-Sami", "name": "Leena Hanhimäki"}
            ]
        },
        {
            "year": 2016,
            "board": [
                {"title": "Puheenjohtaja", "name": "Anna Mäkinen"},
                {"title": "Sihteeri", "name": "Outi Rinta-Homi"},
                {"title": "Varapuheenjohtaja/fuksikapteeni", "name": "Sameli Piirto"},
                {"title": "Talousvastaava", "name": "Pirita Ojanperä"},
                {"title": "Emäntä", "name": "Johanna Koskinen"},
                {"title": "Isäntä", "name": "Leena Hanhimäki"},
                {"title": "Liikuntavastaava", "name": "Pietari Purola"},
                {"title": "Webmaster", "name": "Jukka Pajukangas"}
            ],
            "clerks": [
                {"title": "Pikkuemäntä/AMK-vastaava", "name": "Sanna Saarenpää"},
                {"title": "Pikkuemäntä", "name": "Leena Rinta-Rusala"},
                {"title": "Pehtoori", "name": "Mika Väisänen"},
                {"title": "Osakuntamestari", "name": "Anna Mäkinen"},
                {"title": "Osakuntakamera &amp;<br> Lainaamotäti", "name": "Kaisa Mäkinen"},
                {"title": "Seniori", "name": "Asta Myllymäki"},
                {"title": "Kuraattori", "name": "Aatto Rautio"},
                {"title": "Projekti-Sami", "name": "Sami Saarenpää"},
                {"title": "Apuprojekti-Sami", "name": "Ulla Mäkinen"}
            ]
        },
        {
            "year": 2015,
            "board": [
                {"title": "Puheenjohtaja", "name": "Asta Myllymäki"},
                {"title": "Sihteeri", "name": "Outi Rinta-Homi"},
                {"title": "Varapuheenjohtaja/fuksikapteeni", "name": "Ulla Mäkinen"},
                {"title": "Talousvastaava", "name": "Pirita Ojanperä"},
                {"title": "Emäntä", "name": "Johanna Koskinen"},
                {"title": "Isäntä", "name": "Leena Hanhimäki"},
                {"title": "Liikuntavastaava", "name": "Pietari Purola"},
                {"title": "Webmaster", "name": "Rasmus Rudnäs"}
            ],
            "clerks": [
                {"title": "Pikkuemäntä/AMK-vastaava", "name": "Sanna Saarenpää"},
                {"title": "Pehtoori", "name": "Mika Väisänen"},
                {"title": "Osakuntamestari", "name": "Anna Mäkinen"},
                {"title": "Osakuntakamera &amp;<br> Lainaamotäti", "name": "Kaisa Mäkinen"},
                {"title": "Seniori", "name": "Sami Saarenpää"},
                {"title": "Vuosijuhla-assistentti", "name": "Joona Lahti"},
                {"title": "Kuraattori", "name": "Aatto Rautio"}
            ]
        },
        {
            "year": 2014,
            "board": [
                {"title": "Puheenjohtaja", "name": "Sami Saarenpää"},
                {"title": "Sihteeri", "name": "Anni Sillanpää"},
                {"title": "Varapuheenjohtaja/osakuntamestari", "name": "Anna Mäkinen"},
                {"title": "Talousvastaava", "name": "Joona Rintamäki"},
                {"title": "Emäntä", "name": "Asta Myllymäki"},
                {"title": "Isäntä", "name": "Markus Anttila"},
                {"title": "Fuksikapteeni", "name": "Outi Rinta-Homi"},
                {"title": "Webmaster", "name": "Susanna Sillanpää"}
            ],
            "clerks": [
                {"title": "Pikkuemäntä", "name": "Leena Rinta-Runsala"},
                {"title": "Pehtoori", "name": "Eero Vuorenmaa"},
                {"title": "Liikuntavastaava/AMK-vastaava", "name": "Matti Niemi-Nikkola"},
                {"title": "Osakuntakamera", "name": "Kaisa Mäkinen"},
                {"title": "Seniori / Osakunnan \"hengellinen johtaja\"", "name":"Joona Lahti"},
                {"title": "Kuraattori", "name": "Mats Kronholm"}
            ]
        },
        {
            "year": 2013,
            "board": [
                {"title": "Puheenjohtaja", "name": "Joona Lahti"},
                {"title": "Sihteeri", "name": "Leena Rinta-Runsala"},
                {"title": "Rahastonhoitaja", "name": "Anna Mäkinen"},
                {"title": "Emäntä", "name": "Asta Myllymäki"},
                {"title": "Isäntä", "name": "Mika Väisänen"},
                {"title": "Fuksikapteeni", "name": "Sami Saarenpää"},
                {"title": "Liikuntavastaava", "name": "Joona Rintamäki"},
                {"title": "Webmaster", "name": "Susanna Sillanpää"},
                {"title": "Varajäsen", "name": "Riikka Muotio"},
                {"title": "Varajäsen", "name": "Henriikka Hentilä"}
            ],
            "clerks": [
                {"title": "Pikkuemäntä", "name": "Kaisa Mäkinen"},
                {"title": "Pehtoori", "name": "Markus Anttila"},
                {"title": "Osakuntakamera", "name": "Henriikka Hentilä"},
                {"title": "AMK-vastaava", "name": "Matti Niemi-Nikkola"},
                {"title": "Seniori", "name": "Anniina Kivimäki"},
                {"title": "Kuraattori", "name": "Mats Kronholm"},
                {"title": "Inspehtoori", "name": "Marko Huttula"},
                {"title": "Toiminnantarkastaja", "name": "Henna Väkiparta"},
                {"title": "Toiminnantarkastaja", "name": "Ville Akonlahti"}
            ]
        },
        {
            "year": 2012,
            "board": [
                {"title": "Puheenjohtaja", "name": "Anniina Kivimäki"},
                {"title": "Sihteeri", "name": "Sami Saarenpää"},
                {"title": "Rahastonhoitaja", "name": "Joona Lahti"},
                {"title": "Emäntä", "name": "Saara Hippi"},
                {"title": "Osakuntamestari", "name": "Riikka Muotio"},
                {"title": "Webmaster", "name": "Tuomo Takala"},
                {"title": "Fuxikapteeni", "name": "Kaisa Mäkinen"}
            ],
            "clerks": [
                {"title": "AMK-vastaava", "name": "Matti Niemi-Nikkola"},
                {"title": "Pehtoori", "name": "Matti Karikallio"},
                {"title": "Pikkuemännät", "name": "Asta Myllymäki ja Sofia Ranta-Aho"},
                {"title": "Osakuntakamera", "name": "Leena Rinta-Runsala"},
                {"title": "Kirjastosetä", "name": "Veli-Pekka Rämäkkö"},
                {"title": "Seniori", "name": "Kaisa Tuppi"},
                {"title": "Kuraattori", "name": "Mats Kronholm"},
                {"title": "Inspehtori", "name": "Marko Huttula"}
            ]
        },
        {
            "year": 2011,
            "board": [
                {"title": "Puheenjohtaja", "name": "Kaisa Tuppi"},
                {"title": "Sihteeri", "name": "Kaisa Mäkinen"},
                {"title": "Rahastonhoitaja", "name": "Riikka Muotio"},
                {"title": "Päätoimittaja", "name": "Kirsi Kankaanpää"},
                {"title": "Emäntä", "name": "Anniina Kivimäki"},
                {"title": "Osakuntamestari", "name": "Leena Rinta-Runsala"},
                {"title": "Webmaster", "name": "Veli-Pekka Rämäkkö"},
                {"title": "Liikuntamestari", "name": "Riku Mäkynen"},
                {"title": "Fuxikapteeni", "name": "Tuomo Takala"}
            ],
            "clerks": [
                {"title": "Pehtoori", "name": "Matti Karikallio"},
                {"title": "Pikkuemäntä", "name": "Henna Väkiparta"},
                {"title": "Kuraattori", "name": "Ilkka Sillanpää"}
            ]
        },
        {
            "year": 2010,
            "board": [
                {"title": "Puheenjohtaja", "name": "Kaisa Tuppi"},
                {"title": "Sihteeri", "name": "Kirsi Kankaanpää"},
                {"title": "Rahastonhoitaja", "name": "Riikka Muotio"},
                {"title": "Isäntä", "name": "Petteri Väänänen"},
                {"title": "Emäntä", "name": "Mari Pukkinen"},
                {"title": "Osakuntamestari", "name": "Jaakko Ala-Reinikka"},
                {"title": "Webmaster", "name": "Veli-Pekka Rämäkkö"},
                {"title": "Liikuntamestari", "name": "Tuomo Takala"},
                {"title": "Fuxikapteeni", "name": "Milla Heikkilä"}
            ],
            "clerks": [
                {"title": "Pehtoori", "name": "Matti Karikallio"},
                {"title": "Pehtoori", "name": "Jarno Asiala"},
                {"title": "Pikkuemäntä", "name": "Anniina Kivimäki"},
                {"title": "Pikkuemäntä", "name": "Leena Yli-Korhonen"},
                {"title": "Kuraattori", "name": "Ilkka Sillanpää"},
                {"title": "EPO-seniori", "name": "Henna Väkiparta"}
            ]
        },
        {
            "year": 2009,
            "board": [
                {"title": "Puheenjohtaja", "name": "Henna Väkiparta"},
                {"title": "Sihteeri", "name": "Kirsi Kankaanpää"},
                {"title": "Rahastonhoitaja", "name": "Ville Akolahti"},
                {"title": "Isäntä", "name": "Jarno Asiala"},
                {"title": "Emäntä", "name": "Maarit Rantanen"},
                {"title": "Tuotepäällikkö", "name": "Aatto Rautio"},
                {"title": "Webmaster", "name": "Veli-Pekka Rämäkkö"},
                {"title": "Yrityssuhdevastaava", "name": "Milla Heikkilä"},
                {"title": "Liikuntamestari", "name": "Petteri Väänänen"},
                {"title": "Fuxikapteeni", "name": "Mari Pukkinen"},
                {"title": "Varajäsen", "name": "Kaisa Tuppi"},
                {"title": "Varajäsen", "name": "Timo Perälä"}
            ],
            "clerks": [
                {"title": "Päätoimittaja", "name": "Kaisa Tuppi"},
                {"title": "Pehtoori", "name": "Juhani Honkala"},
                {"title": "Pikkuemäntä", "name": "Eeva-Mari Loponen"},
                {"title": "Osakuntakamera", "name": "Timo Perälä"},
                {"title": "Kuraattori", "name": "Ilkka Sillanpää"},
                {"title": "EPO-seniori", "name": "Matti Karikallio"}
            ]
        },

        {
            "year": 2008,
            "board": [
                {"title": "Puheenjohtaja", "name": "Matti Karikallio"},
                {"title": "Sihteeri", "name": "Maarit Rantanen"},
                {"title": "Rahastonhoitaja", "name": "Ville Akolahti"},
                {"title": "Isäntä", "name": "Olli Kalliokoski"},
                {"title": "Emäntä", "name": "Henna Väkiparta"},
                {"title": "Tuotepäällikkö", "name": "Aatto Rautio"},
                {"title": "Yrityssuhdevastaava", "name": "Marjukka Mannila"},
                {"title": "Liikuntamestari", "name": "Juhani Honkala"},
                {"title": "Fuxikapteeni", "name": "Jarno Asiala"},
                {"title": "Osakuntamestari", "name": "Veli-Pekka Rämäkkö"},
                {"title": "Varajäsen", "name": "Kirsi Kotimäki"},
                {"title": "Varajäsen", "name": "Antti Rautio"}
            ],
            "clerks": [
                {"title": "Päätoimittaja", "name": "Kirsi Kotimäki"},
                {"title": "Pehtoori", "name": "Jarkko Halmesmäki"},
                {"title": "Pehtoori", "name": "Jaakko Ala-Reinikka"},
                {"title": "Pehtoori", "name": "Tuomas Lehtola"},
                {"title": "Pikkuemäntä", "name": "Kirsi Kankaanpää"},
                {"title": "Pikkuemäntä", "name": "Maria Lemponen"},
                {"title": "Pikkuemäntä", "name": "Mari Pukkinen"},
                {"title": "Pikkuemäntä", "name": "Tanja Korpela"},
                {"title": "AMK-vastaava", "name": "Leena Yli-Korhonen"},
                {"title": "Osakuntakamera", "name": "Timo Perälä"},
                {"title": "EPO-seniori", "name": "Matti Karikallio"},
                {"title": "Webmaster", "name": "Antti Rautio"}
            ]
        },

        {
            "year": 2007,
            "board": [
                {"title": "Puheenjohtaja", "name": "Matti Karikallio"},
                {"title": "Sihteeri", "name": "Leena Yli-Korhonen"},
                {"title": "Rahastonhoitaja", "name": "Marjukka Mannila"},
                {"title": "Isäntä", "name": "Jaakko Ala-Reinikka"},
                {"title": "Emäntä", "name": "Maiju Sepponen"},
                {"title": "Tuotepäällikkö", "name": "Antti Rautio"},
                {"title": "Liikuntamestari", "name": "Jani Hovila"},
                {"title": "Fuxikapteeni", "name": "Mats Kronholm"},
                {"title": "Osakuntamestari", "name": "Veli-Pekka Rämäkkö"},
                {"title": "Yrityssuhdevastaava", "name": "Tanja Korpela"},
                {"title": "Varajäsen", "name": "Kirsi Kotimäki"},
                {"title": "Varajäsen", "name": "Ville Akolahti"}
            ],
            "clerks": [
                {"title": "Päätoimittaja", "name": "Kirsi Kotimäki"},
                {"title": "Pehtoori", "name": "Ville Akolahti"},
                {"title": "Pehtoori", "name": "Juhani Honkala"},
                {"title": "Pehtoori", "name": "Jarno Asiala"},
                {"title": "Pikkuemäntä", "name": "Maria Lemponen"},
                {"title": "Pikkuemäntä", "name": "Terhi Talvitie"},
                {"title": "Osakuntakamera", "name": "Tuomas Lehtola"},
                {"title": "Webmaster", "name": "Janne Kätevä"},
                {"title": "AMK- ja Excuvastaava", "name": "Maarit Rantanen"},
                {"title": "EPO-seniori", "name": "Mari-Leena Kairivaara"}
            ]
        },

        {
            "year": 2006,
            "board": [
                {"title": "Puheenjohtaja", "name": "Mari-Leena Kairivaara"},
                {"title": "Sihteeri", "name": "Leena Yli-Korhonen"},
                {"title": "Rahastonhoitaja", "name": "Marjukka Mannila"},
                {"title": "Isäntä", "name": "Matti Karikallio"},
                {"title": "Emäntä", "name": "Katri Arokallio"},
                {"title": "Tuotevastaava & Webmaster", "name": "Antti Rautio"},
                {"title": "Osakuntamestari", "name": "Juha Haapasaari"},
                {"title": "Liikuntamestari", "name": "Jaakko Ala-Reinikka"},
                {"title": "Fuxikapteeni", "name": "Maiju Sepponen"},
                {"title": "Varajäsen", "name": "Jani Hovila"},
                {"title": "Varajäsen", "name": "Iida-Maria Mäki-Mantila"}
            ],
            "clerks": [
                {"title": "Pehtoori", "name": "Jani Hovila"},
                {"title": "Pehtoori", "name": "Tuomas Lehtola"},
                {"title": "Pikkuemäntä", "name": "Iida-Maria Mäki-Mantila"},
                {"title": "AMK-vastaava", "name": "Maarit Rantanen"},
                {"title": "Excupäällikkö", "name": "Terhi Talvitie"},
                {"title": "Yrityssuhdevastaava", "name": "Tanja Korpela"}
            ]
        },

        {
            "year": 2005,
            "board": [
                {"title": "Puheenjohtaja", "name": "Ilkka Sillanpää"},
                {"title": "Sihteeri", "name": "Kirsi Rantanen"},
                {"title": "Rahastonhoitaja", "name": "Mari-Leena Kairivaara"},
                {"title": "Isäntä", "name": "Matti Karikallio"},
                {"title": "Emäntä", "name": "Katri Arokallio"},
                {"title": "Seremoniamestari", "name": "Juha Haapasaari"},
                {"title": "Excupäällikkö & Webmaster", "name": "Antti Rautio"},
                {"title": "Yrityssuhdevastaava", "name": "Maiju Sepponen"},
                {"title": "Fuxikapteeni", "name": "Terhi Talvitie"},
                {"title": "Varajäsen", "name": "Jussi Eväsoja"},
                {"title": "Varajäsen", "name": "Iida-Maria Mäki-Mantila"}
            ],
            "clerks": [
                {"title": "Päätoimittaja", "name": "Iida-Maria Mäki-Mantila"},
                {"title": "Pehtoori", "name": "Aatto Rautio"},
                {"title": "Tuotepäällikkö", "name": "Jussi Eväsoja"}
            ]
        },
    ]



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
    epo_template.stream(epo_active=" active", board_members=board_members, clerks=clerks, old_members=old_members).dump("epo.html")

    jaseneksi_template = templateEnv.get_template("jaseneksi_template.html")
    jaseneksi_template.stream(jaseneksi_active=" active").dump("jaseneksi.html")

    linkkeja_template = templateEnv.get_template("linkkeja_template.html")
    linkkeja_template.stream(linkkeja_active=" active").dump("linkkeja.html")


if __name__ == '__main__':
    main()