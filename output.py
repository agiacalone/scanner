from easygui import  *

class output:

    def output_text(result, token_status):
        return print("Token Discovered is", result, "->", token_status.rstrip())
        
    def output_gui(output_message, output_title, output_text):
        return textbox(msg=output_message, title=output_title, text=output_text, codebox=0)
        
    def output_dict(output_message, output_title, dictionary):
        pretty_dict = 'Count' + '\t' + 'ID' + '\n\n'
        for k, v in sorted(dictionary.items(), key=lambda count: count[1], reverse=True):
            pretty_dict += (str(v) + '\t' + str(k) + '\n')
        return textbox(msg=output_message, title=output_title, text=pretty_dict, codebox=0)
