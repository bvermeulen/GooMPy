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
from decouple import config


# Get a key from https://developers.google.com/maps/documentation/staticmaps/#api_key and
# put it between the quotation marks below:
_KEY = config('GOOGLE_API_KEY')
