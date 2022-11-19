import texture_show as image
map_w = 50
map_h = 50
first_lvl = [
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "0000000000000",
    "1111111111111"
]
list_create_map = []
map_rect = []
def create_area(level,texture):
    x = 0
    y = 0
    for string in level:
        for el in string:
            if el == "1":
                obj = image.image(
                    x= x,
                    y= y,
                    width= map_w,
                    height= map_h,
                    name_img= (texture)
                )
                obj.load_texture()
                list_create_map.append(obj)
                map_rect.append(obj.RECT)

            x += map_w
        x = 0
        y += map_h
create_area(first_lvl,"texture/platforms/test.png")