from yandex_map.yandex_map import (
    search_business, 
    get_coordinates,
    show_map,
    get_map,
    del_map,
    generate_spn,
    get_territory_business
)
import argparse
from yandex_map.distance import distance_two_point


parser = argparse.ArgumentParser()
parser.add_argument("adres")

territory = get_territory_business(parser.parse_args().adres, "аптека")
start_coords = get_coordinates(parser.parse_args().adres)

points = str(search_business(start_coords, "аптека", 1)) + f"~{str(start_coords[0])},{str(start_coords[1])},pm2blm"

farm = search_business(start_coords, "аптека", 1, get_object=True)[0]

image = get_map(start_coords, spn=generate_spn(territory), pt=points)
show_map(image)
del_map(image)
print(f"Расстояние от аптеки до точки: {distance_two_point(start_coords, farm.coords)}")
print(f"Адрес: {farm.get_adres()}")
print(f"Название: {farm.get_name()}")
print(f"Время работы: {farm.get_active()}")
# # """python one_pharrmacy.py "еликий овгород -осковская 120 к1""""