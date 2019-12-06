'''
GooMPy: Google Maps for Python
Copyright (C) 2015 Alec Singer and Simon D. Levy
This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this code.  If not, see <http://www.gnu.org/licenses/>.

Updated by Bruno Vermeulen @2019
'''
from .goompy_functions import _new_image, fetchTiles

class GooMPy(object):

    def __init__(self, width, height, latitude, longitude, zoom,
                 maptype, radius_meters=None, default_ntiles=4):
        '''
        Creates a GooMPy object for specified display width and height at the specified
        coordinates, zoom level (0-22), and map type ('roadmap', 'terrain', 'satellite',
        or 'hybrid'). The value of radius_meters deteremines the number of tiles that will
        be used to create the map image; if it is unspecified, the number defaults to
        default_ntiles.
        '''
        self.lat = latitude
        self.lon = longitude

        self.width = width
        self.height = height

        self.zoom = zoom
        self.maptype = maptype
        self.radius_meters = radius_meters
        self.default_ntiles = default_ntiles

        self.winimage = _new_image(self.width, self.height)

        self._fetch()

        halfsize = int(self.bigimage.size[0] / 2)
        self.leftx = halfsize
        self.uppery = halfsize

        self._update()

    def getImage(self):
        '''
        Returns the current image as a PIL.Image object.
        '''
        return self.winimage

    def move(self, dx, dy):
        '''
        Moves the view by the specified pixels dx, dy.
        '''
        self.leftx = self._constrain(self.leftx, dx, self.width)
        self.uppery = self._constrain(self.uppery, dy, self.height)
        self._update()

    def useMaptype(self, maptype):
        '''
        Uses the specified map type 'roadmap', 'terrain', 'satellite', or 'hybrid'.
        Map tiles are fetched as needed.
        '''
        self.maptype = maptype
        self._fetch_and_update()

    def useZoom(self, zoom):
        '''
        Uses the specified zoom level 0 through 22.
        Map tiles are fetched as needed.
        '''
        self.zoom = zoom
        self._fetch_and_update()

    def _fetch_and_update(self):
        self._fetch()
        self._update()

    def _fetch(self):
        self.bigimage, self.northwest, self.southeast = fetchTiles(
            self.lat, self.lon, self.zoom, self.maptype,
            self.radius_meters, default_ntiles=self.default_ntiles)

    def _update(self):
        self.winimage.paste(self.bigimage, (-self.leftx, -self.uppery))

    def _constrain(self, oldval, diff, dimsize):
        newval = oldval + diff
        return newval if newval > 0 and newval < self.bigimage.size[0]-dimsize else oldval