import csv

grid_rows = 8
grid_cols = 3
label_x_span = 47
label_y_span = 14.5 
label_spacing = 5 

total_labels_printed = grid_rows * grid_cols

total_x_span = (grid_cols * (label_x_span+label_spacing)) + label_spacing
total_y_span = (grid_rows * (label_y_span+label_spacing)) + label_spacing

print(
    "total bed size needed for grid size {grid_rows}x{grid_cols}={total_labels_printed} is {total_x_span}mm x {total_y_span}mm".
        format(grid_rows = grid_rows, grid_cols = grid_cols, total_x_span = total_x_span, total_y_span = total_y_span, total_labels_printed = total_labels_printed))

scad_text = "include <../GenerateLabel.scad>\n\nrotate([0, 180, 0]) {\n"
scad_bg = "include <../GenerateLabel.scad>\n\nrotate([0, 180, 0]) {\n"
scad_core = "include <../GenerateLabel.scad>\n\nrotate([0, 180, 0]) {\n"

with open('labels.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_no = 0
    grid_row = 0
    grid_col = 0
    for row in csv_reader:
        if line_no != 0 and line_no <= total_labels_printed:
            if grid_col >= grid_cols:
                grid_col = 0
                grid_row += 1

            #top left
            origin_x = (total_x_span/2)-(label_x_span/2);
            origin_y = (total_y_span/2)-(label_y_span/2);

            location_x = ((grid_col * (label_x_span + label_spacing)) + label_spacing) - origin_x
            location_y = ((grid_row * (label_y_span + label_spacing)) + label_spacing) - origin_y

            scad_snippet_text = "\ttranslate([{location_x}, {location_y}, 0]) {{\n".format(location_x=location_x, location_y=location_y)
            scad_snippet_bg = "\ttranslate([{location_x}, {location_y}, 0]) {{\n".format(location_x=location_x, location_y=location_y)
            scad_snippet_bg += "\t\tGenerateLabel(title=\"\", subtitle=\"\", backgroundOnly=true);\n"
            scad_snippet_core = "\ttranslate([{location_x}, {location_y}, 0]) {{\n".format(location_x=location_x, location_y=location_y)
            scad_snippet_core += "\t\tGenerateLabel(title=\"\", subtitle=\"\", coreOnly=true);\n"

            title = row[0]
            subtitle = None
            if len(row) > 1:
                subtitle = row[1]
                scad_snippet_text += "\t\tGenerateLabel(title=\"{title}\", subtitle=\"{subtitle}\", textOnly=true);\n".format(title=title.strip().replace("\"", "\\\""), subtitle=subtitle.strip().replace("\"", "\\\""))
            else:
                scad_snippet_text += "\t\tGenerateLabel(title=\"{title}\", textOnly=true);\n".format(title=title.strip().replace("\"", "\\\""))

            scad_snippet_text += "\t}\n"
            scad_snippet_bg += "\t}\n"
            scad_snippet_core += "\t}\n"

            scad_text+=scad_snippet_text
            scad_bg+=scad_snippet_bg
            scad_core+=scad_snippet_core

            grid_col += 1
        line_no += 1
scad_text += "}\n"
scad_bg += "}\n"
scad_core += "}\n"

f = open("tmp/text.scad", "w")
f.write(scad_text)
f.close()

f = open("tmp/bg.scad", "w")
f.write(scad_bg)
f.close()

f = open("tmp/core.scad", "w")
f.write(scad_core)
f.close()

f = open("tmp/preview.scad", "w")
f.write(scad_core + scad_bg + scad_text)
f.close()

