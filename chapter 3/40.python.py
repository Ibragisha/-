def analyze_trees(file_path):
    max_height = 0
    max_diameter = 0
    tallest_tree = None
    widest_tree = None

    with open(file_path, 'r') as file:

        for line in file:

            data = line.strip().split('\t')
            if len(data) < 3:

                continue

            tree_name = data[0]
            height = float(data[1])
            diameter = float(data[2])


            if height > max_height:
                max_height = height
                tallest_tree = tree_name

            if diameter > max_diameter:
                max_diameter = diameter
                widest_tree = tree_name


    message = f"Самое высокое дерево: {tallest_tree} с высотой {max_height} метров.\n"
    message += f"Дерево с наибольшим диаметром: {widest_tree} с диаметром {max_diameter} метров."

    return message


file_path = '/data/wood.txt'


result = analyze_trees(file_path)
print(result)