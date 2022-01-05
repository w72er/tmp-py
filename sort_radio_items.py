INPUT_TXT = 'input.txt'
OUTPUT_TXT = 'output.txt'


def scan_radio_items():
    items = []
    with open(INPUT_TXT, 'r') as inp:
        item_counts = int(inp.readline())
        for i in range(item_counts):
            values = inp.readline().strip()
            values = values.split(', ')
            type_ = values[0]
            size = int(values[1])
            nominal = float(values[2])
            items.append({'type_': type_, 'size': size, 'nominal': nominal})
        return items


def sort_radio_items(items):
    return sorted(items, key=lambda i: (-i['size'], i['type_'], i['nominal']))


def print_radio_items(items):
    with open(OUTPUT_TXT, 'w') as out:
        for item in items:
            out.write(f'{item["type_"]}: {item["nominal"]}; {item["size"]}\n')


if __name__ == '__main__':
    radio_items = scan_radio_items()
    sorted_items = sort_radio_items(radio_items)
    print_radio_items(sorted_items)
