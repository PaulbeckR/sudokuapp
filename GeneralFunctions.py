# import pygame

# def get_box_elements(grid,i,j):
#     box_i = i // 3
#     box_j = j // 3
#     box_elements=[]
#     for row in range(box_i*3, box_i*3 + 3):
#         for col in range(box_j*3, box_j*3 + 3):
#             #what follows here will do for each element in a box.
#             box_elements.append(grid[row][col])
#     return box_elements

# #my_box = get_box_elements(grid, 6,4)
# # print(my_box)

# #location will be box, row, col. nums will be a list
# #def remove_nums(grid, location,  nums):
#  #   if location == square:

#   #  any(nums in location for range(9))
  
# '''
# Function that wraps text for pygame. Used for wrapping possible solution numbers
# that are shown as a list. Wrap inside box. 

# '''  

# def wrap_text_display(number_list, font, colour, x,y,screen, allowed_width):
#     #splitting numbers array into 
#     numbers_string = ",".join(map(str, numbers))
#     numbers = numbers_string.split(",")
    
#     #create lines
#     lines = []
    
    
#     while len(numbers) > 0:
#         #fill each line to their max
#         line_numbers = []
#         line_width = 0
#         while len(numbers) > 0: 
#             fit_length, fit_height = font.size(' '.join(line_numbers + numbers[:1]))
           
#             if line_width + font.metrics(numbers[0])[0][4] > allowed_width:
                
#                 break
#             line_width += font.metrics(numbers[0])[0][4]
            
#             line_numbers.append(numbers.pop(0))
       

#         lines.append(','.join(line_numbers))
   
    
#     y_offset = 0
#     for line in lines:
#         fit_length, fit_height = font.size(line)
        
#         tx = x - fit_length / 2 
#         ty = y +  y_offset
        
#         font_surface = font.render(line, True, colour)
#         print("font surface is : ", font_surface)
#         screen.blit(font_surface, (tx, ty))
        
#         y_offset += fit_height
        
# # try again

# def wrap(text, fontname=None, fontsize=None, sysfontname=None,
#          bold=None, italic=None, underline=None, width=None, widthem=None, strip=None):
#     if widthem is None:
#         font = getfont(fontname, fontsize, sysfontname,
#                        bold, italic, underline)
#     elif width is not None:
#         raise ValueError("Can't set both width and widthem")
#     else:
#         font = getfont(fontname, REFERENCE_FONT_SIZE,
#                        sysfontname, bold, italic, underline)
#         width = widthem * REFERENCE_FONT_SIZE
#     if strip is None:
#         strip = DEFAULT_STRIP
#     texts = text.replace("\t", "    ").split("\n")
#     lines = []
#     for text in texts:
#         if strip:
#             text = text.rstrip(" ")
#         if width is None:
#             lines.append(text)
#             continue
#         if not text:
#             lines.append("")
#             continue
#         # Preserve leading spaces in all cases.
#         a = len(text) - len(text.lstrip(" "))
#         # At any time, a is the rightmost known index you can legally split a line. I.e. it's legal
#         # to add text[:a] to lines, and line is what will be added to lines if
#         # text is split at a.
#         a = text.index(" ", a) if " " in text else len(text)
#         line = text[:a]
#         while a + 1 < len(text):
#             # b is the next legal place to break the line, with bline the
#             # corresponding line to add.
#             if " " not in text[a + 1:]:
#                 b = len(text)
#                 bline = text
#             elif strip:
#                 # Lines may be split at any space character that immediately follows a non-space
#                 # character.
#                 b = text.index(" ", a + 1)
#                 while text[b - 1] == " ":
#                     if " " in text[b + 1:]:
#                         b = text.index(" ", b + 1)
#                     else:
#                         b = len(text)
#                         break
#                 bline = text[:b]
#             else:
#                 # Lines may be split at any space character, or any character immediately following
#                 # a space character.
#                 b = a + 1 if text[a] == " " else text.index(" ", a + 1)
#             bline = text[:b]
#             if font.size(bline)[0] <= width:
#                 a, line = b, bline
#             else:
#                 lines.append(line)
#                 text = text[a:].lstrip(" ") if strip else text[a:]
#                 a = text.index(" ", 1) if " " in text[1:] else len(text)
#                 line = text[:a]
#         if text:
#             lines.append(line)
#     return lines