import ctypes
import os
import tkinter as tk
import dearpygui.dearpygui as dpg
from data_base import java_library
import textwrap

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

root = tk.Tk()
user_width = root.winfo_screenwidth()
user_height = root.winfo_screenheight()
root.destroy()

DESIGN_WIDTH = 1920.0
DESIGN_HEIGHT = 1080.0

ratio_x = user_width / DESIGN_WIDTH
ratio_y = user_height / DESIGN_HEIGHT

def scale_x(val):
    return int(val * ratio_x)

def scale_y(val):
    return int(val * ratio_y)

dpg.create_context()

calculated_height = 0

def button_callback(ID, Nothing, user_data):
    dpg.delete_item("results_container", children_only=True)
    dpg.delete_item("lines_container", children_only=True)
    concept_data = java_library.get(user_data)
    
    pos = [scale_x(575), scale_y(35)]
    
    glow = dpg.add_text(
        f"---{user_data}---", 
        pos=[pos[0] + scale_x(2), pos[1] + scale_y(1)], 
        color=[255, 50, 255, 255], 
        parent="results_container"
    )
    
    title = dpg.add_text(f"---{user_data}---", pos=pos, color=[255, 50, 255, 255], parent="results_container")
    
    dpg.bind_item_font(title, big_bold_font)
    dpg.bind_item_font(glow, big_bold_font)

    dpg.add_spacer(height=scale_y(20), parent="results_container")

    syntax_lines = concept_data["syntax"].split("\n")
    desc_lines = concept_data["desc"].split("\n")
    
    max_chars = max(len(line) for line in syntax_lines) if syntax_lines else 0
    total_lines = len(syntax_lines)
    
    dynamic_width = max(scale_x(150), (max_chars * scale_x(9)) + scale_x(30)) 
    dynamic_height = max(scale_y(50), (total_lines * scale_y(20)) + scale_y(30))

    COLOR_DEFAULT = [220, 220, 224, 255] 
    COLOR_KEYWORD = [255, 146, 43, 255]   
    COLOR_STRING = [31, 255, 166, 255]  
    COLOR_COMMENT = [128, 128, 128, 255] 
    COLOR_TiTles = [230, 219, 116, 255]
    
    KEYWORDS = {
        "public", "private", "protected", "class", "interface", 
        "extends", "implements", "import", "package", "new", "this",
        "if", "else", "switch", "case", "default", "break", 
        "continue", "return", "for", "while", "try", "catch", "finally",
        "int", "double", "float", "boolean", "char", "void", "static", 
        "final", "abstract", "var", "String","enum"
    }

    syntax_x = scale_x(575) - ((len(f"---{user_data}---") + 6) * scale_x(22)) / 2
    syntax_y = scale_y(100)
    
    syntax = dpg.add_text("SYNTAX:", color=COLOR_TiTles, pos=[syntax_x, syntax_y], parent="results_container")
    dpg.bind_item_font(syntax, BIGcode_font)
    
    group_x = scale_x(575) - ((len(f"---{user_data}---") + 6) * scale_x(22)) / 2
    group_y = scale_y(150)
    
    with dpg.group(pos=[group_x, group_y], parent="results_container"):
        with dpg.child_window(width=dynamic_width, height=dynamic_height, no_scrollbar=True) as code_box:
            for line in syntax_lines:
                with dpg.group(horizontal=True, horizontal_spacing=1):
                    if "//" in line:
                        code_part, comment_part = line.split("//", 1)
                        comment_part = "//" + comment_part 
                    else:
                        code_part = line
                        comment_part = ""
                    words = code_part.split(" ")
                    in_string = False 
                    in_quote = False 
                    maybe_in_string = False
                    for word in words:
                        if not word: 
                            continue
                        if word in KEYWORDS:
                            word_item = dpg.add_text(word, color=COLOR_KEYWORD)
                            dpg.bind_item_font(word_item, code_font)
                        #elif word in KEYWORDS and (word=="enum" or word=="void"):
                         #   keyword=True
                          #  word_item = dpg.add_text(word, color=COLOR_KEYWORD)
                         #   dpg.bind_item_font(word_item, code_font)
                        else:
                            for letter in word:
                                if not in_quote and letter == "'":
                                    in_quote = True
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                elif in_quote and letter == "'":
                                    in_quote = False
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                elif not in_string and letter == '"':
                                    in_string = True
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                elif in_string and not maybe_in_string and letter == '"':
                                    in_string = False
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                elif in_string and letter == "\\":
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                    maybe_in_string = True
                                elif in_string and maybe_in_string and letter == '"':
                                    maybe_in_string = False
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                elif in_string:
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                elif in_quote:
                                    letter_item = dpg.add_text(letter, color=COLOR_STRING)
                                    dpg.bind_item_font(letter_item, code_font)
                                else:
                                    letter_item = dpg.add_text(letter, color=COLOR_DEFAULT)
                                    dpg.bind_item_font(letter_item, code_font)
                        dpg.add_text(" ")            
                    if comment_part:
                        comment_item = dpg.add_text(comment_part, color=COLOR_COMMENT)
                        dpg.bind_item_font(comment_item, code_font)
                        
    dpg.bind_item_theme(code_box, code_box_theme)

    desc_y = dynamic_height + scale_y(200)
    description = dpg.add_text("DESCRIPTION:", color=COLOR_TiTles, pos=[group_x, desc_y], parent="results_container")
    dpg.bind_item_font(description, BIGcode_font)
    
    current_line_y = dynamic_height + scale_y(240) 
    line_spacing = scale_y(22) 
    
    for paragraph in desc_lines:
       
        wrapped_chunks = textwrap.wrap(paragraph, width=150)
        
        if not wrapped_chunks:
            current_line_y += line_spacing
            continue
            
        for chunk in wrapped_chunks:
            with dpg.group(horizontal=True, horizontal_spacing=1, pos=[group_x, current_line_y], parent="results_container"):
                line_item = dpg.add_text(chunk, color=COLOR_DEFAULT)
                dpg.bind_item_font(line_item, code_font)
            current_line_y += line_spacing

def check_input(ID, user_input):
    text = user_input.lower()
    i = 0
    dpg.delete_item("results_container", children_only=True)
    dpg.delete_item("lines_container", children_only=True)
    
    for key in java_library.keys():
        if text in key and text != "" and text != " ":
            new_button = dpg.add_button(
                label=key, 
                parent="results_container", 
                width=scale_x(300),
                height=scale_y(20),
                callback=button_callback, 
                user_data=key            
            )
            dpg.bind_item_theme(new_button, text_button_theme)
            i += 1
            
    if i == 0 and text != "":
        dpg.add_text("not found", parent="results_container")
        
    elif i != 0 and text != "" and text != " ":
        if i == 1:
            calculated_height = scale_y(50)
        else:
            calculated_height = scale_y(50) + (i - 1) * scale_y(25)
            
        x_left = 0
        x_right = scale_x(375)  
        y_top = scale_y(30)
        y_bottom = calculated_height 
        
        line_color = [255, 255, 255, 100]
        line_thick = 1
        
        dpg.draw_line(p1=[x_left, y_top], p2=[x_right, y_top], parent="lines_container", color=line_color, thickness=line_thick)
        dpg.draw_line(p1=[x_left, y_bottom], p2=[x_right, y_bottom], parent="lines_container", color=line_color, thickness=line_thick)
        dpg.draw_line(p1=[x_left, y_top], p2=[x_left, y_bottom], parent="lines_container", color=line_color, thickness=line_thick)
        dpg.draw_line(p1=[x_right, y_top], p2=[x_right, y_bottom], parent="lines_container", color=line_color, thickness=line_thick)


with dpg.theme() as text_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 255, 255, 30])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [255, 255, 255, 60])
        dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.0, 0.5)
        

font_large_size = max(20, scale_y(40))
font_small_size = max(10, scale_y(15))
font_medium_size = max(15, scale_y(30))


with dpg.font_registry():
    with dpg.font("C:\\Windows\\Fonts\\arial.ttf", font_large_size) as big_bold_font: 
        pass
    with dpg.font("C:\\Windows\\Fonts\\consola.ttf", font_small_size) as code_font:
        pass
    with dpg.font("C:\\Windows\\Fonts\\consola.ttf", font_medium_size) as BIGcode_font:
        pass


with dpg.theme() as code_box_theme:
    with dpg.theme_component(dpg.mvChildWindow):
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, [20, 20, 23, 255])
        dpg.add_theme_color(dpg.mvThemeCol_Border, [60, 60, 65, 255])
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 6)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 12, 12)


with dpg.window(tag="primary_window", no_title_bar=True, no_move=True, no_resize=True):

    input_check = dpg.add_input_text(hint="Search here...", callback=check_input)

    dpg.add_draw_node(tag="lines_container")
    
    with dpg.group(pos=[scale_x(15), scale_y(40)]):
        dpg.add_group(tag="results_container")  
    

viewport_w = scale_x(600)
viewport_h = scale_y(400)

dpg.create_viewport(title="Java Syntax Researcher", width=viewport_w, height=viewport_h)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary_window", True)
dpg.start_dearpygui()
dpg.destroy_context()
