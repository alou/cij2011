#!usr/bin/env python
# -*- coding= UTF-8 -*-
#maintainer: alou

import xlwt
import StringIO
from datetime import date


font_title = xlwt.Font()
font_title.name = 'Times New Roman'
font_title.bold = True
font_title.height = 19 * 0x14
font_title.underline = xlwt.Font.UNDERLINE_DOUBLE

font1 = xlwt.Font()
font1.name = 'Verdana'
font1.height = 10 * 0x14
font1.bold = True

borders_title = xlwt.Borders()
borders_title.left = 0
borders_title.right = 0
borders_title.top = 0
borders_title.bottom = 1

borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1

al = xlwt.Alignment()
al.horz = xlwt.Alignment.HORZ_CENTER
al.vert = xlwt.Alignment.VERT_CENTER
al1 = xlwt.Alignment()
al1.horz = xlwt.Alignment.HORZ_RIGHT

color = xlwt.Pattern()
color.pattern = xlwt.Pattern.SOLID_PATTERN
color.pattern_fore_colour = 22

style_title = xlwt.XFStyle()
style_title.font = font_title
style_title.alignment = al
style_title.borders = borders_title

style_t_table = xlwt.XFStyle()
style_t_table.font = font1
style_t_table.pattern = color
style_t_table.alignment = al
style_t_table.borders = borders

style_row_table = xlwt.XFStyle()
style_row_table.borders = borders

style = xlwt.XFStyle()
style.alignment = al1


def liste_des_leo(pampers):
    ''' Export data '''
    # Principe
    # write((nbre ligne - 1), nbre colonne, "contenu", style(optionnel).
    # write_merge((nbre ligne - 1), (nbre ligne - 1) + nbre de ligne
    # à merger, (nbre de colonne - 1), (nbre de colonne - 1) + nbre
    # de colonne à merger, u"contenu", style(optionnel)).
    #~ from ipdb import set_trace; set_trace()
    book = xlwt.Workbook(encoding='ascii')
    sheet = book.add_sheet(u"la liste des LEO")
    rowx = 0
    sheet.write_merge(rowx, rowx + 2, 0, 3,\
                            u"Liste des LEO pré-inscrit", style_title)
    rowx += 4

    sheet.col(1).width = 0x0d00 * 2
    sheet.col(2).width = 0x0d00 * 2
    sheet.col(3).width = 0x0d00 * 2
    sheet.col(4).width = 0x0d00 * 2
    sheet.col(5).width = 0x0d00 * 2
    sheet.col(6).width = 0x0d00 * 3
    sheet.col(7).width = 0x0d00 * 1
    sheet.col(8).width = 0x0d00 * 3
    sheet.col(9).width = 0x0d00 * 1
    sheet.col(10).width = 0x0d00 * 1
    sheet.col(11).width = 0x0d00 * 2
    sheet.col(12).width = 0x0d00 * 2
    sheet.col(13).width = 0x0d00 * 2
    hdngs = [u"Titre",u"Nom", u"Prénom", u"Pays", u"Ville", u"Nationalité", u"Email", u"Langue", u"Nom du club", u"Zone", u"DIstrict", u"Date d'arrivée", u"Date de départ","Moyen de tranport"]
    rowx += 3
    for colx, value in enumerate(hdngs):
        sheet.write(rowx, colx, value, style_t_table)
    rowx += 1
    for pamper in pampers:
        sheet.write(rowx, 0, pamper.title)
        sheet.write(rowx, 1, pamper.first_name)
        sheet.write(rowx, 2, pamper.last_name)
        sheet.write(rowx, 3, pamper.country.name)
        sheet.write(rowx, 4, pamper.city)
        sheet.write(rowx, 5, pamper.nationality.name)
        sheet.write(rowx, 6, pamper.email)
        sheet.write(rowx, 7, pamper.language)
        sheet.write(rowx, 8, pamper.club_name)
        sheet.write(rowx, 9, pamper.zone)
        sheet.write(rowx, 10, pamper.district)
        sheet.write(rowx, 11, pamper.date_to_arrive.strftime("%d/%m/%Y"))
        sheet.write(rowx, 12, pamper.departure_date.strftime("%d/%m/%Y"))
        sheet.write(rowx, 13, pamper.transportation.name)
        rowx += 1



    stream = StringIO.StringIO()
    book.save(stream)
    return stream


