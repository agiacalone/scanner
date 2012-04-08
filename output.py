from easygui import  *

class output:

    def output_text(result, token_status):
        return print("Token Discovered is", result, "->", token_status.rstrip())
        
    def output_gui(output_message, output_title, output_text):
        return textbox(msg=output_message, title=output_title, text=output_text, codebox=0)
