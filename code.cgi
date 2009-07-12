#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import web
import sys
import bdz
import utils
import json

template_globals = {
    'url': utils.url,
    'images_url': utils.images_url,
    'style_url': utils.style_url,
    'js_url': utils.js_url,
    'web': web,
    'option': utils.option,
    'hasattr': hasattr,
    'json': json,
    'bdz': bdz,
}

render = web.template.render('templates/', base='layout', globals=template_globals)

def static(name):
    class Static:
        def GET(self):
            return getattr(render, name)()
    return Static

class BDZ:
    i = lambda self: web.input(from_station='', to_station='')
    
    def GET(self):      
            return render.bdz(bdz.stations(), i=self.i())
    def POST(self):
        i = self.i()
        i.from_station, i.to_station = [bdz.canonical_station(s) for s in (i.from_station, i.to_station)]
        trains = bdz.trains(i.from_station, i.to_station)
        if trains:
            bdz.add_to_user_stations(i.from_station, i.to_station)
        return render.bdz(bdz.stations(), trains, i=i, contact_places=bdz.contact_places)

urls = (
    '/', static('index'),
    '/bdz', BDZ,
    '/about', static('about')
)


app = web.application(urls, globals())

if __name__ == "__main__": app.run()